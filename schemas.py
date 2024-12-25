from pydantic import BaseModel
from enum import Enum

# Cостояния заявки
class DeliveryStatus(str, Enum):
    CREATED = "created"
    IN_DELIVERY = "in_delivery"
    DELIVERED = "delivered"

# Cхема для создания
class DeliveryRequestCreate(BaseModel):
    product_name: str  

# Схема для ответа API
class DeliveryRequestResponse(BaseModel):
    id: int
    product_name: str
    status: DeliveryStatus
    
    class Config:
        from_attributes = True
