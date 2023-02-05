import './App.css';
import UserContext from './context/UserContext';
import Navbar from './components/Navbar/Navbar';
import Scrappers from './components/Scrappers/Scrappers';
import { useContext } from 'react';
import Login from './pages/Login/Login';
import {Routes, Route} from "react-router-dom"
import Signup from './pages/Signup/Signup';
import PhoneScrapper from './pages/Scrappers/Phone/PhoneScrapper';
import Instagram from './pages/Scrappers/Instagram/Instagram';
import LinkedIn from './pages/Scrappers/LinkedIn/LinkedIn';
import Twitter from './pages/Scrappers/Twitter/Twitter';
import Facebook from './pages/Scrappers/Facebook/Facebook';

function App() {
const context = useContext(UserContext);
const{user} = context
  return (
      <div className="sections">
          <Navbar/>
          <Routes>
            <Route exact path = "/login" element = {<Login/>}></Route>
            <Route exact path = "/signup" element = {<Signup/>}></Route>
            <Route exact path = "/" element = {<Scrappers/>}></Route>


            <Route exact path = "/scrape/phone" element = {<PhoneScrapper/>}></Route>
            <Route exact path = "/scrape/instagram" element = {<Instagram/>}></Route>
            <Route exact path = "/scrape/linkedin" element = {<LinkedIn/>}></Route>
            <Route exact path = "/scrape/twitter" element = {<Twitter/>}></Route>
            <Route exact path = "/scrape/facebook" element = {<Facebook/>}></Route>
          </Routes>
      </div>
  );
}

export default App;
