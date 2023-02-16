import React from "react";
import ClipLoader from "react-spinners/ClipLoader";

function Loader() {
  return (
    <div className="z-[100] fixed h-[100vh] w-[100vw] flex items-center justify-center">
      <p className="text-4xl pr-[2rem]">Image is Being Uploaded...</p>
      <ClipLoader
  color="black"
  size={80}
/>
    </div>
  );
}

export default Loader;
