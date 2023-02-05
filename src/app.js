const express = require('express')
const app = express()
const fileUpload = require('express-fileupload')
const path=require('path')

const PORT = process.env.PORT || 9000

const axios = require('axios')
const ffmpeg = require('ffmpeg')

app.use(express.urlencoded({ extended: true }))
app.use(express.json())
app.use(fileUpload())

app.use((req, res, next) => {
  handleError(express.json(), req, res, next);
});

app.get('/', (req, res) => {
  console.log(req.files, '\n', '- - - - - - - - - - - \n')
  console.log(req.body)
  res.send({ msg: 'Index page' })
})
app.post('/', async (req, res) => {
  console.log(req.files.sdfsdfs.data, '\n', '- - - - - - - - - - - \n')
  console.log(req.body)
  console.log( __dirname,__filename )
  let file=path.join(__dirname,'/vid_file.mp4')
  
  try {
    var process = new ffmpeg(file);
    process.then(function (video) {
        video.fnExtractFrameToJPG(path.join(__dirname,'../frames'), {
          
            every_n_seconds:.5
        })
    }, function (err) {
        console.log('Error: ' + err);
    });
} catch (e) {
    console.log(e)
}



  res.send({ msg: 'Index page post' })
})

app.listen(PORT, () => {
  console.log(`Server active on ${PORT}`)
})

function handleError(middleware, req, res, next) {
  middleware(req, res, (err) => {
    if (err) {
      console.error(err);
      return res.status(400).send({ msg: "Format not correct" }); // Bad request
    }
    next();
  });
}

module.exports = app