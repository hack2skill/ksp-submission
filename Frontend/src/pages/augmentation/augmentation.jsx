import React, { useRef } from "react";
import Navbar from "../../Components/Navbar";
import upload from "../../images/upload.png";
import "./augmentation.css";
import axios from "axios";
import { useState, useEffect } from "react";
import { Modal } from "antd";
import { useNavigate } from "react-router-dom";
import { ROUTES } from "../../routes/Routerconfig";
import Loader from "../../Components/Loader/Loader";
import MLLoader from "../../Components/Loader/MLLoader";
function Augment() {
  const navigate = useNavigate();
  const fileref = useRef();
  const [ml, setML] = useState(false);
  const [move1, setMove1] = useState(false);
  const [move, setMove] = useState(false);
  const [file, setFile] = useState(true);
  const [loading, setLoading] = useState(false);
  const handleChange = (e) => {
    let file = e.target.files[0];
    setFile(file);
    console.log(file);
  };

 

  let images = [];
  function shreyas() {
    const importAll = (r) => {
      return r.keys().reduce((acc, key) => {
        acc.push({ name: key.split("/").pop().split(".")[0], url: r(key) });
        return acc;
      }, []);
    };

    images = importAll(
      require.context("../../Components/augmented", false, /\.(png|jpe?g|svg)$/)
    );

    if (images.length != 0) {
      setML(false);
      console.log("Hello");
      setMove(true);
    }
    console.log(images);
  }

  useEffect(() => {
    shreyas();
  }, []);

  const clear = () => {
    fileref.current.value = null;
  };

  const submit = async () => {
    const formdata = new FormData();
    formdata.append("image", file);
    setLoading(true);
    await axios
      .post("http://localhost:1999/api/upload/augment", formdata)
      .then((res) => {
        console.log(res);
        setLoading(false);
        setOpen(true);
        clear();
      })
      .catch((err) => {
        console.log(err);
        setLoading(false);
        clear();
      });
  };

  const [open, setOpen] = useState(false);
  const [confirmLoading, setConfirmLoading] = useState(false);
  const [modalText, setModalText] = useState("Successfully Uploaded Image");
  const handleOk = () => {
    setConfirmLoading(true);
    setTimeout(() => {
      setOpen(false);
      setConfirmLoading(false);
      setML(true);
      shreyas();
    }, 2000);
  };
  const handleCancel = () => {
    setOpen(false);
    setML(true);
  };

  const shreyas1 = () => {
    navigate(ROUTES.Augoutput);
  };

  return (
    <div>
      {loading ? (
        <div className="">
          <Loader />
        </div>
      ) : null}
      {ml  ? (
        <div className="">
          <MLLoader />
        </div>
      ) : null}
      <div className={loading || ml ? "opacity-25 hello" : "hello"}>
        <Navbar />
        <div className="bg-white mt-[2rem] max-w-[60rem] ml-[32rem]">
          <p className="pt-[1rem] font-serif text-[3rem]">
            Please Upload Image Of The Person whose Augmentation can be generated
          </p>
        </div>
        <div className="border-dotted border-4 ml-[41rem] h-[25rem] w-[45rem]  mt-[3rem]">
          <div class="upload-btn">
            <button class="btn">
              <img src={upload} className="pr-[3rem]" alt="" />
              Upload Image
            </button>
            <br></br>
            <input
              type="file"
              ref={fileref}
              onChange={handleChange}
              className="text-white ml-[8rem] text-xl mt-[2rem]"
            />
          </div>
        </div>
        <button
          class="button-30 mt-[3rem] w-[10rem]"
          onClick={submit}
          role="button"
        >
          Submit
        </button>

        {!loading ? (
          <Modal
            title="Success ✅"
            className="mt-[17rem] text-4xl"
            open={open}
            onOk={handleOk}
            confirmLoading={confirmLoading}
            onCancel={handleCancel}
          >
            {modalText}
          </Modal>
        ) : null}
        {move ? (
          <button
            class="button-30 mt-[3rem] ml-[4rem] w-[10rem]"
            onClick={() => shreyas1()}
            role="button"
          >
            Output
          </button>
        ) : null}
        <div class="abc"></div>
      </div>
    </div>
  );
}

export default Augment;
