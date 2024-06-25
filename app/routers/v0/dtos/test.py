from pydantic import BaseModel

class TestRequest(BaseModel):
    context: str

class TestResponse(BaseModel):
    message: str

