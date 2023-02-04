require('dotenv').config({path:__dirname+'/.env'})
const path = require('path');

const api_id = Number(process.env.APP_ID)
const api_hash = process.env.API_HASH;
const telesession = process.env.TELE_SESSION;
// console.log(api_hash,api_id)
// 1. Create instance
const { TelegramClient,Api } = require('telegram')
const { StringSession } = require('telegram/sessions')
const input = require('input') // npm i input

async function getUsernameDetails(username){

    const stringSession = new StringSession(telesession); 
    
        console.log('Loading interactive example...')
        const client = new TelegramClient(stringSession, api_id, api_hash, { connectionRetries: 5 })
        await client.start({
            phoneNumber: async () => await input.text('number ?'),
            password: async () => await input.text('password?'),
            phoneCode: async () => await input.text('Code ?'),
            onError: (err) => console.log(err),
        });
        
        console.log('You should now be connected.')
        console.log(client.session.save()) // Save this string to avoid logging in again
        await client.sendMessage('me', { message: 'Hello!' });
        
    
                try{
                    
                    const result = await client.invoke(
                        new Api.contacts.ResolveUsername({
                            username:username
                        }),
                        );
                        
                        // console.log(result); 
                        
                        return result
                    }
                    catch{
                        return {
                            usernameExists:false
                        }
                    }
                
                                
        }
                            
module.exports={
    getUsernameDetails:getUsernameDetails
}