import json
import requests
import os
import time
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import Request
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from utils import parse_file


app = FastAPI(title="Karnataka Police | Bank Account Analysis")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.add_middleware(GZipMiddleware)

if not os.path.exists("data"):
    os.makedirs("data")

@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}

@app.post("/parse_bank_statement", tags=['Parser'])
async def parse_bank_statement(file: UploadFile = File(...)):
    start_time = time.time()

    file_location = f"data/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    print({"info": f"file '{file.filename}' saved at '{file_location}'"})


    output_path = parse_file(file_location)

    print("Time taken to process:", round(time.time()-start_time, 2), "sec")

    #remove the input file
    # os.remove(file_location)

    return FileResponse(path=output_path, filename=output_path)
    


if __name__=='__main__':
    uvicorn.run("main:app", host="127.0.0.1",port=8000)
    



