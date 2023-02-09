import React from "react";
import main from "../images/kar_main_logo.png"
import bommai from "../images/Bommai.png"
import Araga from "../images/Araga.png"
import "./Navbar.css"
const Navbar = () => {
  return(
    <div className="h-[150px]  gap-[5rem] pt-[1rem] grid grid-cols-3 nav shadow-2xl" >
    <div className="col-span-1 justify-center flex">
    <img src={bommai} alt ="" className="h-[110px] mr-[6rem]"/> 
    </div>
    <div className="col-span-1 ml-[4rem] flex">
    <div className="flex">
    <div>
    <img src={main} alt ="" className="h-[110px] ml-[1rem]"/>    
    </div>
    <div className="ml-[1.5rem] mt-[1.5rem] text-left">
    <p className="font-semibold text-3xl">Karnataka State Police</p>
    <p className="pt-[0.4rem]">Government Of Karnataka</p>
    </div>
    </div>

    </div>
    <div className="col-span-1">
    <img src={Araga} alt ="" className="h-[110px] ml-[10rem]"/> 
    </div>  
    </div>
  )
};

export default Navbar;
