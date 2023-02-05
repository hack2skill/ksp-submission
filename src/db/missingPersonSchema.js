const mongoose = require('mongoose')

const ageSchema=new mongoose.Schema({
    years:Number,
    months:Number,
    days:Number
})

const missingPersonSchema=new mongoose.Schema({
    District_Name:String,
    UnitName:String,
    FIRNo:String,
    RI:Number,
    Year:Number,
    Month:Number,
    Offence_From_Date:Date,
    Offence_To_Date:Date,
    FIR_Date:Date,
    FIR_Type:String,
    FIR_Stage:String,
    CrimeGroup_Name:String,
    CrimeHead_Name:String,
    ActSection:String,
    Photo_Full_front:String,
    Photo_image_url:String,
    Gender:{
        type:String,
        enum:['Male','Female']
    },
    Person_Name:String,
    Person_Age:[ageSchema]
})

const missingPerson=mongoose.model('missingPersonFIR',missingPersonSchema,'missingPersonFIR')


module.exports=missingPerson