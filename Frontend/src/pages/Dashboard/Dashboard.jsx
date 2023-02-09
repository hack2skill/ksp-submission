import React from "react";
import { useState, useEffect } from "react";
import { notification } from "antd";
import background from "../../images/upload.jpg";
import { ROUTES } from "../../routes/Routerconfig";
import { useNavigate } from "react-router-dom";
import image1 from "../../images/123.webp";
import dcb from "../../images/aa1.jpg";
import xyz from "../../images/234.png";
import jwt_decode from "jwt-decode";
import "./Dashboard.css";
import Navbar from "../../Components/Navbar";
const Dashboard = () => {
  const navigate = useNavigate();
  const [api, contextHolder] = notification.useNotification();
  const openNotificationWithIcon = (type, message, desc) => {
    api[type]({
      message: `${message}`,
      description: `${desc}`,
    });
  };

  const logout = () => {
    localStorage.removeItem("noty");
    localStorage.removeItem("uid");
    navigate(ROUTES.Home);
  };

  let noty = localStorage.getItem("noty");
  useEffect(() => {
    if (!noty) {
      openNotificationWithIcon("success", "Login", "Successfully Logged In");
    }
    noty = true;
    localStorage.setItem("noty", true);
  }, []);

  return (
    <div className="back">
      {contextHolder}
      <Navbar />
      <button
        class="button-30 text-black ml-[99rem] mt-[4rem] justify-end"
        role="button"
        onClick={() => logout()}
      >
        Log Out
      </button>

      <div className="text-white">
        <p className="pt-[1rem] font-serif text-[4rem]">
          {" "}
          -- Welcome to Dashboard --
        </p>
      </div>

      <div className="grid-cols-2 grid justify-center ml-[10rem] mt-[3rem]">
        <div class="flex items-center justify-center">
          <div class="rounded-lg shadow-lg bg-white max-w-md">
            <a href="#!">
              <img class="rounded-t-lg h-[18rem] w-[29rem]" src={dcb} alt="" />
            </a>
            <div class="p-6">
              <h5 class="text-gray-900 text-3xl font-semibold mb-2">
                Lost Person Identification using Web scrapping technique.
              </h5>
              <p class="text-gray-700 text-lg mb-4">
                Make AI Model to work on identifying lost person details.
              </p>
              <button
                class="button-30 w-[10rem] text-lg mt-[1rem]"
                role="button"
                onClick={() => navigate(ROUTES.LostPerson)}
              >
                Search
              </button>
            </div>
          </div>
        </div>
        <div class="flex items-center justify-center mr-[10rem]">
          <div class="rounded-lg shadow-lg bg-white max-w-md">
            <a href="#!">
              <img class="rounded-t-lg h-[18rem] w-[29rem]" src={xyz} alt="" />
            </a>
            <div class="p-6">
              <h5 class="text-gray-900 text-3xl font-semibold mb-2">
                Data Augmentation to identify frames
              </h5>
              <p class="text-gray-700 text-lg mb-4 mt-[3rem]">
                Using Aritificial Intelligence algorithms to create variations
                of the given data.
              </p>
              <button
                class="button-30 w-[10rem] text-lg mt-[1rem]"
                role="button"
                onClick={() => navigate(ROUTES.Augmentation)}
              >
                Search
              </button>
            </div>
          </div>
        </div>
      </div>
      <div className="grid grid-cols-2 ml-[10em] mt-[8rem]">
        <div class="flex ml-[2rem] items-center justify-center">
          <div class="rounded-lg shadow-lg bg-white max-w-md">
            <a href="#!">
              <img
                class="rounded-t-lg h-[18rem] w-[29rem]"
                src={image1}
                alt=""
              />
            </a>
            <div class="p-6">
              <h5 class="text-gray-900 text-3xl font-semibold mb-2">
                Lost Person Detection using Advanced CCTV Surveillance Footage
              </h5>
              <p class="text-gray-700 text-lg mb-4">
                Make AI Model to work on identifying lost person details.
              </p>
              <button
                class="button-30 w-[10rem] text-lg mt-[1rem]"
                role="button"
                onClick={() => navigate(ROUTES.Missing)}
              >
                Search
              </button>
            </div>
          </div>
        </div>
        <div class="flex justify-center">
          <div class="rounded-lg shadow-lg bg-white max-h-[90rem] mr-[10rem] max-w-md">
            <a href="#!">
              <img
                class="rounded-t-lg h-[18rem] w-[29rem]"
                src={background}
                alt=""
              />
            </a>
            <div class="p-6">
              <h5 class="text-gray-900 text-3xl font-semibold mb-2">
                Partial Face Detection
              </h5>
              <p class="text-gray-700 text-lg mb-4">
                Make AI Model to work on identifying required thief details.
              </p>
              <button
                class="button-30 w-[10rem]  mt-[5.5rem]"
                role="button"
                onClick={() => navigate(ROUTES.Thief)}
              >
                Search
              </button>
            </div>
          </div>
        </div>
      </div>
      <div className="h-[14.3rem]"></div>
    </div>
  );
};
export default Dashboard;
