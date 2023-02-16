import Event from "../models/Events/Events.js";
import bigPromise from "../middlewares/bigPromise.js";
import fs from "fs";

export const newUpload = bigPromise(async (req, res, next) => {
  res.status(200).send({
    success: true,
    message: "Successfully Uploaded to folder",
  });
});

export const readata = bigPromise(async (req, res, next) => {
  let names = [];
  let data1 = [];

  try {
    const data = await fs.promises.readFile("test.txt", "utf-8");
    names = data.toString().split("\n").map((line) => line.trim());

    for (let i = 0; i < names.length; i++) {
      let a = await Event.findOne({ name: names[i] });
      if(a){
      data1.push(a);
      }
    }
  } catch (error) {
    return res.status(500).json({
      success: false,
      message: "Error reading file or querying database: " + error.message,
    });
  }

  return res.status(200).json({
    success: true,
    data: data1,
    message: "Successfully Sent the details",
  });
});

export const thiefupload =bigPromise(async(req,res)=>{
  res.status(200).send({
    success: true,
    message: "Successfully Uploaded to folder",
  });
})

export const details=bigPromise(async(req,res)=>{
       const {name,aadhar_no,contact_no,address}=req.body;
       const x=await Event.create({
              name,
              aadhar_no,
              contact_no,
              address
       })
      if(x)
      {
        return res.status(200).json({
          success:true,
          message:"Successfully sent details"
        });
      }
})