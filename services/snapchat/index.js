'use strict'
let express = require("express")
let app = express();
app.use(express.json())
let snapAPI = require('./snap');

app.get("/snapsAtLocation",async (req,res)=>{

    let lat = req.query.lat;
    let long = req.query.long;
    let radius = req.query.radius ?? 200;
    console.log(lat,long)
    if(!lat || !long){
        res.status(400).send("'lat' and 'long' query param req")
        return;
    }
    try{
        let data = await snapAPI.getPlaylist(Number(lat),Number(long),radius,17.00)
        // console.log(data)
        res.status(200).send(data)
    }
    catch(err){
        // console.log(err)
        res.status(500).send(err)
    }
})

app.listen(3000,()=>{
    console.log("listening on 3000")
})