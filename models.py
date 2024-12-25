from sqlalchemy import Column, Integer, String, Enum
from database import Base
import enum


# Cостояния заявки
class DeliveryStatus(str, enum.Enum):
    CREATED = "created"
    IN_DELIVERY = "in_delivery"
    DELIVERED = "delivered"

class DeliveryRequest(Base):
    __tablename__ = "delivery_requests"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, nullable=False)
    status = Column(Enum(DeliveryStatus), default=DeliveryStatus.CREATED)

