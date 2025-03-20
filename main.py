from fastapi import APIRouter, FastAPI

app = FastAPI()  # This creates the FastAPI app instance

router = APIRouter()

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}

app.include_router(router)
