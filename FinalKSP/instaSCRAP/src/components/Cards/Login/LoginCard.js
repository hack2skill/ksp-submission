import React from 'react'
import "./Login.css"
import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom/dist';
const port = "http://localhost:8000";

export default function LoginCard()
{
  const [user, setUser] = useState({email:"", password:""});
  const navigate = useNavigate()

  const handleOnSubmit =async(e)=>{
      e.preventDefault();
      console.log(user)
      const resp = await fetch(`${port}/api/auth/login`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: user.email,
            password: user.password,
          }),
        });
        const json = await resp.json();
        console.log(json)

        if (json.success) {
          sessionStorage.setItem("token", json.authToken);
          navigate("/");
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
        <span id="title">Sign In</span>
        <input type="text" id="name" name="email" placeholder="Email Id" onChange={handleOnChange}/>
        <input type="password" id="password" name="password" placeholder="Password" onChange={handleOnChange}/>
        <div id="button">
            <input type="submit" value="Sign in"/>
        </div>
    <div id="linksParent">
        <Link to='/signup'>Sign up</Link>
    </div>
    </form>
</div>
  )
}
