import express, { application }  from "express"
import  dotenv  from "dotenv"
import bodyParser from 'body-parser'
import connectDB from "./config/db.js"
import cors from 'cors'
dotenv.config();
const app=express()
app.use(cors());
import cookieParser from "cookie-parser"

//cookies and filemiddleware
app.use(cookieParser())

// morgan middlewares
import morgan from "morgan"
app.use(morgan("tiny"))
app.use(bodyParser.raw({ type: 'application/octet-stream' }));

// regular middlewares
app.use(express.json())
app.use(express.urlencoded({extended:true}));

app.use(bodyParser.json());
app.use(express.static('public')); 
app.use('/images', express.static('images'));
app.use(bodyParser.urlencoded());
// import all routes here
import userRoutes from "./routes/userRoutes.js"
import eventRoutes from "./routes/eventRoutes.js"
// router middleware
app.use("/api/user",userRoutes);
app.use("/api/upload",eventRoutes);
export default app;