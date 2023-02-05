const mongoose = require("mongoose");

const Schema = mongoose.Schema;

const personschema = new Schema(
  {
    District_Name: { type: String },
    UnitName: { type: String },
    FIRNo: { type: String },
    RI: { type: String },
    Year: { type: String },
    Month: { type: String },
    Offence_From_Date: { type: String },
    Offence_To_Date: { type: String },
    FIR_Date: { type: String },
    FIR_Type: { type: String },
    FIR_Stage: { type: String },
    CrimeGroup_Name: { type: String },
    CrimeHead_Name: { type: String },
    Photo_Full_front: { type: String },
    Gender: { type: String },
    Person_Name: { type: String },
    age: { type: String },
    Months: { type: String },
    Days: { type: String },
    image: { type: Buffer },
  },
  {
    timestamps: true,
  }
);

module.exports = mongoose.model("person", personschema);
