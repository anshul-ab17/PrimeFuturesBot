import { useState } from "react";
import { placeOrder } from "../lib/api";

export default function OrderForm({ setResult }: any) {
  const [form, setForm] = useState({
    symbol: "BTCUSDT",
    side: "BUY",
    order_type: "MARKET",
    quantity: "0.01",
    price: "",
  });
  const [error, setError] = useState<string | null>(null);

  const submit = async () => {
    setError(null);
    try {
      const res = await placeOrder({
        ...form,
        quantity: Number(form.quantity),
        price: form.price ? Number(form.price) : null,
      });
      setResult(res);
    } catch (err: any) {
      const message =
        err?.response?.data?.detail ||
        err?.message ||
        "Failed to place order. Is the backend running?";
      setError(message);
    }
  };

  return (
    <div className="p-4 border rounded-lg space-y-2">
      <h2 className="text-lg font-semibold">Place Order</h2>

      <input
        className="border p-2 w-full"
        value={form.symbol}
        onChange={(e) => setForm({ ...form, symbol: e.target.value })}
      />

      <select
        className="border p-2 w-full"
        onChange={(e) => setForm({ ...form, side: e.target.value })}
      >
        <option>BUY</option>
        <option>SELL</option>
      </select>

      <select
        className="border p-2 w-full"
        onChange={(e) =>
          setForm({ ...form, order_type: e.target.value })
        }
      >
        <option>MARKET</option>
        <option>LIMIT</option>
        <option>STOP_MARKET</option>
      </select>

      <input
        className="border p-2 w-full"
        value={form.quantity}
        onChange={(e) => setForm({ ...form, quantity: e.target.value })}
      />

      <input
        className="border p-2 w-full"
        placeholder="Price (if needed)"
        value={form.price}
        onChange={(e) => setForm({ ...form, price: e.target.value })}
      />

      <button
        className="bg-blue-500 text-white px-4 py-2 rounded"
        onClick={submit}
      >
        Submit
      </button>

      {error && (
        <p className="text-red-500 text-sm">{error}</p>
      )}
    </div>
  );
}