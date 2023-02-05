const { Long } = require("bson");
const mongoose = require("mongoose");

const productSchema = new mongoose.Schema({
  State: String,
  District_Name: String,
  PS_Name: String,
  FIRNo: String,
  FIR_Date: Date,

  Person_No: String,

  Arrest_Date: Date,

  Person_Name: String,

  Father_Name: String,

  Gender: String,

  AgeWhileOpening: Number,

  Age: Number,

  Pres_Address1: String,

  Perm_Address1: String,

  PersonStatus: String,

  Name: String,

  Major_Head: String,

  Minor_Head: String,
  Crime_No: Number,

  Arr_ID: Number,

  Unit_ID: Number,

  FIR_ID: String,

  DEDT: String,
});

const Product = mongoose.model("Product", productSchema);

module.exports = Product;
