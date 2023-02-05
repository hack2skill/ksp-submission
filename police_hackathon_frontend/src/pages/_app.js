import { AuthProvider } from '@/context/AuthContext';
import '@/styles/globals.css'
import {createMuiTheme, ThemeProvider} from "@mui/material";
import SideBar from "../../components/SideBar";
const theme = createMuiTheme({
  typography: {
    fontFamily: ['Urbanist'].join(','),
  }
});
export default function App({ Component, pageProps }) {
    return (
  <AuthProvider>
    <ThemeProvider theme={theme}>
      <Component {...pageProps} />
    </ThemeProvider>
  </AuthProvider>
  )
}
