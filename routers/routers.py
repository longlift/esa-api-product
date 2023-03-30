from fastapi import FastAPI, APIRouter
from features.product_detail import router as product_detail

router = APIRouter()


def PublicRoutes(app: FastAPI):
    router.include_router(product_detail.router, prefix="/ProductDetail")

    app.include_router(router, prefix="/Learning")
