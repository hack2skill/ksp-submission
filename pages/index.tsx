import type { NextPage } from "next";
import { AiOutlineSearch } from "react-icons/ai";
import { BsFillPersonFill } from "react-icons/bs";
import Head from "next/head";

const Home: NextPage = () => {
  return (
    <div className="">
      <Head>
        <title>Firebolts</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className="min-h-screen bg-gradient-to-r from-slate-200 to-zinc-100">
        <div className="pt-5 space-y-3 w-[40%] mx-auto">
          <div className="flex items-center space-x-5">
            <p className="text-sm font-bold flex-1">Name:</p>
            <div className="px-4 w-full flex items-center py-2 border border-black rounded-md">
              <input
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
                type="number"
              />
            </div>
            <div className="px-4 w-full flex items-center py-2 border border-black rounded-md">
              <input
                className="outline-none bg-transparent w-full"
                placeholder="To"
                type="number"
              />
            </div>
          </div>
          <div className="space-x-5 flex items-center">
            <p className="text-sm font-bold flex-1">Gender</p>
            <div className="px-4 w-full flex items-center py-2 border border-black rounded-md">
              <select className="outline-none font-normal text-sm text-gray-500 bg-transparent w-full">
                <option value="E">Choose</option>
                <option value="M">Male</option>
                <option value="F">Female</option>
              </select>
              <BsFillPersonFill className="w-5 h-5" />
            </div>
          </div>
          <div className="flex space-x-5">
            <div className="px-3 py-2 bg-blue-500 text-white rounded-md shadow-lg active:scale-95 ease-out duration-100">
              <label className="flex flex-col">
                <input
                  type="file"
                  placeholder="Upload Photo"
                  className="hidden w-full h-full"
                />
                Upload Photo
              </label>
            </div>
            <div className="px-3 py-2 bg-green-500 text-white rounded-md shadow-lg active:scale-95 ease-out duration-100">
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
          <button className="px-3 py-2 bg-red-500 text-white rounded-md shadow-lg active:scale-95 ease-out duration-100">
            Search
          </button>
        </div>
      </main>
    </div>
  );
};

export default Home;
