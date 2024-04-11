from fastapi import FastAPI
from gfg import get_geeksforgeeks_stats
from cc import get_codechef_stats
from cf import get_codeforces_stats

app = FastAPI()

@app.get("/gfg/{username}")
async def get_gfg(username: str):
    return get_geeksforgeeks_stats(username)

@app.get("/cc/{username}")
async def get_cc(username : str):
    return get_codechef_stats(username)

@app.get("/cf/{username}")
async def get_cf(username : str):
    return get_codeforces_stats(username)