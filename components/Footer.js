import Image from "next/image";
import React from "react";

const Footer = () => {
  return (
    <footer className="flex h-24 w-full items-center justify-center border-t">
      <a className="flex items-center justify-center gap-2">
        Made with 🖤 by
        <span className="font-bold">Firebolts</span> for Police Hackathon
      </a>
    </footer>
  );
};

export default Footer;
