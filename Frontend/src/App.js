import { Grid } from "../src/Grid/Grid";
import  {Navbar} from "../src/Navbar/Navbar"
import './App.css'
import Input from "./Input/Input";
import Submit from "./Submit/Submit";
import {Newgrid} from "./Newgrid/Newgrid.jsx"

function App() {
  return (
    <div >
      <Navbar />
      <Input/>
      <Submit/>
      <Grid/>
      <Newgrid/>
    </div>
  );
}

export default App;
