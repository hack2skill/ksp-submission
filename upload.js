const path = require("path");
const multer = require("multer");

var storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, "uploads/user");
  },
  filename: function (req, file, cb) {
    cb(null, Date.now() + ".jpg");
  },
  limits: {
    fileSize: 1024 * 1024 * 5, // 5 MB
  },
});

var upload = multer({
  storage: storage,
  fileFilter: function (req, file, callback) {
    if (
      file.mimetype == "image/jpeg" ||
      file.mimetype == "image/jpg" ||
      file.mimetype == "image/png" ||
      file.mimetype == "image/gif"
    ) {
      callback(null, true);
    } else {
      console.log("only jpg and png supported");
      callback(null, false);
    }
  },
});

module.exports = upload;
