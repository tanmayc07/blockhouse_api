from sqlmodel import SQLModel, Field, Session, create_engine

DATABASE_URL = "sqlite:///./blockhouse.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

class Orders(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    symbol: str
    price: float
    quantity: int
    order_type: str
    
def init_db():
    SQLModel.metadata.create_all(engine)