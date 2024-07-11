from fastapi import FastAPI
from sqlmodel import Field, SQLModel, create_engine
from typing import Optional

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    item_name: str = Field(index=True)
    price : float 
    # Add other relevant order fields like quantity, price, etc.
class orderUpdate(SQLModel):
    item_name: str | None = None
    price: float | None = None
