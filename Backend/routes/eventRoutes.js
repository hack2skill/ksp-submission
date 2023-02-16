import express from "express"
import multer from "multer";
import {newUpload,readata,thiefupload,details} from "../controllers/eventController.js"
const router=express.Router();
const storage=multer.diskStorage({
    destination:(req,file,cb)=>{
        cb(null,"uploads");
    },
    filename:(req,file,cb)=>{
        cb(null,file.originalname);
    }
})
const storage1=multer.diskStorage({
    destination:(req,file,cb)=>{
        cb(null,"thief");
    },
    filename:(req,file,cb)=>{
        cb(null,file.originalname);
    }
})
const storage2=multer.diskStorage({
    destination:(req,file,cb)=>{
        cb(null,"augmentation");
    },
    filename:(req,file,cb)=>{
        cb(null,file.originalname);
    }
})
const upload=multer({storage:storage});
const upload1=multer({storage:storage1});
const upload2=multer({storage:storage2});
router.route("/image").post(upload.single("image"),newUpload);
router.route("/thief").post(upload1.single("image"),thiefupload);
router.route("/augment").post(upload2.single("image"),newUpload);
router.route("/readfile").get(readata);
router.route("/details").post(details);
export default router;