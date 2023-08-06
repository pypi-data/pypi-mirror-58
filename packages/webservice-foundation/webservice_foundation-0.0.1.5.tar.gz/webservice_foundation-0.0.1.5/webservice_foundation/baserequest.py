import json

from tornado.web import RequestHandler

from .bodydata import BodyData
from .originaljsonencoder import OriginalJsonEncoder


class BaseRequestHandler(RequestHandler):

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)

    def initialize(self, **kwargs):
        x_auth_token = 'X-Auth-Token'
        self.request_header = {k: v for k,
                               v in self.request.headers.get_all()}
        self.remote_ip = self.request_header.get(
            'X-Real-IP', self.request.remote_ip)
        if x_auth_token in self.request_header:
            self.request_header[x_auth_token] = json.loads(
                self.request_header[x_auth_token])

        def getArgs(user_args: dict):
            data = {}
            if user_args:
                for key, value in user_args.items():
                    if key not in data:
                        data[key] = []

                    if isinstance(value, list):
                        for v in value:
                            if isinstance(v, bytes):
                                data[key].append(v.decode('utf-8'))
                            else:
                                data[key].append(v)
                    else:
                        data[key].append(value)
            return data
            # return BodyData(data)

        def change_body_data(args):
            data = {}
            for arg in args:
                data.update(args)
            return BodyData(data)
        _dict = []
        if not self.request.files:
            if self.request.body:
                if isinstance(self.request.body, bytes):
                    body = self.request.body.decode('utf-8')
                else:
                    body = self.request.body
                if body:
                    _dict.append(json.loads(body))
        _dict.append(getArgs(self.request.body_arguments))
        _dict.append(getArgs(self.request.query_arguments))
        self.bodydata = change_body_data(_dict)

    def json_write(self, data):
        self.write(json.dumps(data, ensure_ascii=False,
                              cls=OriginalJsonEncoder))
