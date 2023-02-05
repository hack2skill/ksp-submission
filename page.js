const express = require("express");
const app = express();
const path = require("path");
const mongoose = require("mongoose");

const Product = require("./details/schema");
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");
mongoose
  .connect("mongodb://127.0.0.1:27017/police_hack", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => {
    console.log("MONGO CONNECTION OPEN!!");
  })
  .catch((err) => {
    console.log("no error!!");
    console.log(err);
  });

app.get("/detail/:id", async (req, res) => {
  // res.send("woof!");
  const id = req.params["id"];
  const product = await Product.findOne({ FIR_ID: id });
  console.log("product", product);
  res.render("info", { product }); //.ejs file in views
});

app.listen(3000, () => {
  console.log("APP IS LISTENING ON PORT 3000!");
});
