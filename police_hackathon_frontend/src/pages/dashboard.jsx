import React, {useEffect, useState} from "react";
import style from "./dashboard.module.scss"
import {
    Box,
    Button,
    ButtonGroup,
    Checkbox,
    Chip,
    Dialog,
    Fab,
    Input,
    InputLabel,
    MenuItem,
    FormControl,
    Pagination
} from "@mui/material";
import {makeStyles} from "@mui/styles";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import FingerPrintData from "../assets/finger_print_test.png"
import {
    faAngleDoubleLeft, faAngleDoubleRight,
    faAngleDown,
    faAngleUp, faChevronRight,
    faCircleXmark, faCodeMerge, faDownload,
    faMagnifyingGlass,
    faPlus,
    faXmark
} from "@fortawesome/free-solid-svg-icons";
import {DataGrid} from "@mui/x-data-grid";
import {Select} from "@mui/material";
import {ListItemIcon, ListItemText} from "@mui/material";
import MultiSelectDrop from "../../components/MultiSelectDrop";
import SideBar from "../../components/SideBar";
function AccountCircle(props) {
    return null;
}
const sample_data = ["here","ijaois","fsd","fokmvm","pooiwer","heree","he2re","hegre","he1re","hebre",]
const Dashboard=()=>{
    const [currentParamsState, setCurrentParamState] = useState(["here","ijaois"])
    const [modalState1, setModalState1] = useState(false);
    const [rows, setRows] = useState([]);
    const [searchTerm, setSearchTerm] = useState("benga")
    const searchGo=async(search_term)=>{
        let searchTerm = search_term;
        if (search_term!==undefined) {
            searchTerm = search_term
        }
        let data = await fetch(`http://13.71.90.52:8000/search/${searchTerm}`,{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            }
        })
        let json_data = await data.json();
        console.log(json_data["message"])
        setRows(json_data["message"])
    }
    useEffect( ()=>{
        searchGo();
    },[])
    const useStyles = makeStyles((theme) => ({
        formControl: {
            margin: theme.spacing(1),
            width: 300
        },
        indeterminateColor: {
            color: "#f50057"
        },
        selectAllText: {
            fontWeight: 500
        },
        selectedAll: {
            backgroundColor: "rgba(0, 0, 0, 0.08)",
            "&:hover": {
                backgroundColor: "rgba(0, 0, 0, 0.08)"
            }
        }
    }));
    const classes = useStyles();
    const handleChange = (event) => {
        const value = event.target.value;
        if (value[value.length - 1] === "all") {
            setSelected(selected.length === options.length ? [] : options);
            return;
        }
        setSelected(value);
    };
    const columns = [
        { field: 'id', headerName: 'ID', width: 130 },
        { field: 'State', headerName: 'STATE', width: 130 } ,
        { field: 'District_Name', headerName: 'DISTRICT_NAME', width: 130 } ,
        { field: 'PS_Name', headerName: 'PS_NAME', width: 130 } ,
        { field: 'FIRNo', headerName: 'FIRNO', width: 130 } ,
        { field: 'FIR_Date', headerName: 'FIR_DATE', width: 130 } ,
        { field: 'Person_No', headerName: 'PERSON_NO', width: 130 } ,
        { field: 'Arrest_Date', headerName: 'ARREST_DATE', width: 130 } ,
        { field: 'Person_Name', headerName: 'PERSON_NAME', width: 130 } ,
        { field: 'Father_Name', headerName: 'FATHER_NAME', width: 130 } ,
        { field: 'Gender', headerName: 'GENDER', width: 130 } ,
        { field: 'AgeWhileOpening', headerName: 'AGEWHILEOPENING', width: 130 } ,
        { field: 'Age', headerName: 'AGE', width: 130 } ,
        { field: 'Pres_Address1', headerName: 'PRES_ADDRESS1', width: 130 } ,
        { field: 'Perm_Address1', headerName: 'PERM_ADDRESS1', width: 130 } ,
        { field: 'PersonStatus', headerName: 'PERSONSTATUS', width: 130 } ,
        { field: 'Name', headerName: 'NAME', width: 130 } ,
        { field: 'Major_Head', headerName: 'MAJOR_HEAD', width: 130 } ,
        { field: 'Minor_Head', headerName: 'MINOR_HEAD', width: 130 } ,
        { field: 'Crime_No', headerName: 'CRIME_NO', width: 130 } ,
        { field: 'Arr_ID', headerName: 'ARR_ID', width: 130 } ,
        { field: 'Unit_ID', headerName: 'UNIT_ID', width: 130 } ,
        { field: 'fir_id', headerName: 'FIR_ID', width: 130 } ,
        { field: 'dedt', headerName: 'DEDT', width: 130 } ,
    ];

    const rows2 = [
        { id: 4, lastName: 'Stark', firstName: 'Arya', age: 16 },
    ];
    const [file, setFile] = useState();
    return <div style={{display:'flex'}}>
        {/*search dropdown*/}
        <SideBar/>
        <div>
            <div>

            </div>
            <div style={{
                display:"flex",
                gap:"30px",
                flexDirection:"column",
                alignItems:"center"
            }}>
                <form style={{display:"inline",marginTop:"10px"}}
                      onSubmit={(e)=>{
                          e.preventDefault();
                          // setSearchTerm(e.currentTarget.searchbar.value)
                          searchGo(e.currentTarget.searchbar.value);
                      }}
                >
                    <b>Search:</b>&nbsp;&nbsp;
                    <Input
                        id="standard-adornment-amount"
                        placeholder={"Names, id, etc"}
                        name={"searchbar"}
                        startAdornment={<FontAwesomeIcon icon={faMagnifyingGlass} style={{marginRight:"10px"}}/>}
                    />
                    <button
                        type={"submit"}
                    >Search</button>
                </form>
                <form style={{display:"flex"}} onSubmit={async (e)=>{
                    e.preventDefault();
                    let data = new FormData();
                    data.append("assignment_file",file);
                    let dataTest = await fetch("http://13.71.90.52:8000/image-recognize",{
                        method:"POST",
                        body: data
                    })
                    let json = await dataTest.json();
                    setRows(json.responses)
                }}>
                    <p>Image Recognition: &nbsp;</p>
                    <input type={"file"} name={"upload_img"} onChange={(e)=>{
                        if (e.target.files) {
                            setFile(e.target.files[0]);
                        }
                    }}/>
                    <button type={"submit"}>Search for image</button>
                </form>
                <form style={{display:"flex"}} onSubmit={async (e)=>{
                    e.preventDefault();
                    let data = new FormData();
                    data.append("assignment_file",file);
                    let dataTest = await fetch("http://13.71.90.52:8000/finger-recognize",{
                        method:"POST",
                        body: data
                    })
                    let json = await dataTest.json()
                    setRows(json.responses)
                }}>
                    <p>Finger print Recognition: </p>
                    <input type={"file"} name={"upload_img"} onChange={(e)=>{
                        if (e.target.files) {
                            setFile(e.target.files[0]);
                        }
                    }}/>
                    <button type={"submit"}>Search for fingerprint</button>
                </form>
            </div>
            &nbsp;
            &nbsp;
            &nbsp;
            {/*    Icons dropdown*/}
            <div style={{display:"inline"}}>
                {/*<b style={{color:"#8E8E8E"}}>params: </b>*/}
                {/*<Button variant="contained" style={{fontSize:"10px"}} size={"small"}*/}
                {/*        fullWidth={false} onClick={()=>setModalState1(true)}>*/}
                {/*    <FontAwesomeIcon icon={faPlus} fontSize={17}/>*/}
                {/*</Button>*/}
                {/*{*/}
                {/*    currentParamsState.map((cpvls)=>{*/}
                {/*        return <Chip style={{*/}
                {/*            margin:"0 5px"*/}
                {/*        }} label={cpvls} variant="outlined" onDelete={async()=>{*/}
                {/*            console.log("jasiodjoias")*/}
                {/*            setCurrentParamState(state=>{*/}
                {/*                let ret_val=state.filter((chips)=>chips!==cpvls);*/}
                {/*                console.log(ret_val)*/}
                {/*                return state*/}
                {/*            })*/}
                {/*        }}></Chip>*/}
                {/*    })*/}
                {/*}*/}
                <Dialog open={modalState1} >
                    <div style={{
                        padding:"15px",
                        height:"60vh",
                    }}>
                        <Box width={"450px"} style={{display:"flex",flexWrap:"wrap"}}>
                            <Box display={"flex"} position={"absolute"} right={12}><FontAwesomeIcon icon={faCircleXmark} color={"red"} fontSize={20} onClick={()=>{
                                setModalState1(false)
                            }
                            }/></Box>
                            <div>
                                {
                                    sample_data.map((val,index)=>{
                                        return <Fab variant="extended" size={"small"} style={{
                                            margin:"10px 6px",
                                        }}>
                                            <Checkbox size={"small"}
                                                      defaultChecked={currentParamsState.includes(val)}
                                                      onClick={(e)=>{
                                                          console.log(e.target.checked)
                                                          if (e.target.checked) {
                                                              setCurrentParamState(state=>{
                                                                  state.push(val);
                                                                  return state
                                                              });
                                                          } else {
                                                              setCurrentParamState(state=>{
                                                                  state.splice(state.indexOf(val),1);
                                                                  return state
                                                              })
                                                          }
                                                      }}
                                            />
                                            <p>{val}</p>
                                            &nbsp;
                                            &nbsp;
                                        </Fab>
                                    })
                                }
                            </div>
                        </Box>
                        {/*<span style={{maxWidth:"100%",marginTop:"10px"}}>Note: Increasing number of selections leads to higher time to load the results.</span>*/}
                        <Box justifyContent={"center"} display={"flex"} alignItems={"center"} position={"absolute"} bottom={"10px"}>
                            <b>Add new search paramters </b>&nbsp;&nbsp;
                            <Button size={"small"} variant={"contained"} disabled={false} onClick={()=>{
                                setModalState1(false);
                            }
                            }>Add</Button>
                            {/*&nbsp;&nbsp;<p>({currentParamsState && currentParamsState.length })</p>*/}
                        </Box>
                    </div>
                </Dialog>
            </div>
            {/*This here is the filter section*/}
            {/*<div style={{display:"flex", alignItems:"center", marginTop:"13.4px", flexWrap:"wrap"}}>*/}
            {/*    <p style={{color:"#8E8E8E"}}>Filters:&nbsp;</p>*/}
            {/*    {*/}
            {/*        demi_data.map((vls,index)=>{*/}
            {/*            return <MultiSelectDrop labelled_name={vls.name} options={vls.value}/>*/}
            {/*        })*/}
            {/*    }*/}
            {/*</div>*/}
            {/*    combined view parameters: */}
            {/*    <div style={{display:"flex", alignItems:"center", marginTop:"9.4px", flexWrap:"wrap"}}>*/}
            {/*        <p style={{color:"#8E8E8E"}}>combined view parameters:&nbsp;</p>*/}
            {/*        <Button variant="outlined" size={"small"} endIcon={<FontAwesomeIcon icon={faXmark} style={{height:"10px"}}/>} style={{*/}
            {/*            marginRight:"13px"*/}
            {/*        }}>*/}
            {/*            valid_id | valid_id_details*/}
            {/*        </Button>*/}
            {/*        <Button variant="outlined" size={"small"} endIcon={<FontAwesomeIcon icon={faXmark} style={{height:"10px"}}/>} style={{*/}
            {/*            marginRight:"13px"*/}
            {/*        }}>*/}
            {/*            valid_id | valid_id_details*/}
            {/*        </Button>*/}
            {/*        <p>+ add new parameters</p>*/}
            {/*    </div>*/}
            {/*    <h2 style={{*/}
            {/*        margin:"10px"*/}
            {/*    }}>Finger Print Data Analysis</h2>*/}
            {/*    <div style={{*/}
            {/*        display:"flex",*/}
            {/*        alignItems:"center",*/}
            {/*        justifyContent:"space-between",*/}
            {/*        width:"1300px"*/}
            {/*    }}>*/}
            {/*        <div>*/}
            {/*            <img src={FingerPrintData.src} style={{*/}
            {/*                width:"180px"*/}
            {/*            }}/>*/}
            {/*        </div>*/}
            {/*        <FontAwesomeIcon icon={faAngleDoubleRight}/>*/}
            {/*        <div style={{*/}
            {/*            display:"flex",*/}
            {/*            flexDirection:"column",*/}
            {/*            alignItems:"center",*/}
            {/*        }}>*/}
            {/*            <p*/}
            {/*                style={{*/}
            {/*                    fontSize:"45px",*/}
            {/*                    fontWeight:"900",*/}
            {/*                    color:"green"*/}
            {/*                }}*/}
            {/*            >90%</p>*/}
            {/*            <p*/}
            {/*            style={{*/}
            {/*                fontSize:"35px",*/}
            {/*                color:"green"*/}
            {/*            }}*/}
            {/*            >Match</p>*/}
            {/*            <div style={{*/}
            {/*                display:"flex",*/}
            {/*                gap:"10px",*/}
            {/*                alignItems:"center",*/}
            {/*                marginTop:"10px"*/}
            {/*            }}>*/}
            {/*                <p style={{color:"#8E8E8E"}}>Download:</p>*/}
            {/*                <div*/}
            {/*                    style={{*/}
            {/*                        width:"30px",*/}
            {/*                        height:"30px",*/}
            {/*                        background:"lightgrey",*/}
            {/*                        borderRadius:"7px",*/}
            {/*                        justifyContent:"center",*/}
            {/*                        display:"flex",*/}
            {/*                        alignItems:"center",*/}
            {/*                        color:"#ffffff"*/}
            {/*                    }}*/}
            {/*                ><FontAwesomeIcon icon={faDownload}/></div>*/}
            {/*            </div>*/}
            {/*        </div>*/}
            {/*        <FontAwesomeIcon icon={faAngleDoubleRight}/>*/}
            {/*        <div>*/}
            {/*            <div style={{ height: "350px",width: "600px" }}>*/}
            {/*                <DataGrid*/}
            {/*                    rows={rows2}*/}
            {/*                    columns={columns}*/}
            {/*                    pageSize={15}*/}
            {/*                    rowsPerPageOptions={[10]}*/}
            {/*                    page={0}*/}
            {/*                    style={{*/}
            {/*                        width:"400px"}*/}
            {/*                    }*/}
            {/*                />*/}
            {/*            </div>*/}
            {/*        </div>*/}
            {/*    </div>*/}
            <div style={{display:"flex", alignItems:"center",gap:"37px",marginTop:"17px"}}>
                <div style={{display:"flex", alignItems:"center", flexWrap:"wrap"}}>
                    <p style={{color:"#8E8E8E"}}>select page:&nbsp;</p>
                    <Pagination count={Math.round(rows.length / 15)} variant="outlined" shape="rounded" />
                </div>
                {/*<div style={{display:"flex", alignItems:"center", flexWrap:"wrap"}}>*/}
                {/*    <p style={{color:"#8E8E8E"}}>rows per page:&nbsp;</p>*/}
                {/*    <RowCountComp/>*/}
                {/*</div>*/}
                <div style={{
                    display:"flex",
                    alignItems:"center",
                    gap:"4px"
                }}>
                    <p style={{color:"#8E8E8E"}}>PDF:</p>
                    <div
                        style={{
                            width:"30px",
                            height:"30px",
                            background:"lightgrey",
                            borderRadius:"7px",
                            justifyContent:"center",
                            display:"flex",
                            alignItems:"center",
                            color:"#ffffff"
                        }}
                    ><FontAwesomeIcon icon={faDownload}/></div>
                </div>
                <div style={{display:"flex", alignItems:"center",  flexWrap:"wrap"}}>
                    {/*<p style={{color:"#8E8E8E"}}>merge direction:&nbsp;&nbsp;</p>*/}
                    {/*<ButtonGroup size={"small"} variant="outlined" color={"secondary"} aria-label="outlined button group">*/}
                    {/*    <Button>Left</Button>*/}
                    {/*    <Button>Full</Button>*/}
                    {/*    <Button>right</Button>*/}
                    {/*</ButtonGroup>*/}
                </div>
                {/*<p style={{color:"#8E8E8E"}}>excise (database 1)&nbsp;&nbsp;<FontAwesomeIcon icon={faCodeMerge}/>&nbsp;&nbsp;home guard (database 2)</p>*/}

            </div>
            &nbsp;
            &nbsp;
            &nbsp;
            &nbsp;
            {/*added MUI library*/}
            <div style={{ height: "70vh", width: '90vw' }}>
                <DataGrid
                    rows={rows}
                    columns={columns}
                    pageSize={15}
                    rowsPerPageOptions={[10]}
                    page={0}
                    // checkboxSelection
                    style={{
                        width:"100%"}
                    }
                />
            </div>

        </div>
    </div>
}
export const CustomFilter=()=>{
    const test_vals = ['test','test','test','test','test','test','test','test','test','test']
    const [toggleOpen,setToggleOpen]=useState(false);
    return <div
            style={{display:"flex",
                alignItems:'center',
                border: '1.03535px solid #C4C4C4',
                borderRadius: '3.10604px',
                position:"relative",
                marginBottom:"7px",
                marginRight:"19px"
            }}>
        <p style={{margin:"0 7.2px"}}><b >place_of_origin: </b>Bengaluru</p>
        <div className={style.drop_down} style={{background:"#FAFAFA",padding:"5px",borderRadius: '3.10604px'}} onClick={()=> {
            setToggleOpen(state=>!state)
        }
        }>
            <FontAwesomeIcon icon={!toggleOpen?faAngleDown:faAngleUp}/>
        </div>
    {/*    this here is for the drop-down*/}
        {toggleOpen && <div style={{
            width: "100%",
            maxHeight: "200px",
            position: "absolute",
            background: '#ffffff',
            top: "32px",
            border: '1.03535px solid #C4C4C4',
            borderRadius: '3.10604px',
            boxShadow: "0px 3.54973px 5.3246px rgba(0, 0, 0, 0.25)",
            overflow:"scroll",
            zIndex:1
        }}>
            {
                test_vals.map((vls, index) => {
                    return <div
                        className={style.drop_opt}
                        style={{
                            background: index == 3 ? "#6C85AB" : "",
                            borderRadius: "2.6623px",
                            height: "max-content",
                            margin: "3px 3.5px",
                            padding: "3px 0",
                        }}
                    ><p style={{marginLeft: "5px", color: index == 3 ? "#ffffff" : "#000000"}}>{vls}</p></div>
                })
            }
        </div>}

    </div>
}

