from fastapi import FastAPI

from routers.setup_router import setup_router

app = FastAPI()
setup_router(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}
