'use strict'
let express = require("express")
let app = express();
app.use(express.json())


app.get("/telegramUser/:username",async (req,res)=>{
    let username = req.params.username;

    let result = await require("./tele").getUsernameDetails(username);
    res.send(result);
})
app.listen(3000,()=>{
    console.log("listening on 3000")
})