from fastapi import FastAPI, Form, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db, init_db
from crud import create_request, get_request, delete_request
from schemas import DeliveryRequestCreate, DeliveryRequestResponse

import uvicorn


async def lifespan(app: FastAPI):
    print("Инициализация приложения")
    await init_db()
    yield
    print("Завершение работы приложения")


app = FastAPI(lifespan=lifespan)


# # Создание заявки
# @app.post("/requests/", response_model=DeliveryRequestResponse)
# async def create_delivery_request(request: DeliveryRequestCreate, db: AsyncSession = Depends(get_db)):
#     return await create_request(db, request.product_name)
@app.post(
    "/requests/",
    summary="Создать заявку",
    response_model=DeliveryRequestResponse,
    tags=["Работа с заявками"],
)
async def create_delivery_request(
    product_name: str = Form(...), db: AsyncSession = Depends(get_db)
):
    return await create_request(db, product_name)


# Информация о заявке
@app.get(
    "/requests/{request_id}",
    summary="Информация о заявке",
    response_model=DeliveryRequestResponse,
    tags=["Работа с заявками"],
)
async def get_delivery_request(request_id: int, db: AsyncSession = Depends(get_db)):
    request = await get_request(db, request_id)
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    return request


# Удаление заявки
@app.delete(
    "/requests/{request_id}", summary="Удалить заявку", tags=["Работа с заявками"]
)
async def delete_delivery_request(request_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_request(db, request_id)
    if not success:
        raise HTTPException(status_code=400, detail="Request cannot be deleted")
    return {"detail": "Request deleted successfully"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
