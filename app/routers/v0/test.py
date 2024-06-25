from fastapi import APIRouter, HTTPException
from app.core.example.example_logic import ExampleLogic
from app.core.repo.aa_repo import AARepo
from app.infra.mm_aa_repo import MMAARepo
from .dto import TestRequest, TestResponse

router = APIRouter(
    prefix="/test",
    tags=["test"]
)

aa_repo: AARepo = MMAARepo()

@router.post("/example")
async def example(request: TestRequest) -> TestResponse:
    try:
        return TestResponse(message="Hello, World!")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
