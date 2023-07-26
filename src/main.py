from fastapi import FastAPI
from sql.sql_server import getTesting, getData, setData

from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Kartax", description="API", version="3.0")

# model ---------------------------------
class Registrarse(BaseModel):
  nombres: str
  apellidos: str
  usuario: str
  correo: str
  clave: str

class Usuario(BaseModel):
  id: int
  nombres: str
  apellidos: str
  usuario: str
  correo: str
  fecha: datetime
  is_active: bool

fechaql = datetime.strptime("20230725 15:42:00", "%Y%m%d %H:%M:%S")

usuarios = [
  Usuario(id=1, nombres="Francsico", apellidos="Carmona", usuario="NEFELIN", correo="flcarmonac@yahoo.com", fecha=fechaql, is_active=True),
  Usuario(id=2, nombres="Nicolas", apellidos="Carmona", usuario="KRATOS", correo="kratos@yahoo.com", fecha=fechaql, is_active=True),
  Usuario(id=3, nombres="Michael", apellidos="Carmona", usuario="ZUMO", correo="zumo@yahoo.com", fecha=fechaql, is_active=True),
]

# crud ----------------------------------
@app.get("/")
async def root():
  return getTesting()

@app.get("/usuario-logearse")
async def logearse(usuario: str, clave: str):
  query = "pa_usuario_logearse"
  params = [usuario, clave]
  return await getData(query, params)

@app.post("/usuario-registrarse")
async def registrarse(prop: Registrarse):
  query = "pa_usuario_registrarse"
  params = (prop.nombres, prop.apellidos, prop.usuario, prop.correo, prop.clave,)
  return await setData(query, params)

@app.get("/usuario")
async def get_usuario_all():
  query = "pa_usuario_get_all"
  params = []
  return await getData(query, params)

@app.get("/usuario/{id}")
async def get_usuario_byid(id: int):
  result = list(filter(lambda el: el.id == id, usuarios))
  return result

