"use strict";
let express = require("express");
let app = express();

// Do `$npm install cors` in this folder
var cors = require("cors"); //Add this
app.use(cors()); //Add this

app.use(express.json());
let snapAPI = require("./snap");

app.get("/snapsAtLocation", async (req, res) => {
  let lat = req.query.lat;
  let long = req.query.long;
  let radius = req.query.radius ?? 200;
  console.log(lat, long);
  if (!lat || !long) {
    res.status(400).send("'lat' and 'long' query param req");
    return;
  }
  try {
    let data = await snapAPI.getPlaylist(
      Number(lat),
      Number(long),
      radius,
      17.0
    );
    // console.log(data)
    res.status(200).send(data);
  } catch (err) {
    // console.log(err)
    res.status(500).send(err);
  }
});

app.listen(5001, () => {
  console.log("Snapchat SErvice listening on 5001");
});
