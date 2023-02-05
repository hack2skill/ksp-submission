import React from "react";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Pie } from "react-chartjs-2";

ChartJS.register(ArcElement, Tooltip, Legend);

export default function PieChart() {
  const data = {
    labels: ["Existing Records", "Newly Added Records"],
    datasets: [
      {
        label: "Records",
        data: [12, 19],
        backgroundColor: ["rgba(206,81,82,0.7)","rgba(189,255,0,0.7)"],
        borderColor: ["rgb(206,81,82,1)","rgba(189,255,0,1)"],
        borderWidth: 1,
      },
    ],
  };

  return <Pie data={data} />;
}
