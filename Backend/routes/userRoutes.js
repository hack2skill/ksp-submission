import express from "express"
const router = express.Router()

// import controllers
import {createUser,getUser,updateUserdetails,updatePassword,Deleteuser,login} from "../controllers/userController.js"

router.route("/createUser").post(createUser)
router.route("/login").post(login);
router.route("/getUser").get(getUser);
router.route("/updateUserdetails/:id").put(updateUserdetails);
router.route("/updatePassword/:id").put(updatePassword);
router.route("/deleteUser/:id").delete(Deleteuser);
export default router;