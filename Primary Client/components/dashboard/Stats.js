import React from "react";
// import { Bar } from "react-chartjs-2";
import BarChart from "./BarChart";
import LineChart from "./LineChart";
import PieChart from "./PieChart";

export default function Stats() {
  return (
    <div class="w-full">
      <div class="flex justify-between mt-4 mx-10 items-center">
        <h1 className="title text-3xl ml-20">Stats</h1>
        <h1 className="desc text-lg">Hello, admin!</h1>
      </div>
      <div className="flex flex-col justify-center">
      <div class="w-5/6 mt-6 mx-auto">
        
          <div class="w-3/4 h-3/4 bg-[#dfdfe51a] backdrop-filter backdrop-blur-3xl  border-[#575555] rounded-lg mx-48 p-4">
            <LineChart />
          </div>
      
      </div>
      <div class="mt-12 ml-20">
        <div class="flex flex-row gap-2 ">
          <div class="w-1/2 h-1/2 bg-[#dfdfe51a] backdrop-filter backdrop-blur-3xl  border-[#575555] rounded-lg mx-auto p-4">
            <BarChart />
          </div>
          <div class="w-88 h-88 mb-6 bg-[#dfdfe51a] backdrop-filter backdrop-blur-3xl  border-[#575555] rounded-lg mx-auto p-4">
            <PieChart />
          </div>
        </div>
      </div>
      </div>
      
    </div>
  );
}
