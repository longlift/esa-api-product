from fastapi import APIRouter
from domain.model.product_detail.model import Request
from features.product_detail.handler import Handler
from features.product_detail.repository import Repository
from features.product_detail.service import Service

router = APIRouter()


@router.post("")
def getProductDetail(request: Request):
    repo = Repository()
    service = Service(repo)
    handler = Handler(service)
    return handler.getProductDetail(request)
