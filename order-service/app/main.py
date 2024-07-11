from fastapi import FastAPI ,Depends 
from app.order_crud.crud import OrderService
from sqlmodel import Session , SQLModel
from app import database
from app.model.order import Order ,orderUpdate
from app.database import engine
from app.hello_ai import chat_completion


app = FastAPI()

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)



order_service = OrderService()

# Assuming models.py exists
@app.post("/orders/", response_model=Order)
async def create_order(order:Order, session:Session = Depends(database.get_session)):
    await order_service.create_order(session, order)
    return order


@app.get("/orders/", response_model=list[Order])
async def read_orders(session: Session = Depends(database.get_session)):
    return await order_service.read_orders(session)


@app.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: int, session: Session = Depends(database.get_session)):
    return await order_service.get_order(session, order_id)


@app.patch("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, order_data:orderUpdate, session: Session = Depends(database.get_session)):
    return await order_service.update_order(session, order_id, order_data)


@app.delete("/orders/{order_id}")
async def delete_order(order_id: int, session: Session = Depends(database.get_session)):
    await order_service.delete_order(session, order_id)
    return {"message": f"Order {order_id} deleted."}
@app.get("/hello-ai")
def get_ai_response(prompt:str):
    return chat_completion(prompt)