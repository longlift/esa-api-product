from domain.model.product_detail.model import Request
from domain.model.response import Response


class Service:
    def __init__(self, repo):
        self.repo = repo

    def selectProductDetail(self, request: Request):
        res = Response()

        data, e = self.repo.selectProductDetail(productId=request.productId)
        if None is not e:
            res.err(message=str(e), response=None)
            return res
        if None is data:
            res.err(message="data not found", response=None)
            return res

        res.ok(message="Success", response=data)
        return res
