from fastapi import FastAPI
from returns import router

app = FastAPI(
    title="Return & Exchange Management API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "Return & Exchange Management API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(router)