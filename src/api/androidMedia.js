const mediaRoutesAndroid = require('../app')
const { getMissingPersonDetailByImageName } = require('../db/missingPersonFunc')
const axios = require('axios')

const path=require('path')
const ffmpeg=require('ffmpeg')
const { mediaRoutes } = require('./chromeExtention')

const apiUrl = 'https://seahorse-app-nub7v.ondigitalocean.app/array'

mediaRoutesAndroid.post('/v1/api/android/img', (req, res) => {
    let imageData = req.body.files.img00

    axios({url:apiUrl,
        method:'post',

        
    })
        .then((response) => {
            // console.log(response.data) //image in base 64
            let imageBase64 = Buffer.from(response.data).toString('base64')   //data available in base64
            // console.log(imageBase64)

            return imageBase64

        })
        .then(async (imageDataToML) => {
            console.log('sending img to ML server')
            // return axios.post('https://seahorse-app-nub7v.ondigitalocean.app/image',{image:imageDataToML})
            return { found: true, name: 'husen#_cc296e8b-9dce-4814-9f98-069e2a430d7e1260.jpg' }
        })
        .then((imageResult) => {
            console.log(imageResult)
            if (imageResult.found) {
                console.log('Searching for details ', imageResult.name)
                return getMissingPersonDetailByImageName(imageResult.name)
            } //get Detail from DB (search via imagename)
            else{
                //upload image on 
                return false;
            }

        })
        .then(personDetails => res.send(personDetails))

        .catch((err) => {
            console.log(err)
            res.send({ msg: 'Some error occured' })
        })

})

mediaRoutesAndroid.post('/v1/api/android/vid', (req, res) => {
    try {
        var process = new ffmpeg(path.join(__dirname,'../vid_file.mp4'));
        process.then(function (video) {
            // Callback mode
            video.fnExtractFrameToJPG(path.join(__dirname,'../../frames'), {
                // frame_rate : 1,
                every_n_seconds:2,
                // number : 5,
                file_name : 'my_frame_%t_%s'
            }, function (error, files) {
                if (!error)
                    console.log('Frames: ' + files);
                    axios({
                        method:'post',
                        url:apiUrl,
                        data:{
                            arr:files
                        }
                    })
                    
            });
        }, function (err) {
            console.log('Error: ' + err);
        });
    } catch (e) {
        console.log(e.code);
        console.log(e.msg);
    }


})

module.exports=mediaRoutesAndroid