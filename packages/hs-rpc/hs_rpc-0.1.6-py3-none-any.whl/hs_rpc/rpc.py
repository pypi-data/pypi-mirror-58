'''
编译命令
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./rpc_data.proto
'''
import json
import os
import threading
import time
import requests

from hs_rpc.exceptions import RpcFuncRegisterError, AuthFailedError, RpcError, NotFoundError
from hs_rpc.request import rpc_request_invoke


os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

def rpc_server_invoke(request):
    """
    服务端调用入口
    :param request: 客户端传入的请求对象
    :return: 响应
    """
    try:
        request_data = json.loads(request)
        rule = request_data.pop('func')
        response = rpc.dispatch(rule, **request_data)
    except Exception as e:
        response = Response(e.args[0], code=500, success=False)
    return json.dumps(response.__dict__)


class Response:
    def __init__(self, message, code=200, success=True):
        self.message = message
        self.code = code
        self.success = success


class RpcServerHelper:

    def __init__(self):
        self.app = None
        self.rpc_map = {}
        self.response_class = Response

    def rpc(self, rule=None, token_verify=True):
        """
        rpc函数注册器
        :param rule: rpc函数注册名
        :param token_verify: 是否需要验证token才能访问
        :return:
        """
        def decorator(rpc_func):
            self.add_rpc_rule(rule, rpc_func, token_verify)
            return rpc_func

        return decorator

    def add_rpc_rule(self, rule, rpc_func, token_verify):
        """
        注册rpc函数到映射器
        :param rule: rpc函数注册名
        :param rpc_func: 装饰的函数
        :param token_verify: 是否需要验证token才能访问
        """
        if rule is None:
            rule = self._endpoint_from_rpc_func(rpc_func)

        if rpc_func is not None:
            old_func_obj = self.rpc_map.get(rule)
            if old_func_obj is not None:
                old_func = old_func_obj['func']
                if old_func != rpc_func:
                    raise RpcFuncRegisterError('rpc函数注册规则重复【%s】' % rule)
            self.rpc_map[rule] = {'func':rpc_func, 'token_verify':token_verify}

    def _endpoint_from_rpc_func(self, rpc_func):
        """
        如果不提供端点，则使用函数名作为key注册
        :param rpc_func: 提供注册为rpc服务函数的注册名
        :return:
        """
        assert rpc_func is not None, 'expected rpc_func if endpoint ' \
                                     'is not provided.'
        return rpc_func.__name__

    def _verify_token(self, token):
        """
        验证token，此时又可以作为客户端访问。。。。。
        :param token:
        :return:
        """
        rpc_request_invoke(func='token_verify', message=token, app_rpc='HSRIGHT')


    def dispatch(self, rule, **options):
        with self.app.app_context():
            try:
                func =  self.rpc_map.get(rule)
                if not func:
                    raise NotFoundError('请求错误, 不存在{}函数!'.format(rule))
                if func['token_verify']:
                    token = options.pop('token')
                    if not token:
                        return AuthFailedError('未传入token')
                    self._verify_token({'token':token})
                return self.make_response(func['func'](**options))
            except RpcError as e:
                message, code = e.description, e.code
                return self.response_class(message=message, code=code, success=False)
            except Exception as e:
                raise e

    def make_response(self, rv):
        if isinstance(rv, tuple):
            if len(rv) == 2:
                message, code = rv
                return self.response_class(message=message, code=code)
            elif len(rv) == 3:
                message, code, success = rv
                return self.response_class(message=message, code=code, success=success)
            else:
                raise TypeError('服务器内部错误:未返回一个有效元组，(message, code, success)')

        if isinstance(rv, (dict, list, str, int)) or rv is None:
            return self.response_class(message=rv)

        if not isinstance(rv, self.response_class):
            raise TypeError('服务器内部错误:rpc函数必须返回一个Response实例，或者元组(message, code)')

        return rv

    def run(self, app):
        self.app = app

        # 在flask启动服务时来激活rpc服务
        @app.before_first_request
        def activate_rpc():
            from hs_rpc.server import serve
            t = threading.Thread(target=serve, args=(app,))
            t.start()

        # 循环去激活activate_rpc执行，这里会稍微有些绕
        def start_loop():
            not_started = True
            while not_started:
                try:
                    r = requests.get('http://localhost:{}/'.format(8080))
                    if r.status_code == 200:
                        self.app.logger.info('rpc服务已启动成功！！！')
                        not_started = False
                except:
                    self.app.logger.info('rpc服务启动中...')
                time.sleep(2)

        app.logger.info('正在激活rpc服务...')
        t = threading.Thread(target=start_loop)
        t.start()



rpc = RpcServerHelper()