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
connectAndQuery();

async function connectAndQuery() {
  try {
    var poolConnection = await sql.connect(config);

    console.log("Reading rows from the Table...");
    var resultSet = await poolConnection.request().query(`SELECT * FROM icjs`);

    console.log(`${resultSet.recordset.length} rows returned.`);

    var columns = "";
    for (var column in resultSet.recordset.columns) {
      columns += column + ", ";
    }
    console.log("%s\t", columns.substring(0, columns.length - 2));

    resultSet.recordset.forEach((row) => {
      console.log("%s\t%s", row.CategoryName, row.ProductName);
    });

    poolConnection.close();
  } catch (err) {
    console.error(err.message);
  }
}
