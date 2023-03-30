from fastapi import FastAPI
from routers import routers

app = FastAPI()

routers.PublicRoutes(app)

