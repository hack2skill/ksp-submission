const express = require('express')
const app = express()
const cors = require('cors')
const routers = require('./routes')
const mysqlConnection = require('./database/Sqlconnect')
var gplay = require('google-play-scraper');
const { Configuration, OpenAIApi } = require("openai");

const corsOptio = {
    credentials: true,
    origin: ["http://localhost:3000"]
}
app.use(cors(corsOptio))
app.use(express.json());
app.use(routers)

const configuration = new Configuration({
    apiKey: "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",
});
const openai = new OpenAIApi(configuration);


async function gg() {
    var play = await gplay.search({
        term: "loan apps",
        num: 1,
        country: "IN",
    })
    // console.log(play)

    q = await gplay.reviews({
        appId: play[0].appId,
        num: 2
    })


    q.data.forEach((element) => {
        // console.log(element.text);
        openapi(element.text)
    });

    async function openapi(g) {
        const response = await openai.createCompletion({
            model: "text-davinci-003",
            prompt: `i have give u a text of some app reviews  based on the text given give me output in just two words good or bad based on the user experience on use the two words dont print extra words.The sentence is ${g}`,
            temperature: 2,
            max_tokens: 30,
        });
        console.log( response.data.choices[0].text)
        txt =  response.data.choices[0].text
        if (txt.includes("good")) {
            console.log("good")
        }
    }


}

const port = 5000
app.listen(port, () => {
    console.log(`Server running on ${port}!`)
    // setInterval(() => {
    gg()
    // }, 100000000000);
})
