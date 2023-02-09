// Import Model
import User from "../models/User.js"
import bigPromise from "../middlewares/bigPromise.js"
import { cookieToken } from "../utils/cookieToken.js";
import { mailHelper } from "../utils/mailHelper.js";
export const createUser = bigPromise(async(req,res,next)=>{
    const {username,email,password,isSuperAdmin,CollegeId}=req.body;
    if((!username) || (!email) || (!password)){
        return res.status(400).json({
            success:false,
            message:"All fields are required!"
        })
    }
    
  const existingUser = await User.findOne({email:email})
    if(existingUser){
        return res.status(501).json({
            success:true,
            message:"User Already Exists !",
        })
    }
    else{
        const user=await User.create({
            username,
            email,
            password,
            isSuperAdmin
        })
        cookieToken(user,res,"You have been registered Successfully");
    }
})

export const login= bigPromise(async(req,res,next)=>{
    const {email,password}= req.body;
    const user=await User.findOne({email:email});
    if(!user)
    {
        return res.status(401).json({
        success:false,
        message:"No user exist with the given email"
        });
    }
    else{
        const user1=await user.isValidatedPassword(req.body.password,user.password);  
        if(!user1)
        {
            return res.status(401).json({
                success:false,
                message:"Invalid Login ! Please Enter Password Rightly !"
            });
        }
        cookieToken(user,res,"Successfully Logged in")
    }
});

export const logout=bigPromise(async(req,res,next)=>{
    res.cookie('token',null,{
        expires:new Date(Date.now()),
        httpOnly:true
    })
    res.status(200).json({
        success:true,
        message:"loggedOut Successfully"
    })
})

export const getUser = bigPromise(async(req,res,next) =>{

    if(!req.body.id){
   const details= await User.find({});
//    console.log(JSON.parse(details));
   if(!details)
   {
    return res.status(401).json({
        success:false,
        message:"No users exist till now"
    })
   }
   else{
    return res.status(200).json({
        success:true,
        message:"All User Details !",
        data:details
    });
   }
}
else{
    const details= await User.findById(req.body.id);
       if(!details)
       {
        return res.status(401).json({
            success:false,
            message:"No user exist till now"
        })
       }
       else{
        return res.status(200).json({
            success:true,
            message:"User Details !",
            data:details
        });
       }
}
});


export const updatePassword=bigPromise(async(req,res,next) =>{
   
   const user=await User.findOne({_id:req.body.id});
   console.log(user);
   const user1=await user.isValidatedPassword(req.body.oldpassword,user.password);
   if(!user1)
   {
    return res.status(401).json({
    success:false,
    message:"Old password does not match to the password"
    });
   }
//    const newpass=await bcrypt.hash(req.body.newpassword,10);
   const newpass=req.body.newpassword;
   user.password=newpass;
     const x=await user.save();
   cookieToken(user,res,"Password updated Successfully");
});


export const updateUserdetails = bigPromise(async(req,res,next)=>{
 const data={
    username:req.body.newusername,
    email:req.body.newemail,
 }
 
 const x= await User.findById(req.body.id);
 const user=await x.isValidatedPassword(req.body.password,x.password);
 if(!user)
 {
    return res.status(401).json({
     success:false,
     message:"Incorrect Password"
    });
 }

 const updated = await User.findByIdAndUpdate(req.body.id,data,{
    new:true,
    runValidators:true,
    useModifyandUpdate:false
   });
   
   if(!updated)
   {
    return res.status(401).json({
        success:false,
        message:"This email is already taken !"
     });
   }
   cookieToken(updated,res,"User details have been updated successfully");
});

export const Deleteuser = bigPromise(async(req,res,next)=>{
    const user1 = await User.findById(req.body.id);
    if(!user1)
    {
       return res.status(401).json({
        success:true,
        message:"Invalid details of the user !"
       })
    }
    await user1.remove();
    return res.status(200).json({
    success:true,
    message:"Successfully Deleted User"
    });
})