import mongoose from "mongoose";

const eventSchema=new mongoose.Schema({
name:{
    type:String
},
aadhar_no:{
type:Number
},
contact_no:{
    type:Number
},
address:
 {
    type:String
 }
});
const Event=mongoose.model("Event",eventSchema);
export default Event;