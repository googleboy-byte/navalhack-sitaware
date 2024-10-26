from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import uvicorn
from pydantic import BaseModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

'''
THIS CODE IS SHIT, DONT FOLLOW THIS CODE JUST COOK UP SOMETHING USING FASTAPI. IF NOT POSSIBLE THEN PIVOT TO FLASK. BUT NOT DJANGO.
DJANGO TOO HARD
'''

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use ["http://localhost:8000"] to restrict to specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

class TextInput(BaseModel):
    text: str

@app.post("/api/post/textdata")
async def submit_text(data: TextInput):
    # Handle the text received here
    print(data.text)
    return {"received_text": data.text}

@app.post("/api/post/file")
async def upload_file(file: UploadFile = File(...)):
    # Save the file content if needed
    contents = await file.read()
    return {"filename": file.filename, "content_size": len(contents)}

@app.get("/ops", response_class=HTMLResponse)
async def read_ops():
    with open("static/dashboard.html") as f:
        return HTMLResponse(content=f.read())

@app.get("/landing", response_class=HTMLResponse)
async def read_ops():
    with open("static/landing.html") as f:
        return HTMLResponse(content=f.read())

@app.get("/", response_class=HTMLResponse)
async def read_ops_norm():
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
