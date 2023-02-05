import React, {useEffect, useState} from "react";
import PiChart from "../assets/Chart.png"
import style from "./chartCreator.module.scss"
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faExternalLink, faLink} from "@fortawesome/free-solid-svg-icons";
import {Button, makeStyles, TextField} from "@mui/material";
import HeatMapTS from "../assets/HeatMapTS.svg"
import {CustomFilter} from "@/pages/dashboard";
import {HexColorPicker} from "react-colorful";
import Highcharts from "highcharts";
import HighchartsHeatmap from 'highcharts/modules/heatmap';
import HighchartsSankey from "highcharts/modules/sankey";
import HighchartsReact from "highcharts-react-official";
import sankey_test_data from "../test/sankey_test"
import line_chart_test from "../test/line_chart_test"
if (typeof Highcharts === 'object') {
    HighchartsHeatmap(Highcharts);
    HighchartsSankey(Highcharts);
}
export const ChartCreator=()=>{
    const [selColor, setSelColor] = useState("#aabbcc");
    const WEEK_DAYS = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
    ];
    const pi_data = {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: '',
            align: 'left'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        accessibility: {
            point: {
                valueSuffix: '%'
            }
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                }
            }
        },
        series: [{
            name: 'Brands',
            colorByPoint: true,
            data: [{
                name: 'Chrome',
                y: 70.67,
                sliced: true,
                selected: true
            }, {
                name: 'Edge',
                y: 14.77
            },  {
                name: 'Firefox',
                y: 4.86
            }, {
                name: 'Safari',
                y: 2.63
            }, {
                name: 'Internet Explorer',
                y: 1.53
            },  {
                name: 'Opera',
                y: 1.40
            }, {
                name: 'Sogou Explorer',
                y: 0.84
            }, {
                name: 'QQ',
                y: 0.51
            }, {
                name: 'Other',
                y: 2.6
            }]
        }]
    }
    const options = {
        chart: {
            type: 'heatmap',
            plotBorderWidth: 1,
        },
        title: {
            text: 'Revenue per hour per weekday heatmap',
        },
        xAxis: {
            min: 0,
            max: 13,
            tickInterval: 1,
            labels: {
                step: 1,
                style: {
                    fontSize: '14px',
                    fontFamily: 'Open Sans',
                },
            },
            gridLineWidth: 0,
            lineWidth: 0.5,
            lineColor: 'rgba(0,0,0,0.75)',
            tickWidth: 0.5,
            tickLength: 3,
            tickColor: 'rgba(0,0,0,0.75)',
            title: {
                text: 'Hour',
            },
        },
        yAxis: {
            categories: WEEK_DAYS,
            title: 'Weekdays',
            labels: {
                style: {
                    fontSize: '14px',
                    fontFamily: 'Open Sans',
                },
            },
        },
        tooltip: {
            formatter: function () {
                return (
                    '<b>Hour Is: </b>' +
                    this.point.x +
                    '<br /><b>Day Is:</b> ' +
                    this.point.y +
                    '<br />' +
                    '<b>Revenue Is:</b> $' +
                    this.point.value
                );
            },
        },
        colorAxis: {
            stops: [
                [0, 'rgba(56, 7, 84, 0.4)'],
                [0.5, 'rgba(56, 7, 84, 0.65)'],
                [1, 'rgba(69, 9, 104, 1)'],
            ],
        },
        series: [
            {
                name: 'Revenue',
                borderWidth: 0.5,
                borderColor: 'white',
                dataLabels: {
                    enabled: true,
                    color: '#000000',
                },
                data: [
                    [1, 2, 100],
                    [1, 4, 100],
                    [4, 3, 200],
                    [7, 4, 300],
                    [2, 5, 400],
                    [5, 6, 500],
                    [12, 1, 600],
                    [10, 0, 700],
                ],
            },
        ],
    };
    useEffect(()=>{

    },[])
    return <div>
        <p  className={style.header}>Currently saved visuals !</p>
        <div className={style.indiCol}>
            <img src={PiChart.src} width={"80px"} height={"80px"}/>
            <div style={{textAlign:"right"}} className={style.named}>
                <h3>Offense List 22-23</h3>
                <p style={{width:"250px"}}>This here is the visual chart representing
                    the Citizen data between 2022-23</p>
                <p style={{color:"blue"}}>Open <FontAwesomeIcon icon={faExternalLink}/></p>
            </div>
        </div>
        <p  className={style.header}>Create new visuals!</p>
        <div className={style.mainChartSec}>
        <div className={style.chartDiv}>
            <div className={style.chartCreateMain}>
                <div style={{display:"flex",alignItems:"center",gap:"10px"}}>
                    <label>Name the visual instance:</label>
                    <TextField
                        label="Chart Name"
                        id="filled-size-small"
                        defaultValue=""
                        variant="filled"
                        size="small"
                    />
                </div>
                <div style={{display:"flex",alignItems:"center",gap:"10px",marginTop:"20px"}}>
                    <label>Select the type of Graph to visualize:</label>
                    <CustomFilter/>
                </div>
                <div style={{display:"flex",alignItems:"center",gap:"10px",marginTop:"20px"}}>
                    <label>write a detailed description of the
                        visual:</label>
                    <textarea/>
                </div>
                <div style={{display:"flex",gap:"160px",marginTop:"30px"}}>
                    <div>axis orientation: <input type={"checkbox"}/></div>
                    <div>choose color scheme: <b style={{color:selColor}}>{selColor}</b><HexColorPicker color={selColor} onChange={setSelColor}/></div>
                </div>
                <div>
                    <p style={{marginTop:"30px"}}>selected database: <i><b>chronicled_district_data_db1</b></i></p>
                </div>
                <div style={{display:"flex",alignItems:"center",gap:"40px",marginTop:"20px"}}>
                    <div><label>x-axis data: </label>
                        <CustomFilter/></div>
                    <div><label>y-axis data: </label>
                        <CustomFilter/></div>
                </div>
                <Button variant={"contained"}>generate</Button>
            </div>
            <img src={HeatMapTS.src}/>
        </div>
            <div style={{width:"800px", marginLeft:"10px"}}>
                <HighchartsReact highcharts={Highcharts} options={options} />
                <HighchartsReact
                    highcharts={Highcharts}
                    options={sankey_test_data}
                    // constructorType="sankyChart"
                />
                <HighchartsReact
                    highcharts={Highcharts}
                    options={pi_data}
                    // constructorType="sankyChart"
                />
                <HighchartsReact
                    highcharts={Highcharts}
                    options={line_chart_test}
                    // constructorType="sankyChart"
                />
            </div>
        </div>

    </div>
}
export default ChartCreator
