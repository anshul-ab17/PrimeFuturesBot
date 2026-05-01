import "./index.css";


import { useState } from "react";
import UserProfile from "./components/UserProfile.tsx";
import PriceChart from "./components/PriceChart";
import OrderForm from "./components/OrderForm";
import OrderResult from "./components/OrderResult";

function App() {
  const [result, setResult] = useState<any>(null);

  return (
    <div className="max-w-xl mx-auto p-6 space-y-4">
      <h1 className="text-2xl font-bold">Trading Dashboard</h1>

      <UserProfile />
      <PriceChart />
      <OrderForm setResult={setResult} />
      <OrderResult result={result} />
    </div>
  );
}

export default App;