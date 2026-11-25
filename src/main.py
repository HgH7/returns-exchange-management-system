from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Return & Exchange Management API",
    version="1.0.0"
)


class ReturnRequest(BaseModel):
    order_id: str
    product_code: str
    request_type: str
    reason: str


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