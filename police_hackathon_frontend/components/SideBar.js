import React from "react";
import style from "./SideBar.module.scss";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faChartBar, faEye} from "@fortawesome/free-solid-svg-icons";
const SideBar=()=>{
    return <div style={{width:'76px',background:"rgba(55, 41, 41, 0.79)",height:"100vh",margin:"10px",borderRadius:"10px"}}
        className={style.sidebar}
    >
        <div className={style.round}>
            <p>AG</p>
        </div>
        {/*here is the database numbers*/}
        <div style={{display:"flex",flexDirection:"column",justifyContent:"center"}}>
            <span className={style.header}>127</span>
            <span className={style.text}>datasets</span>
        </div>
        <div style={{
            display:"flex",
            flexDirection:"column",
            alignItems:"center",
            gap:"14px"
        }}>
            <div>
                <p style={{textAlign:"center"}} className={style.viewText}>Current View</p>
            </div>
            {/*here is the switcher section*/}
            <div>
                <FontAwesomeIcon icon={faEye}
                                 style={{
                                     color:"#ffffff",
                                     fontSize:"37px"
                                 }}
                />
            </div>
            <div className={style.cockpit}>
                <FontAwesomeIcon icon={faChartBar}
                                 style={{
                                     color:"grey",
                                     fontSize:"37px",
                                 }}
                />
                <div style={{display:"flex",flexDirection:"column",justifyContent:"center"}} >
                    <span className={style.header} style={{color:"grey"}}>127</span>
                    <span className={style.text} style={{color:"grey"}}>datasets</span>
                </div>
            </div>
        </div>
    </div>
}
export default SideBar;
