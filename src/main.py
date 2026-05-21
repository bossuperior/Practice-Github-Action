from fastapi import FastAPI


app = FastAPI()


@app.get("/", tags=["home"])
async def home() -> dict:
    return {"message": "Hello world Boss", "status": True}
