import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
} from "chart.js";
import { Line } from "react-chartjs-2";

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement);

export default function PriceChart() {
  const data = {
    labels: ["1", "2", "3", "4", "5"],
    datasets: [
      {
        label: "BTC Price",
        data: [60000, 61000, 60500, 62000, 61500],
        borderColor: "#3b82f6",
      },
    ],
  };

  return (
    <div className="p-4 border rounded-lg">
      <h2 className="text-lg font-semibold mb-2">Price Chart</h2>
      <Line data={data} />
    </div>
  );
}