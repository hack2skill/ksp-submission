import mongoose from "mongoose";
import KSP from "../../modals/KSPModal";
mongoose.set("strictQuery", false);

mongoose.connect(process.env.mongo_url, () => {
  console.log("connected to mongo");
});
export default async function handler(req, res) {
  var modal = await KSP.find();
  console.log(modal);

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

  return res.status(200).json(filteredData);
}
