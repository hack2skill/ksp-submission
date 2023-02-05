import Head from "next/head";
import Image from "next/image";
import styles from "../styles/Home.module.css";
import { kph } from "../assets/kph2.png";

export default function Home() {
  return (
    <div className="w-full h-screen bg-[#101012]">
      <section class="hero-gradienty">
        <div class="mx-auto max-w-screen-xl px-4 py-32 lg:flex lg:h-screen lg:items-center">
          <div class="mx-auto  text-center">
            <span class="inline-flex items-center justify-center rounded-full bg-[#bbff005b] desc px-2.5 py-0.5 text-black">
              <p class="text-sm whitespace-nowrap">
                {" "}
                Built at Karnataka Police Hackathon
              </p>

              <button class="-mr-1 ml-1.5 inline-block rounded-full bg-[#BDFF00] p-0.5 text-black transition ">
                <span class="sr-only">Built</span>

                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="w-4 h-4"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"
                  />
                </svg>
              </button>
            </span>

            <h1 class="text-7xl mt-6 title">
              Unified data portal
              <strong class=" text-[#BDFF00] sm:block">
                for united policing
              </strong>
            </h1>

            <p class="mt-10 text-md sm:leading-relaxed desc opacity-50">
              An all in one portal for effective data based policing
            </p>

            <div class="mt-20 flex flex-wrap justify-center gap-4">
              <a
                class="block w-full rounded bg-[#BDFF00] px-12 py-3 text-sm font-medium text-black title shadow hover:bg-[#BDFF00] focus:outline-none focus:ring active:bg-[#BDFF00] sm:w-auto"
                href="/dashboard"
              >
                Get Started
              </a>

              {/*<a*/}
              {/*  class="block w-full rounded px-12 py-3 desc text-sm font-medium text-[#BDFF00] shadow hover:text-[#BDFF00] focus:outline-none focus:ring active:text-[#BDFF00] sm:w-auto"*/}
              {/*  href="/about"*/}
              {/*>*/}
              {/*  API Documentation*/}
              {/*</a>*/}
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
