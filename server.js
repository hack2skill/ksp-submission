const express = require("express");
const model = require("./model");
const multer = require("multer");
const dotenv = require("dotenv");
const bodyParser = require("body-parser");
const DBConnection = require("./DBconnection");
const upload = require("./upload");
const Binary = require("mongodb").Binary;
const { spawn } = require("child_process");
const path = require("path");
const fs = require("fs");
const xlsx = require("xlsx");
const { json } = require("express/lib/response");

// const output = require("./data.json");
const port = 8000;
dotenv.config();
const app = express();
DBConnection();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

//multer code
var storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, "uploads/user");
  },
  filename: function (req, file, cb) {
    cb(null, file.originalname);
  },
});

const upload_user = multer({ storage });

//code for data connection with python
const python_run = (data) => {
  const python = spawn("python", ["ml-model/siamese_network.py", data]);
  console.log("Data send to pyhton");
  python.stdout.on("data", (data) => {
    console.log(`${data}`);
  });
  python.stderr.on("data", (data) => {
    console.error(`error: ${data}`);
  });
  python.on("close", (data) => {
    console.log(`Child Process exited with code: ${data}`);
  });
};

//Routes for all static files
app.use("/uploads", express.static("uploads"));

//Sending frontend
app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});
app.get("/style", (req, res) => {
  res.sendFile(__dirname + "/styles.css");
});
app.get("/js", (req, res) => {
  res.sendFile(__dirname + "/index.js");
});

//getting image uploaded by user
//use upload_user for having same name as img file
app.post("/", upload.single("image"), (req, res) => {
  res.json({ imageURL: `/uploads/user/${req.file.filename}` });
  python_run(req.file.filename);
  output.forEach(function (object) {
    console.log(object.key);
  });
});

//to add data in database automatically with excel file
// just copy path of xlfile in readfile and make empty post request in person

app.post("/person", async (req, res) => {
  try {
    //reading xl file
    const xlfile = xlsx.readFile(
      "C:\\Users\\Adm\\Desktop\\Sample Missing Persons FIRS.xlsx"
    );
    //extracting data in sheet
    const sheet = xlfile.Sheets[xlfile.SheetNames[0]];
    //converting sheet into json
    const data = xlsx.utils.sheet_to_json(sheet);

    //adding data to mongodb
    await model.insertMany(data).then((result) => {
      if (result.length > 0) {
        res.send({ status: 200, message: "success", count: result.length });
      } else {
        res.send(new ErrResponse(201, "failed"));
      }
    });
  } catch (error) {
    res.send(new ErrResponse(error));
  }
});

//to show  person

app.get("/find", async (req, res) => {
  //for checking
  const allperson = await model.find({});
  if (allperson.length === 0) {
    return res.status(404).json({
      message: "No person present",
    });
  }

  return res.status(200).json({
    data: allperson,
  });
});

app.listen(port, () => {
  console.log(`Running on port ${port}`);
});
