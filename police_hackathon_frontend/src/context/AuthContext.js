import { createContext,useState, useEffect } from "react"
import jwt_decode from 'jwt-decode'
import { useRouter } from "next/router"


const AuthContext = createContext()

export default AuthContext

export const AuthProvider = ({children}) => {
  let [authTokens, setAuthTokens] = useState(null)
  let [user, setUser] = useState(null)

  useEffect(() => {
      let token = localStorage.getItem('authTokens')
      if(token){
          let decode = jwt_decode(JSON.parse(token).access_token)
          setUser(decode)
      }

      let user_data = localStorage.getItem('user')
      if(user_data){
          setUser(JSON.parse(user_data))
      }
  },[])

  const router = useRouter()

  let login = async(email, password) => {
      let formData = new FormData()
      formData.append('username', email)
      formData.append('password', password)
      let response = await fetch('http://localhost:8000/auth',formData,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
      })

      let data = response.data

      if(response.status === 200){
          const decode = jwt_decode(data.access_token)
          setAuthTokens(data)
          setUser(decode)
          localStorage.setItem('authTokens', JSON.stringify(data))
          router('/dashboard')
      }else{
          console.log('Error')
      }

  }

  let logout = () => {
      setAuthTokens(null)
      setUser(null)
      localStorage.removeItem('authTokens')
      router('/')
  }

  let contextData = {
      user:user,
      authTokens:authTokens,
      login:login,
      logout: logout,
  }

  return (
      <AuthContext.Provider value={contextData}>
          {children}
      </AuthContext.Provider>
  )
}

