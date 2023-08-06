# coding=utf-8


class InvokeException(Exception):
    err_code = 0
    message = ""

    def __init__(self, message: str = ""):
        if message:
            self.message = message


class ArgsException(InvokeException):
    err_code = 200
    message = "args error."
