import React from "react";
import Navbar from "../../Components/Navbar";
import axios from "axios";
import {ROUTES} from "../../routes/Routerconfig"
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
function LostOutput() {
  const navigate=useNavigate();
  var images = [];
  const importAll = (r) => {
    return r.keys().reduce((acc, key) => {
      acc.push({ name: key.split("/").pop().split(".")[0], url: r(key) });
      return acc;
    }, []);
  };

  const [details, setDetails] = useState([]);
  const shreyas = async() => {
   await axios
      .get("http://localhost:1999/api/upload/readfile")
      .then((res) => {
        console.log(res.data.data);
        setDetails(res.data.data);
        console.log(details);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  useEffect(() => {
    shreyas();
  }, []);

  images = importAll(
    require.context(
      "../../Components/imagesThief/",
      false,
      /\.(png|jpe?g|jpg|svg)$/
    )
  );

  const xyz = () =>{
    navigate(ROUTES.Dashboard);
  }
  return (
    <div>
      <Navbar />
      <p className="text-[4rem] pt-[2rem] text-red-600">
        Output Images With Names
      </p>
      <button type="button" onClick={xyz} class="ml-[98rem] px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded-full shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out justify-end">Dashboard</button>
      <div className=" grid grid-cols-3">
        {images
          ? images.map((image, index) => {
              return (
                <div className="grid-cols-3">
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
          : null}
          
          {
           (details && images.length!=0) ? details.map((item,key)=>{
            return(
              <div>
              <h1 className="flex text-3xl justify-center ml-[63rem] ">Details</h1>
              <p className="text-2xl mt-[5rem]">Name- {item?.name}</p>
              <p className="text-2xl">Contact No - {item?.contact_no}</p>
              <p className="text-2xl">Aadhar Card Number - {item?.aadhar_no}</p>
              <p className="text-2xl">Address - {item?.address}</p>
              </div>
              );
           }):null
          }
      </div>
    </div>
  );
}

export default LostOutput;
