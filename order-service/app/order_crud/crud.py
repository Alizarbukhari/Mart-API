from fastapi import HTTPException, status 
from app.model.order import Order, orderUpdate
from sqlmodel import Session
class OrderService:

    def __init__(self, session: Session = None):
        self.session = session or Session()

    def create_order(self, order: Order):
        try:
            # Validate order data (optional)
            # ...

            self.session.add(order)
            self.session.commit()
            self.session.refresh(order)  # Refresh object with database values
            return order
        except Exception as e:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error creating order: {str(e)}")

    def read_orders(self):
        orders = self.session.query(Order).all()
        return orders

    def get_order(self, order_id: int):
        order = self.session.query(Order).filter(Order.id == order_id).first()
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order with id {order_id} not found")
        return order

    def update_order(self, order_id: int, order_data: orderUpdate):
        order = self.get_order(order_id)  # Ensure order exists first
        # Update relevant fields in the existing order object
        order.status = order_data.status  # Assuming status is an update field
        # ... update other fields as needed
        self.session.commit()
        return order

    def delete_order(self, order_id: int):
        order = self.get_order(order_id)
        self.session.delete(order)
        self.session.commit()
        return {"message": f"Order with id {order_id} deleted."}
