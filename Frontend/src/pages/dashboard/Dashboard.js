import React, { useState } from "react";
import { Grid } from "@material-ui/core";

// styles
import useStyles from "./styles";

// components
import Widget from "../../components/Widget";
import PageTitle from "../../components/PageTitle";
import Table from "./components/Table/Table";
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import { ToastContainer } from "react-toastify";
import { FaceOutlined, FingerprintOutlined, Search, Settings } from "@material-ui/icons";

import mock from './mock'
import { Typography } from '@material-ui/core';


export default function Dashboard(props) {
  const classes = useStyles();

  const fingerPrintImageInput = React.useRef();
  const faceImageInput = React.useRef();

  const [fingerPrintImage, setFingerPrintImage] = useState(null);
  const [faceImage, setFaceImage] = useState(null);

  const [searchOptions, setSearchOptions] = useState(mock.table);

  const [searchValue, setSearchValue] = useState();
  const [gender, setGender] = useState("M" | "F");
  const [age, setAge] = useState(Number);

  const [advanceSearch, setIsAdvancedSearch] = useState(false)

  const handleOnAdvanceSearchClick = () => {
    setIsAdvancedSearch(!advanceSearch);
  }
  const myHeaders = new Headers();
  myHeaders.append("User-Agent", "-U");
  myHeaders.append("Authorization", "ApiKey RnpEc0c0WUJXNXBSYkhGUm1GUHk6SVYzS3VwakRRTmluMk8ybENKRWJEQQ==");
  myHeaders.append("Content-Type", "application/json");

  const raw = JSON.stringify({
    "query": {
      "bool": {
        "must": {
          "multi_match": {
            "query": searchValue,
            "operator": "and",
            "fuzziness": "AUTO",
            "fields": [
              "Name^11",
              "Person_Name^10",
              "Father_Name^9",
              "Perm_Address1^7",
              "Pres_Address1^6",
              "District_Name^5",
              "Gender^4",
              "State^3",
              "FIRNo^2",
              "Photo_Full_front"
            ]
          }
        },
        "filter": !advanceSearch === true ? [] : [{
          "match": {
            "Gender": {
              "query": gender
            }
          }
        },
        {
          "match": {
            "Age": {
              "query": age
            }
          }
        }]
      }
    },
    "size": 50
  });

  const requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
  };

  const handleSearch = async () => {
    await fetch("https://fcd19a3882ba4cf99f3386ed6885b50f.ap-south-1.aws.elastic-cloud.com:443/fir_new,fir_ktk/_search?pretty", requestOptions)
      .then(response => response.text())
      .then(result => { 
        const parsedResult = JSON.parse(result);
        console.log(parsedResult)
        setSearchOptions(parsedResult.hits.hits);
      })
      .catch(error => console.log('error', error));

  }

  const handleFingerPrintImageChange = async (e) => {
    if (e.target.files[0]) {
      const image = e.target.files[0];
      setFingerPrintImage(image)
    }
  }

  const handleFaceImageChange = async (e) => {
    if (e.target.files[0]) {
      const image = e.target.files[0];
      setFaceImage(image)
    }
  }

  let fingerprintFormData = new FormData();
  fingerprintFormData.append('file', fingerPrintImage)

  const fingerprintRequestOptions = {
    method: 'POST',
    // headers: myHeaders,
    body: fingerprintFormData,
    redirect: 'follow'
  };


  const [imageName, setImageName] = useState();
  const [imageScore, setImageScore] = useState();


  const handleFingerPrintImageSearch = async (e) => {
    await fetch("http://35.154.50.44:5000/process_fingerprint", fingerprintRequestOptions)
      .then(response => response.text())
      .then(async (result) => {
        const parsedResult = JSON.parse(result);
        setImageName(parsedResult[0].image_name);
        setImageScore(parsedResult[0].match_score);
      })
      .catch(error => console.log('error', error));
  }

  let faceFormData = new FormData();
  faceFormData.append('file', faceImage)

  const faceRequestOptions = {
    method: 'POST',
    // headers: myHeaders,
    body: faceFormData,
    redirect: 'follow'
  };

  const [faceName, setFaceName] = useState();
  const [faceScore, setFaceScore] = useState();

  const handleFaceImageSearch = async (e) => {
    await fetch("http://35.154.50.44:5000/process_faceimage", faceRequestOptions)
      .then(response => response.text())
      .then(async (result) => {
        const parsedResult = JSON.parse(result);
        setFaceName(parsedResult[0].image_name);
        setFaceScore(parsedResult[0].match_score)
        setSearchValue(parsedResult[0].image_name);
      })
      .catch(error => console.log('error', error));
  }


  return (
    <>
      <PageTitle title="Dashboard" />
      <Grid container spacing={4}>
        <Grid item xs={12} md={12}>
          <Widget title="" disableWidgetMenu>
            <div className={classes.dashedBorder}>
              <TextField
                id="outlined-full-width"
                label="Search"
                color="success"
                value={searchValue}
                onChange={(e) => { setSearchValue(e.target.value) }}
                style={{ margin: 10, width: 500 }}
                placeholder="Search by name, father name, address, district, state"
                margin="normal"
                InputLabelProps={{
                  shrink: true,
                }}
                variant="outlined"
              />
              <Button
                variant="contained"
                color="primary"
                size="medium"
                onClick={handleSearch}
                style={{ marginRight: 10, margin: 10, padding: 15 }}
                className={classes.button}
                startIcon={<Search />}
              >
                Search 
              </Button>
              <Button
                variant="contained"
                color="secondary"
                size="medium"
                onClick={handleOnAdvanceSearchClick}
                style={{ marginRight: 10, margin: 10, padding: 15 }}
                className={classes.button}
                startIcon={<Settings />}
              >
                Advanced Search
              </Button>
              <br />
              <Button
                variant="contained"
                color="default"
                size="medium"
                style={{ marginRight: 10, margin: 10, padding: 15, paddingRight: 210 }}
                className={classes.button}
                startIcon={<FingerprintOutlined />}
              >
                <input type='file' onChange={handleFingerPrintImageChange} ref={fingerPrintImageInput}></input>
              </Button>
              <Button
                variant="contained"
                color="primary"
                size="medium"
                onClick={handleFingerPrintImageSearch}
                style={{ marginRight: 10, margin: 10, padding: 15 }}
                className={classes.button}
                
                startIcon={<Search />}
              >
                Search Fingerprint
              </Button>
              <br />
              {imageName && <Typography style={{ marginLeft: 15 }} variant="span" weight="medium">
                Image Name is <strong>{imageName}</strong>
              </Typography>}
              {imageScore && <> <br />
                <br /></>}
              {imageScore && <Typography style={{ marginLeft: 15 }} variant="span" weight="medium">
                Match Score is <strong>{imageScore}</strong>
              </Typography>}
              <br />
              <Button
                variant="contained"
                color="inherit"
                size="medium"
                style={{ marginRight: 10, margin: 10, padding: 15, paddingRight: 210 }}
                className={classes.button}
                startIcon={<FaceOutlined />}
              >
                <input type='file' onChange={handleFaceImageChange} ref={faceImageInput}></input>
              </Button>
              <Button
                variant="contained"
                color="primary"
                size="medium"
                onClick={handleFaceImageSearch}
                style={{ marginRight: 10, margin: 10, padding: 15 }}
                className={classes.button}
                startIcon={<Search />}
              >
                Search Face
              </Button>
              <br />
              {faceName && <Typography style={{ marginLeft: 15 }} variant="span" weight="medium">
                Person Identified is <strong>{faceName}</strong>
              </Typography>}
              {faceName && <> <br />
                <br /></>}
              {faceScore && <Typography style={{ marginLeft: 15 }} variant="span" weight="medium">
                Match Score is <strong>{faceScore}</strong>
              </Typography>}
              <br />
              {advanceSearch && <>
                <TextField
                  id="outlined-full-width"
                  label="Gender"
                  color="success"
                  value={gender}
                  onChange={(e) => { setGender(e.target.value) }}
                  style={{ margin: 10 }}
                  placeholder="M or F"
                  margin="normal"
                  InputLabelProps={{
                    shrink: true,
                  }}
                  variant="outlined"
                />
                <TextField
                  id="outlined-full-width"
                  label="Age"
                  color="success"
                  value={age}
                  onChange={(e) => { setAge(e.target.value) }}
                  style={{ margin: 10 }}
                  placeholder="Age"
                  margin="normal"
                  InputLabelProps={{
                    shrink: true,
                  }}
                  variant="outlined"
                />
              </>}

              <ToastContainer
                position="top-right"
                autoClose={5000}
                hideProgressBar={false}
                newestOnTop={false}
                closeOnClick
                rtl={false}
                pauseOnFocusLoss
                draggable
                pauseOnHover
              />
            </div>
          </Widget>
        </Grid>
      </Grid>
      <Grid container spacing={4}>
        <Grid item xs={12}>
          <Widget
            title="Matched Results"
            upperTitle
            noBodyPadding
            bodyClass={classes.tableWidget}
          >
            <Table data={searchOptions} />
          </Widget>
        </Grid>
      </Grid>
    </>
  );
}
