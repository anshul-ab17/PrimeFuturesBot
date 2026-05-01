export default function OrderResult({ result }: any) {
  if (!result) return null;

  return (
    <div className="p-4 border rounded-lg">
      <h2 className="text-lg font-semibold">Order Result</h2>
      <p>Order ID: {result.orderId}</p>
      <p>Status: {result.status}</p>
      <p>Executed Qty: {result.executedQty}</p>
      <p>Avg Price: {result.avgPrice}</p>
    </div>
  );
}