export const RowCountComp=()=>{
    const test_vals = [1,2,3,4,5,6,7]
    const [toggleOpen,setToggleOpen]=useState(false);
    return <div
        style={{display:"flex",
            alignItems:'center',
            border: '1.03535px solid #C4C4C4',
            borderRadius: '3.10604px',
            position:"relative",
            margin:"3.5px 13px 3.5px 0"
        }}>
        <p style={{margin:"0 7.2px"}}>10</p>
        <div className={style.drop_down} style={{background:"#FAFAFA",padding:"5px",borderRadius: '3.10604px'}} onClick={()=> {
            setToggleOpen(state=>!state)
        }
        }>
            <FontAwesomeIcon icon={!toggleOpen?faAngleDown:faAngleUp}/>
        </div>
        {/*    this here is for the drop down*/}
        {toggleOpen && <div style={{
            width: "100%",
            maxHeight: "200px",
            position: "absolute",
            background: '#ffffff',
            top: "32px",
            border: '1.03535px solid #C4C4C4',
            borderRadius: '3.10604px',
            boxShadow: "0px 3.54973px 5.3246px rgba(0, 0, 0, 0.25)",
            overflow:"scroll",
            zIndex:1
        }}>
            {
                test_vals.map((vls, index) => {
                    return <div
                        className={style.drop_opt}
                        style={{
                            background: index == 3 ? "#6C85AB" : "",
                            borderRadius: "2.6623px",
                            height: "max-content",
                            margin: "3px 3.5px",
                            padding: "3px 0",
                        }}
                    ><p style={{marginLeft: "5px", color: index == 3 ? "#ffffff" : "#000000"}}>{vls}</p></div>
                })
            }
        </div>}

    </div>
}

export default Dashboard
