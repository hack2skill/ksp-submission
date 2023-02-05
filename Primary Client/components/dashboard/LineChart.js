import React from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export const options = {
  responsive: true,
  plugins: {
    legend: {
      position: "top",
    },
    title: {
      display: true,
      text: "Number of Requests",
    },
  },
};

export default function LineChart() {
  const labels = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  const data = {
    labels,
    datasets: [
      {
        label: "",
        data: [12, 24, 46, 78, 45, 98, 56, 80, 30, 60, 20, 0],
        borderColor: "rgb(189,255,0)",
        backgroundColor: "rgba(189,255,0,0.5)",
      },
      // {
      //   label: "",
      //   data: [42, 64, 96, 70, 41, 78, 6],
      //   borderColor: "rgb(206,81,82)",
      //   backgroundColor: "rgba(206,81,82,0.5)",
      // },
    ],
  };

  return <Line options={options} data={data} />;
}
