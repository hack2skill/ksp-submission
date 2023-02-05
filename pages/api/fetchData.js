import sql from "mssql";

const config = {
  user: process.env.username,
  password: process.env.password,
  server: process.env.server,
  port: 1433,
  database: process.env.database,
  authentication: {
    type: "default",
  },
  options: {
    encrypt: true,
  },
};

console.log("Starting...");

export default async function handler(req, res) {
  try {
    var poolConnection = await sql.connect(config);

    console.log("Reading rows from the Table...");
    var resultSet = await poolConnection.request().query(`SELECT * FROM icjs`);

    res.status(200).json(searchData(resultSet.recordset, req.body));
    poolConnection.close();
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
}

const searchData = (JSONfile, searchData) => {
  let filteredData = [];
  filteredData = JSONfile.filter((data) =>
    data.Person_Name?.toLowerCase().includes(searchData.name?.toLowerCase())
  );

  if (searchData.fatherName) {
    filteredData = filteredData.filter((data) =>
      data.Father_Name?.toLowerCase().includes(
        searchData.fatherName?.toLowerCase()
      )
    );
  }
  if (searchData.ageFrom && searchData.ageTo) {
    filteredData = filteredData.filter((data) => {
      return (
        parseInt(data.Age.replace('"', "")) >= searchData.ageFrom &&
        parseInt(data.Age.replace('"', "")) <= searchData.ageTo
      );
    });
  }

  if (searchData.gender) {
    filteredData = filteredData.filter((data) =>
      data.Gender?.toLowerCase().includes(searchData.gender?.toLowerCase())
    );
  }

  if (filteredData.length === 0)
    return res.status(200).json({ message: "No Data Found" });

  return filteredData;
};
