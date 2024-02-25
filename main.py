from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    return FileResponse("static/index.html")


@app.get("/contacts")
async def read_contacts(skip: int = 0, limit: int = 12):
    with open("contacts.json", "r") as json_file:
        contacts = json.load(json_file)

    # Appliquer la pagination
    paginated_contacts = contacts[skip : skip + limit]
    return paginated_contacts


@app.get("/contacts/count")
async def get_contacts_count():
    print("YOUPI")
    with open("contacts.json", "r") as json_file:
        contacts = json.load(json_file)
    return {"count": len(contacts)}


@app.get("/contact/{contact_id}", response_class=HTMLResponse)
def read_contact(request: Request, contact_id: int):
    with open("contacts.json", "r") as json_file:
        contacts = json.load(json_file)
    contact = next(
        (c for c in contacts if str(c.get("id", "")) == str(contact_id)), None
    )
    if contact:
        return templates.TemplateResponse(
            "contact_details.html", {"request": request, "contact": contact}
        )
    else:
        raise HTTPException(status_code=404, detail="Contact not found")
