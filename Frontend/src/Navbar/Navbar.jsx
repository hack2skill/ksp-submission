import React from 'react'
import Styles from  '../Navbar/Navbar.module.css'

export const Navbar = () => {
    return (
        <header>
            <nav className={`${Styles.nav} ${Styles.cont}`}>
                <div className={Styles.logo}> 
                    <img src="hack.webp" className={Styles.navimg} alt="logo"/>
                    <span>Fraud app Detection</span>
                </div>
                <div className={Styles.navitems}>
                    <ul className={Styles.list}>
                        <li>Home</li>
                        <li>Contact</li>
                        <li>Info</li>
                        <li>Help</li>
                    </ul>
                </div>
            </nav>
        </header>
    )
}