from sqlmodel import Field, SQLModel
class User(SQLModel,table=True): # type: ignore
    id: int = Field(primary_key=True)
    username: str
    email: str

class UserUpdate(SQLModel):
    username: str | None = None
    email: str | None = None
    