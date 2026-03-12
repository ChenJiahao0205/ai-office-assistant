
from fastapi import FastAPI
from upload import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    return {"status": "AI Office Assistant running"}

