import React from "react";
import Navbar from "../../Components/Navbar";
import Praveen from "../../images/Praveen.jpg";
import Brain from "../../images/brain.png";
import Hack from "../../images/Hack2Skill.png";
import Photo from "../../images/Photo.png";
import Mask from "../../images/Mask.png";
import a from "../../images/1.png";
import { ROUTES } from "../../routes/Routerconfig";
import b from "../../images/2.jfif";
import { MdEmail } from "react-icons/md";
import Inputfield from "../../Components/Email/Input";
import Password from "../../Components/Password/Password";
import { useNavigate } from "react-router-dom";
import { useState } from "react";
import main from "../../images/kar_main_logo.png";
import Button from "../../Components/Button/Button";
import axios from "axios";
import "./Home.css";
import { notification} from 'antd';

const Home = () => {
  const navigate = useNavigate();
  
  const [api, contextHolder] = notification.useNotification();
  const openNotificationWithIcon = (type,message,desc) => {
    api[type]({
      message: `${message}`,
      description:
        `${desc}`,
    });
  };


  const [email, setEmail] = useState();
  const [password, setPassword] = useState();

  const handleEmailState = (e) => setEmail(e.target.value);
  const handlePasswordState = (e) => setPassword(e.target.value);
  let a=0;
  const login = () => {
    
    if(!email || !password)
    {
      a=1;
      openNotificationWithIcon('error','Login Failed','Please enter the required details');
    }
    axios
      .post("http://localhost:1999/api/user/login", { email, password })
      .then((res) => {
        console.log(res);
        console.log(res.data.user._id);
        localStorage.setItem("uid", res.data.user._id);
        navigate("/dashboard");
      })
      .catch((err) => {
        console.log(err);

        if(!a){
        openNotificationWithIcon('error','Login Failed','Please enter the Correct details');
        }
      });
  };

  return (
    <div className="h-[100vh]">
    {contextHolder}
      <Navbar />
      {/*{
        [...Array(10).keys()].map(item => (<img src={`http://localhost:1999/images/${item}.png`} />))
      }*/}
      
      <div className="grid mt-[1rem]  grid-cols-3 h-[76vh]">
        <div className="col-span-1 pl-[5rem]">
          <img src={Praveen} className="h-[34rem]"/>
          <p className="pt-[1.5rem] text-3xl text-center text-sky-900 pr-[3rem] font-bold">
            Shri.Praveen Sood, IPS
          </p>
          <p className="text-xl pt-[1rem] text-sky-900 pr-[3rem]">
            Director General and Inspector General of Police.<br></br>
            The Karnataka Government Appointed Praveen Sood - an IPS Officer of
            the 1986 batch as the new Director General and Inspector General of
            Police heading the state's police force following superannuation of
            incumbent DG and IGP Neelmani Raju.
          </p>
        </div>
        <div className="col-span-2">
          <div class="flex justify-center">
            <div class="flex flex-col md:flex-row md:max-w-[70rem] rounded-lg bg-white shadow-lg">
              <img
                class=" w-full h-96 md:h-auto object-cover md:w-48 rounded-t-lg md:rounded-none md:rounded-l-lg"
                src={Photo}
                alt=""
              />
              <div class="p-4 flex flex-col justify-start">
                <h5 class="text-gray-900 text-3xl font-medium mb-2">MOTTO</h5>
                <p class="text-gray-700 text-lg mb-4">
                  The motto of the Karnataka State Police is "COMMITMENT,
                  COMPASSION, PROFESSIONALISM." The first word, "commitment,"
                  refers to the dedication and resolve of the police officers to
                  serve and protect the citizens of the state. The second word,
                  "compassion," acknowledges the importance of treating everyone
                  with empathy and understanding, regardless of their
                  circumstances. Finally, the third word, "professionalism,"
                  emphasizes the need for the police to perform their duties
                  with the highest level of skill and integrity.
                </p>
              </div>
            </div>
          </div>
          <div className="flex grid-cols-2">
            <div class="flex justify-center pt-[1rem]">
              <div class="rounded-lg shadow-lg bg-white w-[40rem] ml-[7.3rem]">
                <a
                  href="#!"
                  data-mdb-ripple="true"
                  data-mdb-ripple-color="light"
                >
                  <img
                    class="rounded-t-lg h-[19rem] w-[70rem]"
                    src={Mask}
                    alt=""
                  />
                </a>
                <h5 class="text-gray-900 text-3xl pt-[0.6rem] font-medium mb-2">
                  AI FACE DETECTION
                </h5>
                <p className="p-3 text-gray-700 text-lg">
                  {" "}
                  Our ultimate goal is to create an artificial intelligence
                  model that can identify a person's face from an input with few
                  features and provide an output that has the highest likelihood
                  of appearing in the database for advanced surveillance.
                </p>
                <div
                  className="h-[3rem]"
                  style={{
                    background:
                      "linear-gradient(to right, #0066cc 0%, #33ccff 100%)",
                  }}
                ></div>
              </div>
            </div>
            <div className="inline-block">
              <img
                src={b}
                className="w-[29rem] h-[23rem] pt-[1rem] ml-[1rem] rounded-xl"
                alt=""
              />
              <button
                class="zoom-in-out-box ml-[4rem] mt-[4rem] middle none center rounded-lg bg-blue-700 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-pink-500/20 transition-all hover:shadow-lg hover:shadow-blue-500/40  focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
                data-ripple-light="true"
                onClick={"#login"}
              >
                Login to Continue 👇
              </button>
            </div>
          </div>
        </div>
      </div>

      <div id="login" className="h-[105vh] flex grid-cols-2">
        <div class="flex pt-[6rem] max-w-[43rem] pl-[5rem] justify-center col-span-1">
          <div class="rounded-lg shadow-lg bg-white">
            <a href="#!" data-mdb-ripple="true" data-mdb-ripple-color="light">
              <img class="rounded-t-lg" src={Brain} alt="" />
            </a>
            <div class="p-6">
              <p className="text-[5rem] pl-[12rem]">
                P<span className="text-green-600">O</span>LICE
              </p>
              <p className="text-[5rem]">
                H<span className="text-green-600">A</span>CK
                <span className="text-green-600">A</span>THON
              </p>
              <img src={Hack} className=" ml-[16.3rem] h-[9rem]" alt="" />
              <p className=" text-4xl pt-[2rem] font-semibold">
                IIIT Banglore 2023
              </p>
            </div>
          </div>
        </div>
        <div className="">
          <div className="flex justify-center mt-[3rem] items-center min-h-screen">
            <div className="flex justify-center rounded-lg">
              <div className=" -z-[1] bg-[#0E223D] min-h-[90vh] w-[400px] rounded-lg translate-x-[100px]">
                <img
                  src={main}
                  alt="Company logo"
                  className="w-[8rem] h-[7rem] mt-[2.5rem] ml-[2.5rem]"
                />
              </div>
              <div className="h-[80%] my-auto left-[200px] z-10 flex flex-col w-[650px] max-w-md px-4 py-8 bg-white rounded-lg shadow-2xl shadow-gray-600/50  sm:px-6 md:px-8 lg:px-10 min-h-[80vh] -translate-x-[100px] justify-center">
                <p className="text-[3rem] tracking-widest text-blue-900 mb-[3rem]">
                  LOGIN
                </p>
                <Inputfield
                  prefix={<MdEmail />}
                  placeholder="Enter Email"
                  type="email"
                  value={email}
                  handleState={handleEmailState}
                  label="email"
                />
                <Password value={password} handleState={handlePasswordState} />
                <Button label="Login" handleevent={login} />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
