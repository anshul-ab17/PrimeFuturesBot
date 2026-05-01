from fastapi import FastAPI
from pydantic import BaseModel
from bot.client import get_client
from bot.orders import place_order
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class OrderRequest(BaseModel):
    symbol: str
    side: str
    order_type: str
    quantity: float
    price: float | None = None

@app.post("/trade")
def trade(order: OrderRequest):
    client = get_client()

    response = place_order(
        client,
        order.symbol,
        order.side,
        order.order_type,
        order.quantity,
        order.price
    )

    return {
        "orderId": response.get("orderId"),
        "status": response.get("status"),
        "executedQty": response.get("executedQty"),
        "avgPrice": response.get("avgPrice"),
    }