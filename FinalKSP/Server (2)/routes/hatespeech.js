const express = require("express");
const router = express.Router();
var fetchuser = require("./middleware/fetchuser");
require("@tensorflow/tfjs");
const toxicity = require("@tensorflow-models/toxicity");

router.post("/detect_hate_speech", fetchuser, async (req, res) => {
  try {
    const { words } = req.body;
    //minimum prediction level
    const threshold = 0.9;

    toxicity.load(threshold).then((model) => {
      const sentences = words;

      model.classify(sentences).then((predictions) => {
        res.send(predictions);
      });
    });
  } catch (error) {
    console.error(error.message);
    res.status(500).send("Internal server error occoured");
  }
});

module.exports = router;
