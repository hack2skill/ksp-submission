import React from 'react'
import Styles from '../Grid/Grid.module.css'

export const Newgrid = () => {
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
