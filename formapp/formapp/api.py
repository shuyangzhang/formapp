# coding=utf-8

from django.conf import settings
from django.utils.datastructures import MultiValueDictKeyError

RET_OK = 1
RET_ERR = 2
HTTP_STATUS_ERR = None

class ApiError(Exception):
    code = RET_OK

    def __init__(self, message, code=None, http_status=None):
        self.message = str(message)
        self.code = int(code) if code is not None else RET_ERR

        self.http_status = http_status

    def __str__(self):
        code = '' if self.code == RET_ERR else (" (%d)" % self.code)
        return "ApiError: %s%s" % (self.message, code)

    def __repr__(self):
        status = '' if self.http_status is None else ", " + str(self.http_status)
        return 'ApiError("%s", %d%s)' %(self.message, self.code, status)

    def to_dict(self):
        return {"code": self.code, "message": self.message}

    def get_http_status_code(self):
        return self.http_status or HTTP_STATUS_ERR
