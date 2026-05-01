import axios from "axios";

export interface OrderRequest {
  symbol: string;
  side: string;
  order_type: string;
  quantity: number;
  price?: number | null;
}

export interface OrderResponse {
  orderId: number;
  status: string;
  executedQty: string;
  avgPrice: string;
}

export const placeOrder = async (data: OrderRequest) => {
  const res = await axios.post<OrderResponse>(
    "http://127.0.0.1:8000/trade",
    data
  );
  return res.data;
};