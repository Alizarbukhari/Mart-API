from sqlmodel import SQLModel, Field, Relationship

# Inventory Microservice Models
class InventoryItem(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    product_id: int
    variant_id: int | None = None
    quantity: int
    status: str 
    
class InventryUpdate(SQLModel):
    product_id: int | None = None
    variant_id: int | None = None
    Quantity: int | None = None
    status: str | None = None

# class InventoryItemUpdate(SQLModel):
#     pass
