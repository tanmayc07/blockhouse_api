from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Blockhouse API"}

@app.get("/orders")
async def get_orders():
    return {"orders": {1, 2, 3, 4}}