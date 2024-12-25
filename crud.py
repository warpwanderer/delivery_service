from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
#from sqlalchemy.exc import NoResultFound
from models import DeliveryRequest, DeliveryStatus

async def create_request(db: AsyncSession, product_name: str):
    try:
        new_request = DeliveryRequest(product_name=product_name)
        db.add(new_request)
        await db.commit()
        await db.refresh(new_request)
        return new_request
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {e}")


async def get_request(db: AsyncSession, request_id: int):
    query = await db.execute(select(DeliveryRequest).where(DeliveryRequest.id == request_id))
    return query.scalars().first()

async def delete_request(db: AsyncSession, request_id: int):
    query = await db.execute(select(DeliveryRequest).where(DeliveryRequest.id == request_id))
    request = query.scalars().first()
    if request and request.status == DeliveryStatus.CREATED:
        await db.delete(request)
        await db.commit()
        return True
    return False

