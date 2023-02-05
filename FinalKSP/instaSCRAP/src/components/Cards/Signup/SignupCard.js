import React from 'react'
import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom/dist';
import './SignupCard.css'
const port = "http://localhost:8000";

function SignupCard() {
    const [user, setUser] = useState({name:"",email:"", password:""});
    const navigate = useNavigate()

    const handleOnSubmit =async(e)=>{
        e.preventDefault();
        console.log(user)
        const resp = await fetch(`${port}/api/auth/createUser`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              name: user.name,
              email: user.email,
              password: user.password,
            }),
          });
          const json = await resp.json();
          console.log(json)

          if (json.success) {
            sessionStorage.setItem("token", json.authToken);
            navigate("/login");
            alert("resgistration successfull")
          } else {
            alert("invalid credentials");
          }
    }

    const handleOnChange = (e) =>{
        setUser({...user, [e.target.name]: e.target.value});
    }
  return (
    <div className='loginbody'>
    <form  onSubmit = {handleOnSubmit}>
        <span id="title">Sign Up</span>
        <input type="text" id="name" name="name" placeholder="Name" onChange={handleOnChange}/>
        <input type="text" id="name" name="email" placeholder="Email Id" onChange={handleOnChange}/>
        <input type="password" id="password" name="password" placeholder="Password" onChange={handleOnChange}/>
        <div id="button">
            <input type="submit" value="Signup"/>
        </div>
    <div id="linksParent">
        <Link to = "/login">Sign in</Link>
    </div>
    </form>
</div>
  )
}

export default SignupCard
