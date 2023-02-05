const mongoose=require('mongoose')
const dotenv=require('dotenv').config()
const dbLink='mongodb+srv://tanishkaDb:Ze3wXDNXDvEBsD3q@cluster0.g2jxbm3.mongodb.net/?retryWrites=true&w=majority'
// const dbLink='mongodb://localhost:27017'

const conn=mongoose.connect(dbLink,{
    autoIndex:true,
    dbName: 'missingPersonDatabase'
})
conn.then(()=>{
    console.log(`DB Connected`)
})
conn.catch((err)=>{
    console.log(err)
})

module.exports=conn