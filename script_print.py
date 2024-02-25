import xmlrpc.client
import json


url = "https://chift.odoo.com"
db = "chift"
username = "chahid.lorenzo@protonmail.com"
password = "hsp507Royco"


common = xmlrpc.client.ServerProxy("{}/xmlrpc/2/common".format(url))
uid = common.authenticate(db, username, password, {})


if uid is False:
    raise Exception("Échec de l'authentification, mauvais identifiants")

models = xmlrpc.client.ServerProxy("{}/xmlrpc/2/object".format(url))


fields = models.execute_kw(
    db,
    uid,
    password,
    "res.partner",
    "fields_get",
    [],
    {"attributes": ["string", "type", "help"]},
)


for field, attrs in fields.items():
    print(f"Champ: {field}")
    print(f"Description: {attrs.get('string', '')}")
    print(f"Type: {attrs.get('type', '')}")
    print(f"Aide: {attrs.get('help', '')}\n")

contacts = models.execute_kw(
    db,
    uid,
    password,
    "res.partner",
    "search_read",
    [[]],
    {"fields": ["name", "email", "phone"]},
)


with open("contacts.json", "w") as json_file:
    json.dump(contacts, json_file, indent=4)
