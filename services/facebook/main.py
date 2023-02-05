import uvicorn
from fastapi import FastAPI
import os
from facebook_scraper import get_profile
from pprint import pprint
import requests

# load environment variables
port = 8000

# initialize FastAPI
app = FastAPI()

@app.get("/facebook")
def fb(fbid:str):
    try: 
        return get_profile(fbid, cookies="cookies.txt")
    except:
        return {"message":"User not found"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)