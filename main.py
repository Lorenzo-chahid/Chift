from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from databases import Database
from dotenv import load_dotenv
import sqlalchemy
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

contacts = sqlalchemy.Table(
    "contacts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String),
    sqlalchemy.Column("phone", sqlalchemy.String),
    sqlalchemy.Column("is_company", sqlalchemy.Boolean),
)

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
def read_root():
    return FileResponse("static/index.html")


@app.get("/contacts")
async def read_contacts(skip: int = 0, limit: int = 12):
    query = contacts.select().offset(skip).limit(limit)
    return await database.fetch_all(query)


@app.get("/contacts/count")
async def get_contacts_count():
    query = sqlalchemy.sql.select([sqlalchemy.func.count()]).select_from(contacts)
    total_count = await database.fetch_val(query)
    return {"count": total_count}


@app.get("/contact/{contact_id}", response_class=HTMLResponse)
async def read_contact(request: Request, contact_id: str):
    query = contacts.select().where(contacts.c.id == contact_id)
    contact = await database.fetch_one(query)
    if contact:
        return templates.TemplateResponse(
            "contact_details.html", {"request": request, "contact": contact}
        )
    else:
        raise HTTPException(status_code=404, detail="Contact not found")
