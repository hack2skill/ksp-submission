import Image from "next/image";
import React from "react";

const Navbar = () => {
  return (
    <header className="py-3 w-full  border-b">
      <div className="w-2/3 mx-auto flex items-center justify-between">
        <Image
          className="cursor-pointer w-20 h-20 rounded-full hover:shadow-lg ease-out duration-100 active:scale-95"
          src={require("../images/ksp-logo.png")}
        />
        <p className="font-bold flex flex-col border rounded-lg hover:tracking-wider cursor-pointer px-4 py-2 hover:shadow-sm">
          <span>Chanakyha Vetri</span>{" "}
          <span className="font-medium text-xs">Karnataka</span>
        </p>
      </div>
    </header>
  );
  x;
};

export default Navbar;
