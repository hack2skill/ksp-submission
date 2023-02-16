import React from "react";
import Navbar from "../Components/Navbar";
import axios from "axios";
import { ROUTES } from "../routes/Routerconfig";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
function AugOutput() {
  const navigate = useNavigate();
  var images = [];
  const importAll = (r) => {
    return r.keys().reduce((acc, key) => {
      acc.push({ name: key.split("/").pop().split(".")[0], url: r(key) });
      return acc;
    }, []);
  };

  images = importAll(
    require.context(
      "../Components/augmented/",
      false,
      /\.(png|jpe?g|jpg|svg)$/
    )
  );

  const xyz = () => {
    navigate(ROUTES.Dashboard);
  };
  return (
    <div>
      <Navbar />
      <p className="text-[4rem] pt-[2rem] text-red-600">
        Output Images of Thief With Names
      </p>
      <button
        type="button"
        onClick={xyz}
        class="ml-[98rem] px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded-full shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out justify-end"
      >
        Dashboard
      </button>
      <div className=" grid grid-cols-4">
        {images
          ? images.map((image, index) => {
              return (
                <div className="grid-cols-4">
                  <div className="ml-[5rem] gap-[2rem]">
                    <img
                      className="w-[30rem] rounded-md shadow-2xl mt-[4rem] h-[25rem]"
                      src={image.url}
                    />
                    <p className="pt-[1rem] pr-[3rem] text-2xl"></p>
                  </div>
                </div>
              );
            })
          : null}{" "}
      </div>
    </div>
  );
}

export default AugOutput;
