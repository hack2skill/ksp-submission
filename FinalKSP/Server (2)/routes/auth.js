const express = require("express");
const router = express.Router();
const User = require("../models/User");
const { body, validationResult } = require("express-validator"); 
const bcrypt = require("bcryptjs");
var jwt = require("jsonwebtoken");
const JWT_SECRET = "CHOLEBHATOORE@69";
var fetchuser = require("./middleware/fetchuser");

//Route 1 : Create a user using: POST "api/auth/createUser".
router.post(
  "/createUser",
  [
    body("name", "Enter a valid name atleast 3 letters").isLength({ min: 3 }),
    body("email", "Enter valid email").isEmail(),
    body("password", "Enter atleast 8 letters long password").isLength({
      min: 8,
    }),
  ],
  async (req, res) => {

    let success = false;

    //check for errors(express validator)
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    //Check whether a user with that email exists already
    try {
      let user = await User.findOne({ email: req.body.email });
      if (user) {
        return res
          .status(400)
          .json({
            success,
            error: "sorry a user with this email already exists",
          });
      }
      
      const salt = await bcrypt.genSalt(10);
      const securePassword = await bcrypt.hash(req.body.password, salt);

      user = await User.create({
        name: req.body.name,
        email: req.body.email,
        password: securePassword,
      });
      const data = {
        user: {
          id: user.id,
        },
      };
      const authToken = jwt.sign(data, JWT_SECRET);
      success = true;
      res.json({ success, authToken });
    } catch (error) {
      console.error(error.message);
      res.status(500).send("some error happened");
    }
  }
);

// Route 2 : Authenticate a User "/api/auth/login". 
router.post(
  "/login",
  [
    body("email", "Enter valid email").isEmail(),
    body("password", "password cannot be blank").exists(),
  ],
  async (req, res) => {
    let success = false;

    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    const { email, password } = req.body;
    try {
      let user = await User.findOne({ email });
      if (!user) {
        return res
          .status(400)
          .json({ error: "Please login with correct details" });
      }
      const passwordCompare = await bcrypt.compare(password, user.password);
      if (!passwordCompare) {
        success = false;
        return res
          .status(400)
          .json({ success, error: "Please login with correct details" });
      }
      const data = {
        user: {
          id: user.id,
        },
      };
      const authToken = jwt.sign(data, JWT_SECRET);
      success = true;
      res.json({ success, authToken });
    } catch (error) {
      console.error(error.message);
      res.status(500).send("Internal server error occoured");
    }
  }
);


module.exports = router;
