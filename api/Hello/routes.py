# api/hello/routes.py

from fastapi import APIRouter

router = APIRouter(prefix="/hello", tags=["Hello"])

@router.get("/")
async def hello_world():
    return {"message": "Hello World!"}