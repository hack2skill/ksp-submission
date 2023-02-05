import React from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
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
      text: "Newly Added Data",
    },
  },
};

export default function BarChart() {
  const labels = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
  ];

  const data = {
    labels,
    datasets: [
      {
        label: "State portal",
        data: [12, 24, 46, 78, 45, 98, 56],
        backgroundColor: "rgba(189,255,0,0.5)",
      },
      {
        label: "National portal",
        data: [42, 64, 96, 70, 41, 78, 6],
        backgroundColor: "rgba(206,81,82,0.5)",
      },
    ],
  };

  return (
    <>
      <Bar options={options} data={data} />
    </>
  );
}
