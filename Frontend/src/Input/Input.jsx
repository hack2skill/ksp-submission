import React, { useState } from 'react'
import Styles from "../Input/Input.module.css"
import { search } from "../https/request";


function Input() {
    const [link, setlink] = useState("");
    const [msg, setmsg] = useState("")
    async function ck() {
        const url = "https://ipqualityscore.com/api/json/url/qHgRkbygkOIr9ksDnjNrqcdvfsRHw3ah/"+link;
        try {
            const { data } = await search({ url })
            if (data === false){
              setmsg("This is safe application  ✨ ")
            }else{
                setmsg("This is unsafe ⚠️☠️")
            }
            console.log(data)
        } catch (error) {
            console.error(error.message);
        }
    }

    const handleChange = (event) => {
        setlink(event.target.value);
        console.log(link)
    };
    return (
        <div className={Styles.cont}>
            <div className={Styles.box}>
                <input type="text" placeholder='Put your links hear' className={Styles.search} autoComplete="off" value={link} onChange={handleChange} />
                <button className={Styles.btn} onClick={ck}> Check</button>
            </div>
            <div className={Styles.check}>{msg}</div>
        </div>
    )
}

export default Input