from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    return FileResponse("static/index.html")


@app.get("/contacts")
async def read_contacts():
    with open("contacts.json", "r") as json_file:
        contacts = json.load(json_file)
    return contacts
