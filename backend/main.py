from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import sqlite3
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

'''
THIS CODE IS SHIT, DONT FOLLOW THIS CODE JUST COOK UP SOMETHING USING FASTAPI. IF NOT POSSIBLE THEN PIVOT TO FLASK. BUT NOT DJANGO.
DJANGO TOO HARD
'''

@app.get("/ops", response_class=HTMLResponse)
async def read_ops():
    with open("static/dashboard.html") as f:
        return HTMLResponse(content=f.read())

@app.get("/landing", response_class=HTMLResponse)
async def read_ops():
    with open("static/landing.html") as f:
        return HTMLResponse(content=f.read())


@app.get("/api/contacts", response_class=JSONResponse)
async def read_records():
    conn = sqlite3.connect('./localdb/contacts.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts_basic")
    records = cursor.fetchall()
    conn.close()
    
    # Convert tuples to lists
    records_as_lists = [list(record) for record in records]
    return records_as_lists

@app.get("/api/zones", response_class=JSONResponse)
async def read_records():
    conn = sqlite3.connect('./localdb/contacts.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM zones_basic")
    records = cursor.fetchall()
    conn.close()
    
    # Convert tuples to lists
    records_as_lists = [list(record) for record in records]
    return records_as_lists


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
