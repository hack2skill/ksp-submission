import { BsFillPersonFill } from "react-icons/bs";
import Head from "next/head";
import { useState } from "react";
import Table from "../components/Table";

const Home = () => {
  const [searchData, setSearchData] = useState({
    name: "CHANDAPPA",
    ageFrom: "20",
    ageTo: "30",
    database: {
      icjs: true,
      ksp: false,
    },
  });
  const [loader, setLoader] = useState(false);
  const [data, setData] = useState([]);
  const [kspData, setKspData] = useState([]);

  const getData = () => {
    setLoader(true);
    const fetchData = async () => {
      const res = await fetch("/api/fetchData", {
        method: "POST",
        body: JSON.stringify(searchData),
        headers: {
          "Content-Type": "application/json",
        },
      });
      const data = await res.json();
      setData(data);
      setLoader(false);
    };

    fetchData();
  };

  const getDataForKsp = () => {
    setLoader(true);
    const fetchData = async () => {
      const res = await fetch("/api/fetchKSP", {
        method: "POST",
        body: JSON.stringify(searchData),
        headers: {
          "Content-Type": "application/json",
        },
      });
      const data = await res.json();
      setKspData(data);
      setLoader(false);
    };

    fetchData();
  };

  return (
    <div className="">
      <Head>
        <title>Firebolts</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className="min-h-screen bg-gradient-to-r from-slate-200 to-zinc-100">
        <code>
          <pre>{JSON.stringify(searchData, null, 2)}</pre>
        </code>
        <div className="pt-5 space-y-3 px-10 md:w-[40%] mx-auto">
          <div className="flex items-center space-x-5">
            <p className="text-sm font-bold flex-1">Name:</p>
            <div className="px-4 w-full flex items-center py-2 border border-black rounded-md">
              <input
                onChange={(e) =>
                  setSearchData({ ...searchData, name: e.target.value })
                }
                value={searchData.name}
                className="outline-none bg-transparent w-full"
                type="text"
              />
              <BsFillPersonFill className="w-5 h-5" />
            </div>
          </div>
          <div className="space-x-5 flex items-center">
            <p className="text-sm font-bold flex-1">Father's Name:</p>
            <div className="px-4 w-full flex items-center py-2 border border-black rounded-md">
              <input
                onChange={(e) =>
                  setSearchData({ ...searchData, fatherName: e.target.value })
                }
                value={searchData.fatherName}
                className="outline-none bg-transparent w-full"
                type="text"
              />
              <BsFillPersonFill className="w-5 h-5" />
            </div>
          </div>
          <div className="flex space-x-5 items-center">
            <p className="text-sm font-bold flex-1">Age:</p>
            <div className="px-4 w-full flex items-center py-2 border border-black rounded-md">
              <input
                className="outline-none bg-transparent w-full"
                placeholder="From"
                onChange={(e) =>
                  setSearchData({ ...searchData, ageFrom: e.target.value })
                }
                value={searchData.ageFrom}
                type="text"
              />
            </div>
            <div className="px-4 w-full flex items-center py-2 border border-black rounded-md">
              <input
                onChange={(e) =>
                  setSearchData({ ...searchData, ageTo: e.target.value })
                }
                value={searchData.ageTo}
                className="outline-none bg-transparent w-full"
                placeholder="To"
                type="text"
              />
            </div>
          </div>
          <div className="space-x-5 flex items-center">
            <p className="text-sm font-bold flex-1">Gender</p>
            <div className="px-4 w-full flex items-center py-2 border border-black rounded-md">
              <select
                onChange={(e) =>
                  setSearchData({ ...searchData, gender: e.target.value })
                }
                className="outline-none font-normal text-sm text-gray-500 bg-transparent w-full"
              >
                <option value="E">Choose</option>
                <option value="M">Male</option>
                <option value="F">Female</option>
              </select>
              <BsFillPersonFill className="w-5 h-5" />
            </div>
          </div>
          <div className="flex space-x-3">
            <div className="flex space-x-1">
              <input
                onChange={(e) =>
                  setSearchData({
                    ...searchData,
                    database: {
                      ...searchData.database,
                      icjs: e.target.checked,
                    },
                  })
                }
                checked={searchData.database.icjs}
                type="checkbox"
                id="database-select"
              />
              <p>ICJS Database</p>
            </div>
            <div className="flex space-x-1">
              <input
                onChange={(e) =>
                  setSearchData({
                    ...searchData,
                    database: { ...searchData.database, ksp: e.target.checked },
                  })
                }
                checked={searchData.database.ksp}
                type="checkbox"
                id="database-select"
              />
              <p>Karnataka Database</p>
            </div>
          </div>
          <div className="flex space-x-5">
            <div className="cursor-pointer px-3 py-2 bg-blue-500 text-white rounded-md shadow-lg active:scale-95 ease-out duration-100">
              <label className="flex flex-col">
                <input
                  type="file"
                  placeholder="Upload Photo"
                  className="hidden w-full h-full"
                />
                Upload Photo
              </label>
            </div>
            <div className="cursor-pointer px-3 py-2 bg-green-500 text-white rounded-md shadow-lg active:scale-95 ease-out duration-100">
              <label className="flex flex-col">
                <input
                  type="file"
                  placeholder="Upload Photo"
                  className="hidden w-full h-full"
                />
                Upload Fingerprint
              </label>
            </div>
          </div>
          <button
            onClick={() => {
              getData();
              getDataForKsp();
            }}
            className="px-3 py-2 bg-red-500 text-white rounded-md shadow-lg active:scale-95 ease-out duration-100"
          >
            Search
          </button>
        </div>

        <Table
          database={searchData.database}
          loader={loader}
          data={data}
          kspData={kspData}
        />
      </main>
    </div>
  );
};

export default Home;
