from typing import TypeVar, Generic

T = TypeVar('T')


class Response(Generic[T]):
    code: int = None
    message: str = None
    data: T = None

    def err(self, message: str, response: T):
        self.code = -99
        self.message = message
        self.data = response

    def ok(self, message: str, response: T):
        self.code = 200
        self.message = message
        self.data = response
