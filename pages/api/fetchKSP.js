import mongoose from "mongoose";
import KSP from "../../modals/KSPModal";
// mongoose.set("strictQuery", false);

// mongoose.connect(process.env.mongo_url);
export default async function handler(req, res) {
  var modal = await KSP.find();

  let filteredData;

  filteredData = modal.filter((data) => {
    return data._doc.Person_Name?.toLowerCase().includes(
      req.body.name?.toLowerCase()
    );
  });

  if (req.body.fatherName) {
    filteredData = filteredData.filter((data) => {
      return data._doc.Father_Name?.toLowerCase().includes(
        req.body.fatherName?.toLowerCase()
      );
    });
  }
  if (req.body.ageFrom && req.body.ageTo) {
    filteredData = filteredData.filter((data) => {
      return (
        parseInt(data._doc.Age.replace('"', "")) >= req.body.ageFrom &&
        parseInt(data._doc.Age.replace('"', "")) <= req.body.ageTo
      );
    });
  }

  if (req.body.gender) {
    filteredData = filteredData.filter((data) =>
      data._doc.Gender?.toLowerCase().includes(req.body.gender?.toLowerCase())
    );
  }

  if (filteredData.length === 0)
    return res.status(200).json({ message: "No Data Found" });
  return res.status(200).json(filteredData);
}
