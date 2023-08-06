class WindowDoesNotExistException(Exception):
    def __init__(self, winname):
        self.winname = winname

    def __str__(self):
        return f"'{self.winname}' Window Does Not Exist"


class MessageDoesNotExistException(Exception):
    def __init__(self, funcname):
        self.funcname = funcname

    def __str__(self):
        return f"{self.funcname} This function has no return value"
