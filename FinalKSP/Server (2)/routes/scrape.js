const express = require("express");
const truecallerjs = require("truecallerjs");
const router = express.Router();
var fetchuser = require("./middleware/fetchuser");
const axios = require('axios');

const replacerFunc = () => {
  const visited = new WeakSet();
  return (key, value) => {
    if (typeof value === "object" && value !== null) {
      if (visited.has(value)) {
        return;
      }
      visited.add(value);
    }
    return value;
  };
};

router.post("/phone", fetchuser, async (req, res) => {
  try {
    const { number } = req.body;

    var countryCode = "IN";
    var installationId =
      "a1i0e--dT0TGqVy-56TddPFyZXFgo5ZD6mXrYZ2s52HSmOxx3E94-TZ-w6g0cKob";
    var phoneNumbers = number; 

    const searchResult = truecallerjs.bulkSearch(
      phoneNumbers,
      countryCode,
      installationId
    );
    searchResult.then(function (response) {
      const data = JSON.stringify(response, null, 2);
      res.send(data)
    });
  } catch (error) {
    console.error(error.message);
    res.status(500).send("Internal server error occoured");
  }
});

router.get("/instagram", fetchuser, async (req, res) => {
  try {
  const {username} = req.body;
  const data = await axios.get(`https://www.instagram.com/${username}/?__a=1&__d=dis`);
  const str = JSON.stringify(data, replacerFunc());
   res.send(str);
  } catch (error) {
    console.error(error.message);
    res.send({"status":500});
  }
});

module.exports = router;
