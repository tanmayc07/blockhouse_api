from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from database import Orders, engine, init_db

app = FastAPI()

'''
Database Integration
'''
init_db()

def get_db():
    with Session(engine) as session:
        yield session

'''
Routes
'''
@app.get("/")
async def root():
    return {"message": "Welcome to Blockhouse API"}

@app.get("/orders")
async def get_orders(db: Session = Depends(get_db)):
    return db.exec(select(Orders)).all()

@app.post("/orders")
async def post_order(order: Orders, db: Session = Depends(get_db)):
    db.add(order)
    db.commit()
    db.refresh(order)
    return order