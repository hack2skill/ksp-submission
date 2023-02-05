const mediaRoutes = require('../app')
const { getMissingPersonDetailByImageName } = require('../db/missingPersonFunc')
const axios = require('axios')
const FormData = require('form-data');
const form = new FormData();
const apiUrl = 'https://seahorse-app-nub7v.ondigitalocean.app/arun'
// const apiUrl = 'https://abc2424.cognitiveservices.azure.com/'

mediaRoutes.post('/v1/api/extension', (req, res) => {
    //image link
    console.log(req.body)
    const scrapedData = {
        baseUrl: req.body.baseUrl,
        imgUrl: req.body.imgUrl
    }
    let respData = []
    scrapedData.imgUrl.forEach(imgLink => {
        console.log(imgLink)
        axios({
            method: 'get',
            url: imgLink
        })
            .then((response) => {
                // console.log(response.data) //image in base 64
                let imageBase64 = Buffer.from(response.data).toString('base64')   //data available in base64
                // console.log(imageBase64)

                return imageBase64

            })
            .then(async (imageDataToML) => {
                
                let buf=imageDataToML

                
                    const ab = new ArrayBuffer(buf.length);
                    const view = new Uint8Array(ab);
                    for (let i = 0; i < buf.length; ++i) {
                        view[i] = buf[i];
                    }
                    console.log(ab)
                // axios.post(apiUrl, ab, {
                //         headers: {
                //             'accept': 'application/json',
                //             'Accept-Language': 'en-US,en;q=0.8',
                //             'Content-Type': `multipart/form-data; boundary=${ab._boundary}`,
                //         }
                //     })

                
                    
                    
                
                
                return { found: true, name: 'husen#_cc296e8b-9dce-4814-9f98-069e2a430d7e1260.jpg' }

            })
            .then((imageResult) => {
                console.log('- - - - kfjf- - - - - \n')
                console.log(imageResult)
                if (imageResult.found) {
                    console.log('Searching for details ', imageResult.name)
                    return getMissingPersonDetailByImageName(imageResult.name)
                } //get Detail from DB (search via imagename)
                else {
                    //upload image and log anytime
                    return false
                }

            })
            .then(personDetails => {
                console.log('sdfsdfsfsd');
                console.log(personDetails)

                if (personDetails) respData.push({ imgLink, personDetails })
                if (respData.length === scrapedData.imgUrl.length) res.send({ msg: respData })

            })
            .catch((err) => {
                console.log(err)
                res.send({ msg: 'Some error occured' })
            })
    });
})

module.exports = {
    mediaRoutes
}