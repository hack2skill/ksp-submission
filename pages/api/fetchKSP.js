import mongoose from "mongoose";
import KSP from "../../modals/KSPModal";

mongoose.connect(
  "mongodb+srv://lolbhai:lolbhai@oneclick.le7cuhb.mongodb.net/police?retryWrites=true&w=majority"
);

export default async function handler(req, res) {
  var modal = await KSP.find();

  let filteredData;

  filteredData = modal.filter((data) => {
    return data.Person_Name?.toLowerCase().includes(
      req.body.name?.toLowerCase()
    );
  });

  if (req.body.fatherName) {
    filteredData = filteredData.filter((data) => {
      return data.Father_Name?.toLowerCase().includes(
        req.body.fatherName?.toLowerCase()
      );
    });
  }
  if (req.body.ageFrom && req.body.ageTo) {
    filteredData = filteredData.filter((data) => {
      return (
        parseInt(data.Age.replace('"', "")) >= req.body.ageFrom &&
        parseInt(data.Age.replace('"', "")) <= req.body.ageTo
      );
    });
  }

  if (req.body.gender) {
    filteredData = filteredData.filter((data) =>
      data.Gender?.toLowerCase().includes(req.body.gender?.toLowerCase())
    );
  }

  return res.status(200).json(filteredData);
}
