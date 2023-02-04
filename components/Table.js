import React from "react";
import { MagnifyingGlass } from "react-loader-spinner";

const Table = ({ data, loader }) => {
  return (
    <div className="mx-auto mt-10 w-screen ">
      <p className="font-bold text-center text-5xl mb-10">Results</p>
      <div className="flex justify-center">
        {loader && (
          <MagnifyingGlass
            visible={true}
            height={100}
            width={100}
            ariaLabel="MagnifyingGlass-loading"
            wrapperStyle={{}}
            wrapperClass="MagnifyingGlass-wrapper"
            glassColor="#c0efff"
            color="#e15b64"
          />
        )}
      </div>

      {!loader && (
        <div className="w-[90%] mx-auto overflow-x-scroll border-2 border-black">
          <table cellPadding={10} className="text-center">
            {data &&
              data.length > 0 &&
              Object.keys(data[0])?.map((item, key) => {
                return (
                  <th className="border sticky top-0 border-black" key={key}>
                    {item.replace("_", " ")}
                  </th>
                );
              })}
            {data &&
              data.length > 0 &&
              data.map((item, key) => {
                return (
                  <tr key={key}>
                    {Object.keys(item).map((key, index) => {
                      return (
                        <td
                          className="border bg-green-500 text-white text-xs font-bold border-black"
                          key={index}
                        >
                          {item[key].slice(1, -1)}
                        </td>
                      );
                    })}
                  </tr>
                );
              })}
          </table>
        </div>
      )}
    </div>
  );
};

export default Table;
