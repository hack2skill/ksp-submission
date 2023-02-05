import React,{useState}from 'react'
import { Parser } from '@json2csv/plainjs';
import axios from 'axios';
const port = "http://localhost:8000";


function LinkedIn() {
    const [username, setUsername] = useState({username:""});
    const[isDisabled, setIsDisabled ] = useState(true);
    const [data, setData] = useState({});
    const [json, setJson] = useState({})

    const handleOnChange = (e) =>{
        setUsername({...username, [e.target.name]: e.target.value});
    }

    const handleDownload = () => {
        const parser = new Parser();
        const csv = parser.parse(data);
        const blob = new Blob([csv], { type: 'text/csv' });
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'linkedin.csv';
        link.click();
      };

    const handleOnClick = async() =>{ //**********************change api key later */

        const options = {
          method: "GET",
          url: "https://linkedin-profile-data.p.rapidapi.com/linkedin-data",
          params: { url: `https://www.linkedin.com/in/${username.username}` },
          headers: {
            "X-RapidAPI-Key":
              "e3c00217edmsh843b82807faeca0p1bb939jsn1e20f2758527",
            "X-RapidAPI-Host": "linkedin-profile-data.p.rapidapi.com",
          },
        };

      axios.request(options).then(function (response) {
        setJson(response.data);

        if(Object.keys(json).length === 0) {
          console.log("server busy")
          alert('server busy')
          return
        }

        setData(json)
        setIsDisabled(false)
        console.log(data)
      }).catch(function (error) {
        console.error(error);
      });

      
    }
  return (
    <div className="phonescrap">
      <input
        type="text"
        name="username"
        placeholder="Enter LinkedIn User Name"
        onChange={handleOnChange}
        className="enterphone"
      />
      <div className="phonebuttons">
        <div className="button1">
          <button onClick={handleOnClick} style={{ width: "150px" }}>
            Get Data
          </button>
        </div>
        <div className="button2">
          <button
            onClick={handleDownload}
            disabled={isDisabled}
            style={{ width: "150px" }}
          >
            Download Data
          </button>
        </div>
      </div>
      <div style={{ width: "70%" }}>
        <pre>{JSON.stringify(data, null, 2)}</pre>
      </div>
    </div>
  );
}

export default LinkedIn
