import React,{useState}from 'react'
import "./PhoneScrapper.css";
import { Parser } from '@json2csv/plainjs';
const port = "http://localhost:8000";


function PhoneScrapper() {
    const [number, setNumber] = useState("");
    const [data, setData] = useState({});
    const[isDisabled, setIsDisabled ] = useState(true);
    const[scrapedData, setScrapedData] = useState("");

    const handleOnChange = (e) =>{
        setNumber({...number, [e.target.name]: e.target.value});
    }

    const dataa = {
        "name":"sai",
        "roll":45
    }
    const handleDownload = () => {
        const parser = new Parser();
        const csv = parser.parse(data);
        const blob = new Blob([csv], { type: 'text/csv' });
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'phonedata.csv';
        link.click();
      };

    const handleOnClick = async() =>{
        const resp = await fetch(`${port}/api/scrape/phone`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "auth-token" :"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjNkYWQ5YTM0ODU0YTM5NDZiMTgwMjBmIn0sImlhdCI6MTY3NTMzODUxMX0.kZIUAd_psPjf4PNl_nIIINXrl9giBL5UA4ja6wmqv-s"
            },
            body: JSON.stringify({
              number: number.number,
            }),
          });
          const json = await resp.json();
          console.log(json)
          setScrapedData(json)

          const val = json.data[0].value;

          const obj = {
            name:val.name,
            gender:val.gender,
            email: val.internetAddresses.length > 0?val.internetAddresses[0].id:undefined,
            state:val.addresses[0].city,
            country:val.addresses[0].countryCode,
            job:val.jobTitle,
            carrier:val.phones[0].carrier,
            countryCode: val.phones[0].countryCode,
            numberType: val.phones[0].numberType

          }
          setData(obj)
          setIsDisabled(false)
        //   console.log(obj)
  
      
    }
  return (
    <div className="phonescrap">
      <input
        type="text"
        name="number"
        placeholder="Enter phone"
        onChange={handleOnChange}
        className="enterphone"
      />
      <div className="phonebuttons">
        <div className="button1">
          <button onClick={handleOnClick} style={{ width: "150px" }}>
            Get Phone Data
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
        <h1>Scraped Data</h1>
      <div style={{ border: "1px solid", borderColor: "rgb(160,160,255)" }}>
        <pre>{JSON.stringify(scrapedData, null, 2)}</pre>
      </div>
    </div>
  );
}

export default PhoneScrapper
