const { default: mongoose } = require("mongoose");
const moongose = require("mongoose");

const DBConnection = () => {
  const DB_URL = process.env.MONGO_URI;

  moongose.connect(DB_URL, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  });

  const db = mongoose.connection;

  db.on("error", console.error.bind(console, "Connection error: "));
  db.once("open", function () {
    console.log("DB Connected...");
  });
};
module.exports = DBConnection;
