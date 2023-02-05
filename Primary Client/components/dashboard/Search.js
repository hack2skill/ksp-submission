import React, { useEffect, useState } from "react";
import axios from "axios";
import CsvDownloader from "react-csv-downloader";

export default function Search() {
  const [filters, setFilters] = useState(false);
  const [data, setData] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [search, setSearch] = useState("");
  const [currentP, setCurrentP] = useState(false);


  const states = [
  "Maharashtra",
  "Andhra Pradesh",
  "Uttar Pradesh",
  "Gujarat",
  "Karnataka",
  "Tamil Nadu",
  "Rajasthan",
  "Haryana",
  "Madhya Pradesh",
  "Bihar",
  "Kerala",
  "Odisha",
  "West Bengal",
  "Uttarakhand",
  "Jharkhand",
  "Chhattisgarh",
  "Punjab",
  "Himachal Pradesh",
  "Delhi",
  "Assam",
  "Goa",
  "Jammu and Kashmir",
  "Meghalaya",
  "Telangana",
  "Tripura",
]


  async function handleSubmit(e) {
    e.preventDefault();
    setIsLoading(true);

    var object = {};

    let formData = new FormData(e.target);

    formData.forEach((value, key) => (object[key] = value));

    const res = await axios.get("/api/search", {
      params: object,
    });

    console.log(res.data.data);

    setData(res.data.data);
    setFilters(false);
    setIsLoading(false);
  }

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="w-full">
      <div className="flex justify-between w-full">
        <div className="w-3/4 ml-20">
          <div className="flex justify-between mt-4 mx-10 items-center">
            <h1 className="title text-3xl">Search</h1>
            <h1 className="desc text-lg">Hello, admin!</h1>
          </div>
          <form
            onSubmit={handleSubmit}
            className=" bg-[#BDFF00] rounded-xl mx-10 mt-10 p-5"
          >
            <h1 className="desc text-black">Search for an identity</h1>
            <div className="flex space-x-4 items-center mt-5">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6 text-black"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"
                />
              </svg>

              <input
                className="rounded-md desc text-lg px-4 py-2 w-2/3"
                name="name"
                value={search}
                onChange={(e) => setSearch(e.target.value)}
              />
              <button className="py-3 px-4 title bg-black rounded-xl">
                Search
              </button>
              <button type="button" onClick={() => setFilters(!filters)}>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="w-8 h-8 text-black"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75"
                  />
                </svg>
              </button>
              {data && (
                <CsvDownloader
                  className="py-3 px-4 title bg-black rounded-xl"
                  datas={data}
                  text={"Export"}
                  filename={"export.csv"}
                />
              )}
            </div>
            {filters && (
              <div id="filters">
                <div className="col-lg-4 mx-auto space p-5 rounded shadow">
                  <ul class="flex flex-row space-x-2 ml-6 text-black">
                    <div className="text-base font-medium text-gray-900">
                      Age :
                    </div>
                    <li class="min-w-max ">
                      <div class="md:ml-2 flex items-center">
                        <input
                          checked-id="20-30"
                          name="ages[]"
                          value="20-30"
                          type="checkbox"
                          class="accent-lime-500 h-5 w-5 rounded-full shadow"
                        />
                        <label
                          for="20-30"
                          class="ml-2 text-base font-medium text-black"
                        >
                          20 - 30
                        </label>
                      </div>
                    </li>
                    <li class="min-w-max ">
                      <div class="md:ml-2 flex items-center">
                        <input
                          checked-id="30-40"
                          name="ages[]"
                          value="30-40"
                          type="checkbox"
                          class="accent-lime-500 h-5 w-5 rounded-full shadow"
                        />
                        <label
                          for="30-40"
                          class="ml-2 text-base font-medium text-gray-900 "
                        >
                          30 - 40
                        </label>
                      </div>
                    </li>
                    <li class="min-w-max ">
                      <div class="md:ml-2 flex items-center">
                        <input
                          checked-id="40-50"
                          name="ages[]"
                          value="40-50"
                          type="checkbox"
                          class="accent-lime-500 h-5 w-5 rounded-full shadow"
                        />
                        <label
                          for="40-50"
                          class="ml-2 text-base font-medium text-gray-900 "
                        >
                          40 - 50
                        </label>
                      </div>
                    </li>
                    <li class="min-w-max ">
                      <div class="md:ml-2 flex items-center">
                        <input
                          checked-id="50-60"
                          name="ages[]"
                          value="50-60"
                          type="checkbox"
                          class="accent-lime-500 h-5 w-5 rounded-full shadow"
                        />
                        <label
                          for="50-60"
                          class="ml-2 text-base font-medium text-gray-900 "
                        >
                          50 - 60
                        </label>
                      </div>
                    </li>
                    <li class="min-w-max ">
                      <div class="md:ml-2 flex items-center">
                        <input
                          checked-id="60-120"
                          name="ages[]"
                          value="60-120"
                          type="checkbox"
                          class="accent-lime-500 h-5 w-5 rounded-full shadow"
                        />
                        <label
                          for="60-120"
                          class="ml-2 text-base font-medium text-gray-900 "
                        >
                          60 and above
                        </label>
                      </div>
                    </li>
                  </ul>
                  <div className="flex flex-row mt-2">
                    <div className="mt-2 mr-3 ml-6 text-base font-medium text-gray-900">
                      Arrest Date :{" "}
                    </div>
                    <div className="mt-2">
                      <input
                        name="arrest_date"
                        type="date"
                        data-date-format="dd/mm/yyyy"
                        className="rounded"
                      />
                    </div>
                  </div>

                  <div className="mt-4">
                    <label
                      htmlFor="sel1"
                      className="mt-2 mr-3 ml-6 text-base font-medium text-gray-900"
                    >
                      Gender :{" "}
                    </label>
                    <select
                      name="gender"
                      className="form-control rounded"
                      id="sel1"
                    >
                      <option value="">Select Gender</option>
                      <option value="M">Male</option>
                      <option value="F">Female</option>
                      <option value="O">Other</option>
                    </select>
                  </div>
                  <div className="mt-4">
                    <label
                      htmlFor="sel1"
                      className="mt-2 mr-3 ml-6 text-base font-medium text-gray-900"
                    >
                      State :{" "}
                    </label>
                    <select
                      name="state"
                      className="form-control rounded"
                      id="sel1"
                    >
                      <option value="">Select State</option>
                      {states.map((state, k) => <option key={k} value={state}>{state}</option>)}
                    </select>
                  </div>
                </div>
                <div className="flex justify-end">
                  <button className="py-3 px-4 title bg-black rounded-xl mt-4">
                    Apply filters
                  </button>
                </div>
              </div>
            )}
          </form>
          {data && (
            <div id="cards" className="mt-10 mx-10">
              <div className="grid grid-cols-2">
                {data.map((p, index) => (
                  <div
                    key={index}
                    id="card"
                    className=" shadow-2xl bg-[#dfdfe520] backdrop-filter backdrop-blur-3xl  border-[#575555] rounded-lg m-2 p-4"
                    onClick={() => setCurrentP(p)}
                  >
                    <div className="flex justify-end">
                      <span class="whitespace-nowrap rounded-full bg-[#BDFF00] px-2.5 py-0.5 text-xs text-black text-end">
                        {p.type === "state"
                          ? "State portal"
                          : p.type === "icjs"
                          ? "ICJS portal"
                          : "Both portals"}
                      </span>
                    </div>
                    <div className="flex space-x-3">
                      <div className="space-y-2">
                        <div className="flex space-x-3">
                          <div className="desc text-gray-500 text-sm">Name</div>
                          <div className="desc text-gray-400 text-sm">
                            {p["Person_Name"]}
                          </div>
                        </div>
                        <div className="flex space-x-5">
                          <div className="flex space-x-3">
                            <div className="desc text-gray-500 text-sm">
                              Age
                            </div>
                            <div className="desc text-gray-400 text-sm">
                              {p["Age"]}
                            </div>
                          </div>
                          <div className="flex space-x-3">
                            <div className="desc text-gray-500 text-sm">
                              Arrested on
                            </div>
                            <div className="desc text-gray-400 text-sm">
                              {p["Arrest_Date"]}
                            </div>
                          </div>
                        </div>
                        <div className="flex space-x-3">
                          <div className="desc text-gray-500 text-sm">
                            Location
                          </div>
                          <div className="desc text-gray-400 text-sm">
                            {p["District_Name"]}, {p["State"]}
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
        <div className="w-1/4  h-screen">
          <div className="">
            {currentP ? (
              <div className="h-screen p-5 z-10 bg-[#1313158b] backdrop-filter backdrop-blur-3xl  border-[#575555]">
                <div className="flex justify-center"></div>
                {console.log(currentP)}
                <div className="flex justify-center mt-10">
                  <div className="bg-[#1A1A1D] w-60 rounded-xl p-3">
                    <h1 className="desc text-sm text-white opacity-30">Name</h1>
                    <h1 className="title mt-1 text-2xl text-[#BDFF00]">
                      {currentP["Person_Name"]}
                    </h1>
                  </div>
                </div>{" "}
                <div className="flex justify-center mt-10">
                  <div className="bg-[#1A1A1D] w-60 rounded-xl p-3">
                    <h1 className="desc text-sm text-white opacity-30">
                      Father's Name
                    </h1>
                    <h1 className="title mt-1 text-2xl text-[#BDFF00]">
                      {currentP["Father_Name"]}
                    </h1>
                  </div>
                </div>
                <div className="flex justify-center mt-10">
                  <div className="bg-[#1A1A1D] w-60 rounded-xl p-3">
                    <h1 className="desc text-sm text-white opacity-30">
                      Gender
                    </h1>
                    <h1 className="title mt-1 text-2xl text-[#BDFF00]">
                      {currentP["Gender"] === "M" ? "Male" : "Female"}
                    </h1>
                  </div>
                </div>
                <div className="flex justify-center mt-10">
                  <div className="bg-[#1A1A1D] w-60 rounded-xl p-3">
                    <h1 className="desc text-sm text-white opacity-30">
                      Person Number
                    </h1>
                    <h1 className="title mt-1 text-2xl text-[#BDFF00] overflow-ellipsis">
                      {currentP["Person_No"]}
                    </h1>
                  </div>
                </div>
                <div className="flex justify-center mt-10">
                  <div className="bg-[#1A1A1D] w-60 rounded-xl p-3">
                    <h1 className="desc text-sm text-white opacity-30">
                      FIR ID
                    </h1>
                    <h1 className="title mt-1 text-2xl text-[#BDFF00]">
                      {currentP["FIR_ID"]}
                    </h1>
                  </div>
                </div>
                <div className="flex justify-center mt-10">
                  <div className="bg-[#1A1A1D] w-60 rounded-xl p-3">
                    <h1 className="desc text-sm text-white opacity-30">
                      Crime Number
                    </h1>
                    <h1 className="title mt-1 text-2xl text-[#BDFF00] overflow-ellipsis">
                      {currentP["Crime_No"]}
                    </h1>
                  </div>
                </div>
              </div>
            ) : (
              <div></div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
