import {useContext} from 'react'
import Image from 'next/image'
import styles from '@/styles/Login.module.css'
import ksp_bg from '../assets/red_yellow.png'
import { TextField, Button } from '@mui/material'

import AuthContext from '../context/AuthContext'

const Login = () => {
  let {login} = useContext(AuthContext)
  const handleClick = () => {
    let email = document.getElementById('email').value
    let password = document.getElementById('password').value
    console.log(email, password)
    login(email, password)
  }
  return (
    <div className={styles.container}>
      <div className={styles.left}>
        <div className={styles.logo}>
          <Image src = {ksp_bg} fill/>
        </div>
      </div>
      <div className={styles.right}>
        <h1 className={styles.title}>Welcome!</h1>
        <TextField
          id='email'
          label = 'Email'
          variant='outlined'
          placeholder='user@gmail.com'
          fullWidth
          sx = {{margin: '1em 0'}}
        />
        <TextField
          id='password'
          label = 'Password'
          type='password'
          variant='outlined'
          placeholder='Enter your password here'
          fullWidth
          sx = {{margin: '1em 0'}}
        />
        <Button 
          variant='contained' 
          fullWidth
          className = {styles.signin}
          onClick = {() => handleClick()}
          >Sign In</Button>
        <p>Contact admin if you have forgotten password</p>
      </div>
      <div className = {styles.circle}></div>
    </div>
  )
}

export default Login;