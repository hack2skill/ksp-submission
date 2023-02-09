import React from "react";

const Button = ({ label, style, handleevent }) => {
  return (
    <button
      className={`capitalize bg-[#2d0ff1] mt-[2.75rem] mb-[0.75rem] text-white font-[600] text-[1.125rem] leading-[1.25rem] py-[12px] px-[2rem] rounded-[10px] ${style}`}
      onClick={handleevent}
      >
      {label}
    </button>
  );
};

export default Button;
