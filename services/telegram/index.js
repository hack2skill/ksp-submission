"use strict";
let express = require("express");
let app = express();

// Do `$npm install cors` in this folder
var cors = require("cors"); //Add this
app.use(cors()); //Add this

app.use(express.json());

app.get("/telegramUser/:username", async (req, res) => {
  let username = req.params.username;

  let result = await require("./tele").getUsernameDetails(username);
  res.send(result);
});
app.listen(5002, () => {
  console.log("Telegram running on 5002");
});
