const mongoose = require("mongoose");
const mongoURI = "mongodb+srv://cholebhatoore:cholebhatoore@cluster0.axfumqh.mongodb.net/test";

const connectToMongo = () => {
  mongoose.connect(mongoURI, () => {
    console.log("CholeBhatoore connected to Mongo Successfully");
  });
};

module.exports = connectToMongo;
