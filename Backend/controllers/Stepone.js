const axios = require("axios");
const mysqlConnection = require('../database/Sqlconnect')


class Stepone {
    async search(req, res) {
        const { url } = req.body;
        axios.get(url)
            .then(response => {
                console.log(response.data);
                res.send(response.data.unsafe)
            })
            .catch(error => {
                console.error(error);
            });
    }

    async store(req, res) {
        const{email,nameofapp,whereufound,whatisitrealted,scamrelated} = req.body
        var quearylist = `INSERT INTO review (email,nameofapp,whereufound,whatisitrealted,scamrelated)VALUES ("${email}","${nameofapp}","${whereufound}","${whatisitrealted}","${scamrelated}");`
        const quearylist1 = `select * from review where nameofapp = "${nameofapp}";`
        console.log(quearylist)
        try {
            mysqlConnection.query(quearylist1, function (err, results, rows) {
                if (!err) {
                        mysqlConnection.query(quearylist, (err, rows) => {
                            if (!err) {
                                res.status(200).send(rows);
                            } else {
                                res.status(502).send("Db error");
                            }
                        })
                } else {
                    res.status(502).send("Db error");
                    console.log(err)
                    console.log(results)
                }
            });
        } catch (error) {
            console.log(error)
        }
    }

    async que(req, res) {
        const quearylist1 = `select * from review;`
        try {
            mysqlConnection.query(quearylist1, function (err, results, rows) {
                if (!err) {
                    // console.log(results)
                    res.status(200).send(results);
                } else {
                    res.status(502).send("Db error");
                    console.log(err)
                    console.log(results)
                }
            });
        } catch (error) {
            console.log(error)
        }
    }
}

module.exports = new Stepone();



