from fastapi import FastAPI
from pydantic import BaseModel,Field
from enum import Enum
app = FastAPI(
    title="Return & Exchange Management API",
    version="1.0.0"
)
class RequestType(Enum):
    RETURN = "return"
    EXCHANGE = "exchange"


class ReturnReason(Enum):
    DEFECTIVE = "defective"
    WRONG_PRODUCT = "wrong_product"
    CHANGED_MIND = "changed_mind"


class ReturnRequest(BaseModel):
    order_id: str = Field(min_length=1)
    product_code: str = Field(min_length=1)
    request_type: RequestType
    reason: ReturnReason
    


@app.get("/")
def root():
    return {"message": "Return & Exchange Management API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/returns")
def create_return(return_request: ReturnRequest):
    return {
        "order_id": return_request.order_id,
        "product_code": return_request.product_code,
        "request_type": return_request.request_type,
        "reason": return_request.reason
    }