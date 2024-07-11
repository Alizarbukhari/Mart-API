from contextlib import asynccontextmanager
from typing import AsyncGenerator
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from app.consumers.user_consumer import consume_messages
from app.consumers.inventroy_consumer import consume_user_messages
from app import settings

from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session ,SQLModel
from app.crud import usercrud  
from app import database
from app.models.user_model import User
from app.database import engine
import asyncio
import json

SQLModel.metadata.create_all(engine)

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    print("Creating ... ... ?? !!! ")

    task = asyncio.create_task(consume_messages(
        settings.KAFKA_USER_TOPIC, 'broker:19092'))
    asyncio.create_task(consume_user_messages(
        "AddStock",
        'broker:19092'
    ))

    create_db_and_tables()
    yield


app = FastAPI(
    lifespan=lifespan,
    title="Hello World API with DB",
    version="0.0.1",
)


app = FastAPI()


@app.post("/users/", response_model=User)
async def create_user(user: User,db: Session = Depends(database.get_session)):
    producer = AIOKafkaProducer(settings.BOOTSTRAP_SERVER)
    await producer.start()
    try:
        # Produce message
        await producer.send_and_wait(settings.KAFKA_USER_TOPIC)
        userJSON = json.dumps(user.__dict__).encode("utf-8")
        print (userJSON)
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()
     
    db_user = usercrud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return usercrud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_session)):
    users = usercrud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(database.get_session)):
    db_user = usercrud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User, db: Session = Depends(database.get_session)):
    db_user =usercrud.update_user(db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int, db: Session = Depends(database.get_session)):
    db_user = usercrud.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
