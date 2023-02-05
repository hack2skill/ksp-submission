import React from "react";
import { MagnifyingGlass } from "react-loader-spinner";

const Table = ({ data, loader, kspData, database }) => {
  return (
    <div className="mx-auto py-10 w-screen ">
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
        <>
          <div className="w-[90%] mx-auto overflow-x-scroll">
            {database.icjs && (
              <>
                {data && data.length > 0 && (
                  <table cellPadding={10} className="text-center">
                    <tbody>
                      {Object.keys(data[0])?.map((item, key) => {
                        return (
                          <td
                            className="border sticky top-0 border-black"
                            key={key}
                          >
                            {item.replace("_", " ")}
                          </td>
                        );
                      })}

                      {data.map((item, key) => {
                        return (
                          <tr key={key}>
                            {Object.keys(data[0]).map((value, index) => {
                              return (
                                <td
                                  className="border bg-green-500 text-white text-xs font-bold border-black"
                                  key={index}
                                >
                                  {item[value].slice(1, -1)}
                                </td>
                              );
                            })}
                          </tr>
                        );
                      })}
                    </tbody>
                  </table>
                )}
              </>
            )}
            {database.ksp && (
              <>
                {kspData && kspData.length > 0 && (
                  <table cellPadding={10} className="text-center mt-5">
                    {Object.keys(kspData[0])?.map((item, key) => {
                      if (key > 2)
                        return (
                          <td
                            className="border sticky top-0 border-black"
                            key={key}
                          >
                            {item.replace("_", " ")}
                          </td>
                        );
                    })}

                    {kspData.map((item, key) => {
                      return (
                        <tr key={key}>
                          {Object.keys(kspData[0]).map((key, index) => {
                            if (index > 2)
                              return (
                                <td
                                  className="border bg-red-500 text-white text-xs font-bold border-black"
                                  key={index}
                                >
                                  {item[key]}
                                </td>
                              );
                          })}
                        </tr>
                      );
                    })}
                  </table>
                )}
              </>
            )}
          </div>
        </>
      )}
    </div>
  );
};

export default Table;
