import React, { useEffect, useMemo, useState } from "react";
import ImageCapture from "react-image-data-capture";
import axios from "axios";

export default function Fingerprint() {
  const [config, setConfig] = useState({
    video: true,
  });

  useEffect(() => {
    navigator.mediaDevices.enumerateDevices().then((devices) => {
      devices.forEach(function (device) {
        if (device.kind === "videoinput" && device.label === "Camo") {
          setConfig({
            video: {
              deviceId: device.deviceId,
            },
          });
        }
      });
    });
  }, []);


  const onCapture = (imageData) => {
    let form_data = new FormData();
    form_data.append('image', imageData.file);

    axios.post('https://moses-guitars-threatened-kingdom.trycloudflare.com', form_data).then((res) => console.log(res))
  };

  return (
    <div className="w-full">
      <div className="flex justify-between w-full">
        <div className="w-3/4  h-screen ml-20">
          <div className="flex justify-between mt-4 mx-10 items-center">
            <h1 className="title text-3xl">Fingerprint Lookup</h1>
            <h1 className="desc text-lg">Hello, admin!</h1>
          </div>
          <div className="flex">
            <div className="w-1/2">
              <div className="bg-black rounded-xl h-72  mt-10 ml-10">
                <ImageCapture
                  onCapture={onCapture}
                  width={600}
                  userMediaConfig={config}
                />
              </div>
              <div className="flex justify-center  mt-10 space-x-3 ml-10">
                {/*<button className="rounded-xl flex space-x-2 bg-[#BDFF00] p-3 text-black title">*/}
                {/*  <h1>Capture</h1>*/}
                {/*  <svg*/}
                {/*    xmlns="http://www.w3.org/2000/svg"*/}
                {/*    fill="none"*/}
                {/*    viewBox="0 0 24 24"*/}
                {/*    stroke-width="1.5"*/}
                {/*    stroke="currentColor"*/}
                {/*    class="w-6 h-6"*/}
                {/*  >*/}
                {/*    <path*/}
                {/*      stroke-linecap="round"*/}
                {/*      stroke-linejoin="round"*/}
                {/*      d="M6.827 6.175A2.31 2.31 0 015.186 7.23c-.38.054-.757.112-1.134.175C2.999 7.58 2.25 8.507 2.25 9.574V18a2.25 2.25 0 002.25 2.25h15A2.25 2.25 0 0021.75 18V9.574c0-1.067-.75-1.994-1.802-2.169a47.865 47.865 0 00-1.134-.175 2.31 2.31 0 01-1.64-1.055l-.822-1.316a2.192 2.192 0 00-1.736-1.039 48.774 48.774 0 00-5.232 0 2.192 2.192 0 00-1.736 1.039l-.821 1.316z"*/}
                {/*    />*/}
                {/*    <path*/}
                {/*      stroke-linecap="round"*/}
                {/*      stroke-linejoin="round"*/}
                {/*      d="M16.5 12.75a4.5 4.5 0 11-9 0 4.5 4.5 0 019 0zM18.75 10.5h.008v.008h-.008V10.5z"*/}
                {/*    />*/}
                {/*  </svg>*/}
                {/*</button>*/}
                <input type={"file"} onChange={(e) => {
                  let form_data = new FormData();
                  form_data.append('image', e.target.files[0]);

                  axios.post('https://moses-guitars-threatened-kingdom.trycloudflare.com', form_data).then((res) => console.log(res))
                } } className="rounded-xl flex space-x-2 bg-[#BDFF00] p-3 text-black title">
                  {/*Import from file*/}
                  {/*<svg*/}
                  {/*  xmlns="http://www.w3.org/2000/svg"*/}
                  {/*  fill="none"*/}
                  {/*  viewBox="0 0 24 24"*/}
                  {/*  stroke-width="1.5"*/}
                  {/*  stroke="currentColor"*/}
                  {/*  class="w-6 h-6"*/}
                  {/*>*/}
                  {/*  <path*/}
                  {/*    stroke-linecap="round"*/}
                  {/*    stroke-linejoin="round"*/}
                  {/*    d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z"*/}
                  {/*  />*/}
                  {/*</svg>*/}
                </input>
              </div>
            </div>
            <div className="ml-5 flex flex-col mt-10 space-y-4">
              <h1 className="title text-xl">Potential matches</h1>

              <div
                id="card"
                className=" shadow-2xl bg-[#dfdfe520] backdrop-filter backdrop-blur-3xl  border-[#575555] rounded-lg m-2 p-4"
              >
                <div className="flex justify-end">
                  <span class="whitespace-nowrap rounded-full bg-[#BDFF00] px-2.5 py-0.5 text-xs text-black text-end">
                    State portal
                  </span>
                </div>
                <div className="flex space-x-3">
                  <div className="w-24 h-24 bg-gray-200 rounded-xl"></div>
                  <div className="space-y-2">
                    <div className="flex space-x-3">
                      <div className="desc text-gray-500 text-sm">Name</div>
                      <div className="desc text-gray-400 text-sm">
                        Full name
                      </div>
                    </div>
                    <div className="flex space-x-5">
                      <div className="flex space-x-3">
                        <div className="desc text-gray-500 text-sm">Age</div>
                        <div className="desc text-gray-400 text-sm">22</div>
                      </div>
                      <div className="flex space-x-3">
                        <div className="desc text-gray-500 text-sm">
                          Arrested on
                        </div>
                        <div className="desc text-gray-400 text-sm">
                          28/06/2022
                        </div>
                      </div>
                    </div>
                    <div className="flex space-x-3">
                      <div className="desc text-gray-500 text-sm">Location</div>
                      <div className="desc text-gray-400 text-sm">
                        Bangalore, KA.
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div
                id="card"
                className=" shadow-2xl bg-[#dfdfe520] backdrop-filter backdrop-blur-3xl  border-[#575555] rounded-lg m-2 p-4"
              >
                <div className="flex justify-end">
                  <span class="whitespace-nowrap rounded-full bg-[#BDFF00] px-2.5 py-0.5 text-xs text-black text-end">
                    State portal
                  </span>
                </div>
                <div className="flex space-x-3">
                  <div className="w-24 h-24 bg-gray-200 rounded-xl"></div>
                  <div className="space-y-2">
                    <div className="flex space-x-3">
                      <div className="desc text-gray-500 text-sm">Name</div>
                      <div className="desc text-gray-400 text-sm">
                        Full name
                      </div>
                    </div>
                    <div className="flex space-x-5">
                      <div className="flex space-x-3">
                        <div className="desc text-gray-500 text-sm">Age</div>
                        <div className="desc text-gray-400 text-sm">22</div>
                      </div>
                      <div className="flex space-x-3">
                        <div className="desc text-gray-500 text-sm">
                          Arrested on
                        </div>
                        <div className="desc text-gray-400 text-sm">
                          28/06/2022
                        </div>
                      </div>
                    </div>
                    <div className="flex space-x-3">
                      <div className="desc text-gray-500 text-sm">Location</div>
                      <div className="desc text-gray-400 text-sm">
                        Bangalore, KA.
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="w-1/4  h-screen">
          <div className="">
            <div className="h-screen p-5 z-10 bg-[#1313158b] backdrop-filter backdrop-blur-3xl  border-[#575555]">
              <div className="flex justify-center">
                <div className="bg-white h-60 w-60 rounded-xl shadow-xl shadow-[#bbff007b]"></div>
              </div>{" "}
              <div className="flex justify-center mt-10">
                <div className="bg-[#1A1A1D] w-60 rounded-xl p-3">
                  <h1 className="desc text-sm text-white opacity-30">Name</h1>
                  <h1 className="title mt-1 text-2xl text-[#BDFF00]">Name</h1>
                </div>
              </div>{" "}
              <div className="flex justify-center mt-10">
                <div className="bg-[#1A1A1D] w-60 rounded-xl p-3">
                  <h1 className="desc text-sm text-white opacity-30">Name</h1>
                  <h1 className="title mt-1 text-2xl text-[#BDFF00]">Name</h1>
                </div>
              </div>
              <div className="flex justify-center space-x-2">
                <div className="flex justify-center mt-10 w-60 space-x-2">
                  <div className="bg-[#BDFF00] text-center text-black desc w-1/2 rounded-xl p-3 title">
                    View more
                  </div>
                  <div className="bg-[#BDFF00] text-center text-black desc w-1/2 rounded-xl p-3 title">
                    Save
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
