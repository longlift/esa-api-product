from domain.model.product_detail.model import Request
from domain.model.response import Response


class Handler:
    def __init__(self, service):
        self.service = service

    def getProductDetail(self, request: Request):
        res = Response()

        validate = request.validateModel()
        if validate is not None:
            res.err(message=validate, response=None)
            return res.__dict__

        res = self.service.selectProductDetail(request=request)
        return res.__dict__
