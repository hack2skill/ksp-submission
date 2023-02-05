from fastapi import FastAPI, HTTPException
import psycopg2
import photomatchFinal, fuzzysearchTest, fingermatchFinal
app = FastAPI()

def DNS():
    conn = psycopg2.connect(
        host="kspone.postgres.database.azure.com",
        database="police",
        user="mykspadmin",
        password="PoliceHackathon123",
        port="5432")
    return conn

def query(stat:str):
    conn = DNS()
    cur = conn.cursor()
    cur.execute(f"select person_name from icjs where state='{stat}';")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return {'result': result}

print(query('Karnataka'))