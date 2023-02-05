import React, { useState } from "react";
import Face from "../components/dashboard/Face";
import Fingerprint from "../components/dashboard/Fingerprint";
import Search from "../components/dashboard/Search";
import Stats from "../components/dashboard/Stats";


export default function dashboard() {
  const [menu, setMenu] = useState(1);
  return (
    <div className="w-full h-full bg-[#101012]">
      <section class="hero-gradienty h-full flex">
        <div className="bottom-0 left-0 fixed">
          <div class="flex h-screen w-16 flex-col justify-between z-10 bg-[#1a1a1d] backdrop-filter backdrop-blur-3xl  border-[#575555]">
            <div class="inline-flex h-16 w-16 items-center justify-center">
              <span class="block h-10 w-10 rounded-lg bg-[#BDFF00]">
              <img class="w-10 h-10" src="/assets/logo.png" alt="hello"/>
              </span>
            </div>
            <div>
              <div class="">
                <nav
                  aria-label="Main Nav"
                  class="flex flex-col p-2 items-center"
                >
                  <ul class="space-y-10 pt-4">
                    <li>
                      <button
                        onClick={() => setMenu(1)}
                        class={
                          menu == 1
                            ? "group relative flex justify-center rounded-full px-2 py-1.5 text-gray-500 shadow-xl shadow-[#bbff0076]"
                            : "group relative flex justify-center rounded-full px-2 py-1.5 text-gray-500 shadow-xl"
                        }
                      >
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke-width="1.5"
                          stroke="currentColor"
                          class="w-6 h-6"
                        >
                          <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"
                          />
                        </svg>

                        <span class="absolute left-full top-1/2 ml-4 -translate-y-1/2 rounded bg-gray-900 px-2 py-1.5 text-xs font-medium text-white opacity-0 group-hover:opacity-100">
                          Search
                        </span>
                      </button>
                    </li>

                    <li>
                      <button
                        onClick={() => setMenu(2)}
                        class={
                          menu == 2
                            ? "group relative flex justify-center rounded-full px-2 py-1.5 text-gray-500 shadow-xl shadow-[#bbff0076]"
                            : "group relative flex justify-center rounded-full px-2 py-1.5 text-gray-500 shadow-xl"
                        }
                      >
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke-width="1.5"
                          stroke="currentColor"
                          class="w-6 h-6"
                        >
                          <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 013 19.875v-6.75zM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V8.625zM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V4.125z"
                          />
                        </svg>

                        <span class="absolute left-full top-1/2 ml-4 -translate-y-1/2 rounded bg-gray-900 px-2 py-1.5 text-xs font-medium text-white opacity-0 group-hover:opacity-100">
                          Statistics
                        </span>
                      </button>
                    </li>

                    <li>
                      <button
                        onClick={() => setMenu(3)}
                        class={
                          menu == 3
                            ? "group relative flex justify-center rounded-full px-2 py-1.5 text-gray-500 shadow-xl shadow-[#bbff0076]"
                            : "group relative flex justify-center rounded-full px-2 py-1.5 text-gray-500 shadow-xl"
                        }
                      >
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke-width="1.5"
                          stroke="currentColor"
                          class="w-6 h-6"
                        >
                          <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M7.864 4.243A7.5 7.5 0 0119.5 10.5c0 2.92-.556 5.709-1.568 8.268M5.742 6.364A7.465 7.465 0 004.5 10.5a7.464 7.464 0 01-1.15 3.993m1.989 3.559A11.209 11.209 0 008.25 10.5a3.75 3.75 0 117.5 0c0 .527-.021 1.049-.064 1.565M12 10.5a14.94 14.94 0 01-3.6 9.75m6.633-4.596a18.666 18.666 0 01-2.485 5.33"
                          />
                        </svg>

                        <span class="absolute left-full top-1/2 ml-4 -translate-y-1/2 rounded bg-gray-900 px-2 py-1.5 text-xs font-medium text-white opacity-0 group-hover:opacity-100">
                          Fingerprint
                        </span>
                      </button>
                    </li>

                    <li>
                      <button
                        onClick={() => setMenu(4)}
                        class={
                          menu == 4
                            ? "group relative flex justify-center rounded-full px-2 py-1.5 text-gray-500 shadow-xl shadow-[#bbff0076]"
                            : "group relative flex justify-center rounded-full px-2 py-1.5 text-gray-500 shadow-xl"
                        }
                      >
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke-width="1.5"
                          stroke="currentColor"
                          class="w-6 h-6"
                        >
                          <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z"
                          />
                        </svg>

                        <span class="absolute left-full top-1/2 ml-4 -translate-y-1/2 rounded bg-gray-900 px-2 py-1.5 text-xs font-medium text-white opacity-0 group-hover:opacity-100">
                          Face recognition
                        </span>
                      </button>
                    </li>
                  </ul>
                </nav>
              </div>
            </div>

            <div class="sticky inset-x-0 bottom-0  bg-[#BDFF00] p-2">
              <form action="/logout">
                <button
                  type="submit"
                  class="group relative flex w-full justify-center rounded-lg px-2 py-1.5 text-sm text-black hover:bg-gray-50 hover:text-gray-700"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 opacity-75"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    stroke-width="2"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
                    />
                  </svg>

                  <span class="absolute left-full top-1/2 ml-4 -translate-y-1/2 rounded bg-gray-900 px-2 py-1.5 text-xs font-medium text-white opacity-0 group-hover:opacity-100">
                    Logout
                  </span>
                </button>
              </form>
            </div>
          </div>
        </div>
        {menu === 1 && <Search />}
        {menu === 2 && <Stats />}
        {menu === 3 && <Fingerprint />}
        {menu === 4 && <Face />}
      </section>
    </div>
  );
}
