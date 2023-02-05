const mysql = require('mysql2')


var mysqlConnection = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "123321123qwe",
    database: "hackton",
    multipleStatements: true
})


mysqlConnection.connect((err) => {
    if (!err) {
        console.log("connected to Data-base");
    } else {
        console.log(err)
    }
})


module.exports = mysqlConnection;