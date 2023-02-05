import React from "react";
import { useState, useEffect } from "react";
import axios from "axios";
import { Parser } from "@json2csv/plainjs";
const port = "http://localhost:8000";

const Twitter = () => {
  const [username, setUsername] = useState("");
  const [twitterProfile, setTwitterProfile] = useState({});
  const [tweets, setTweets] = useState([]);

  const downloadTwitterProfile = () => {
    const parser = new Parser();
    const csv = parser.parse(twitterProfile);
    // const csv = Papa.unparse(dataa);
    const blob = new Blob([csv], { type: "text/csv" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "twitterProfile.csv";
    link.click();
  };
  const downloadTwitterTweets = () => {
    const parser = new Parser();
    const csv = parser.parse(tweets);
    // const csv = Papa.unparse(dataa);
    const blob = new Blob([csv], { type: "text/csv" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "twitterTweets.csv";
    link.click();
  };

  const handleTwitterProfile = async () => {
    const response = await axios.post("http://localhost:5000/twitter/profile", {
      twitter_username: username,
    });
    const obj = {
      "Created On": response.data.created,
      Links: response.data.descriptionLinks,
      "Display Name": response.data.displayname,
      "Followers Count": response.data.followersCount,
      "Friends Count": response.data.friendsCount,
      Location: response.data.location,
      "Banner URL": response.data.profileBannerUrl,
      "Image URL": response.data.profileImageUrl,
      Description: response.data.renderedDescription,
      "Verification Status": response.data.verified,
    };
    setTwitterProfile(obj);
  };

  const handleTwitterTweets = async () => {
    const response = await axios.post("http://localhost:5000/twitter/tweets", {
      twitter_username: username,
    });
    setTweets(response.data);
  };

  const getHateSpeechRating = async () => {
    const response = await axios.post("http://localhost:5000/twitter/tweets", {
      twitter_username: username,
    });
    setTweets(response.data);
    // console.log(tweets.length)
    let arr = [];
    for (let i = 0; i < 20; i++) {
      let x = Math.floor(Math.random() * (tweets.length - 1 - 0) + 0);
      // console.log(x)
      arr.push(tweets[x]);
    }
    // console.log(arr)
    let arr2 = [];
    arr.forEach((e) => {
      if(e.length > 2) arr2.push(e[2]);
    });
    console.log(arr2);

    const resp = await fetch(`${port}/api/hatespeech/detect_hate_speech`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "auth-token":
          "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjNkYWQ5YTM0ODU0YTM5NDZiMTgwMjBmIn0sImlhdCI6MTY3NTMzODUxMX0.kZIUAd_psPjf4PNl_nIIINXrl9giBL5UA4ja6wmqv-s",
      },
      body: JSON.stringify({
        words: arr2,
      }),
    });
    const json = await resp.json();
    console.log(json);

    let obj = {};
    json.forEach((e) => {
      let s = 0;
      e.results.forEach((e) => {
        s += e.probabilities["1"];
      });

      let name = e.label;
      obj[name] = s / arr2.length;
      s = 0;
    });
    console.log(obj); // final object with average values

    const parser = new Parser();
    const csv = parser.parse(obj);
    // const csv = Papa.unparse(dataa);
    const blob = new Blob([csv], { type: "text/csv" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "hatespeech.csv";
    link.click();
  };

  return (
    <div className="phonescrap">
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Enter Twitter Username"
      />
      <hr />
      <div className="phonebuttons">
        <button onClick={handleTwitterProfile} style={{ width: "200px" }}>
          Get Twitter Profile
        </button>
        <button onClick={handleTwitterTweets} style={{ width: "200px" }}>
          Get Tweets
        </button>
        <button onClick={downloadTwitterProfile} style={{ width: "200px" }}>
          Download Twitter Profile
        </button>
        <button onClick={downloadTwitterTweets} style={{ width: "200px" }}>
          Download Twitter Tweets
        </button>
        <button onClick={getHateSpeechRating} style={{ width: "200px" }}>
          Get Hate Speech Rating
        </button>
      </div>
      <hr />
      <h1>Twitter Profile Information:</h1>
      <div style={{ border: "1px solid", borderColor: "rgb(160,160,255)" }}>
        <pre>{JSON.stringify(twitterProfile, null, 2)}</pre>
      </div>
      <hr />
      <h1>Twitter Tweets:</h1>
      <div style={{ border: "1px solid", borderColor: "rgb(160,160,255)", width:"80%" }}>
        <ul>
          {tweets.map((tweet, index) => (
            <li key={index}>
              <p>Date: {tweet[0]}</p>
              <p>Username: {tweet[1]}</p>
              <p>Content: {tweet[2]}</p>
              <p>Links: {JSON.stringify(tweet[3])}</p>
            </li>
          ))}
        </ul>
      </div>
      <hr />
    </div>
  );
};

export default Twitter;
