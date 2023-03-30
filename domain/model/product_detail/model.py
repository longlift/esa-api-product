from pydantic import BaseModel, validator


class Request(BaseModel):
    productId: int

    def validateModel(self):
        if self.productId == 0 or self.productId is None:
            return "productId is required."
        return None
