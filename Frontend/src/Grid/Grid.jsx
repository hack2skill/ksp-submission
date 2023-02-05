// import { React, useEffect, useState } from 'react'
// import Styles from '../Grid/Grid.module.css'
// import { que } from "../https/request";
// export const Grid = () => {
//   const [rowData, setrowdata] = useState([]);
//   useEffect(() => {
//     async function fetchdata() {
//       try {
//         const { data } = await que({})
//         setrowdata(data)
//         console.log(data)
//       } catch (error) {
//         console.error(error.message);
//       }
//     }
//     fetchdata()
//   }, []);
// var gg = rowData[1]
// var gd = rowData[0]
// var gk = rowData[2]
//   return (
//     <div className={Styles.cont}>

//       <div className={Styles.fbox}>
//         <div className={Styles.txt}> Top apps reported</div>
//           <div className={Styles.app}>
//             <div><img src="lo.png" className={Styles.im} alt="logo" /></div>
//             <div>
//               Name:{gg.nameofapp}<br />
//               Where u found:{gg.whereufound}<br />
//               Related:{gg.whatisitrelated}<br />
//               Scam involved:{gg.scamrelated}<br />
//             </div>
//           </div>

//       </div>

//     </div>

//   )
// }

import React from 'react'
import Styles from '../Grid/Grid.module.css'

export const Grid = () => {
  return (
    <div className={Styles.cont}>

            <div className={Styles.fbox}>
                <div className={Styles.txt}> Top apps reported</div>
                <div className={Styles.app}>
                <div><img src="lo.png" className={Styles.im} alt="logo"/></div>
                <div>
                    Name:xyz<br/>
                    Repoted: 100 timess
                </div>
                </div>
                <div className={Styles.app}>
                <div><img src="lo.png" className={Styles.im} alt="logo"/></div>
                <div>
                    Name:xyz<br/>
                    Repoted: 100 timess
                </div>
                </div>
            </div>

    </div>

  )
}
