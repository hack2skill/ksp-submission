import asyncio
import fuzzywuzzy
from fuzzywuzzy import fuzz
import psycopg2

async def fuzzy_name_search(names, query):
    async def check_name(name):
        return fuzz.token_sort_ratio(name, query)

    checks = [asyncio.ensure_future(check_name(name)) for name in names]
    results = await asyncio.gather(*checks)

    return [names[i] for i, score in enumerate(results) if score >=70]

async def main():
    names = []
    query = 'mohammad'
    


    conn = psycopg2.connect(
    host="kspone.postgres.database.azure.com",
            database="police",
            user="mykspadmin",
            password="PoliceHackathon123",
            port='5432')
    curr = conn.cursor()
    curr.execute("SELECT person_name from icjs union select person_name from ksp where person_name is not null;")
    names=curr.fetchall()
   
    names=[i[0] for i in names]
    print(names)
    result = await fuzzy_name_search(names, query)
    print(result)




asyncio.run(main())