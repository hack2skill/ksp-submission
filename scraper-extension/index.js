let imgUrls = [];
setTimeout(() => {
  let a = document.getElementsByTagName("img");

  for (let index = 2; index < a.length; index++) {
    imgUrls.push(a[index].src);
  }

//   console.log(imgUrls);
}, 5000);
console.log(window.location.toString());

let foundPersonData = {};
// console.log(btn)
b = document.querySelector('button');
console.log(imgUrls)
b.addEventListener("click", function() {
    fetch("https://bhagwanbharose.azurewebsites.net/v1/api/extension/", {
        method: "post",
        // mode: "no-cors",
        headers: {
          "Content-Type": "application/json",
        },
        body:{
          baseUrl: window.location.toString(),
          imgUrl: imgUrls,
        },
      })
        .then((response) => response.json())
        .then((data) => {
            foundPersonData=data
          console.log(data);
        })
        .catch((err) => {
          console.log(err);
        });

        const orgPerImg = document.createElement("img");
        console.log(foundPersonData)
        orgPerImg.src = foundPersonData.Photo_Full_front;
        orgPerImg.style.width = "150px";
        orgPerImg.style.height = "135px";
        document.getElementById("per-Img").appendChild(orgPerImg);

        const perName = document.createElement("p");
        perName.innerHTML = `Name : ${foundPersonData}`;
        document.getElementById("per-Img").appendChild(perName);

        const perAge = document.createElement("p");
        perAge.innerHTML = `Age : ${foundPersonData}`;
        document.getElementById("per-Img").appendChild(perAge);

});
    


console.log(foundPersonData)


    // fetch("https://scary-fish-pea-coat.cyclic.app/v1/api/extension", {
    //   method: "POST",
    //   headers: {
    //     "Content-Type": "application/json"
    //   },
    //   body: JSON.stringify({baseUrl:window.location.})
    // })
    //   .then(response => response.json())
    //   .then(data =>{
    //       foundPersonData=data

    //        console.log(data)})
    //   .catch(error => console.error(error));

//   foundPersonData = {
//     _id: "63de6bd6d939f1e99eab6f6e",
//     District_Name: "Bagalkot",
//     UnitName: "Teradal PS",
//     FIRNo: "0014/2023",
//     RI: 1,
//     Year: 2023,
//     Month: 1,
//     "FIR Type": "Non Heinous",
//     FIR_Stage: "Under Investigation",
//     CrimeGroup_Name: "MISSING PERSON",
//     CrimeHead_Name: "Man",
//     ActSection: "IPC 1860 00MP",
//     Photo_Full_front:
//       "https://imageio.forbes.com/specials-images/imageserve/5f962df3991e5636a2f68758/0x0.jpg?format=jpg&crop=812,457,x89,y103,safe&width=1200",
//     Gender: "MALE",
//     Person_Name: "HUSENSAB SIRAJSAB NADAF",
//     age: 65,
//     Months: 0,
//     Days: 0,
//     Person_Age: [],
//   };








