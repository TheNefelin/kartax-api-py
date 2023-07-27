from sql.sql_server import getTesting, execute_sp, execute_query
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Kartax", description="API", version="3.0")

# model -------------------------------------------------------------------
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

# usuarios = [
#   Usuario(id=1, nombres="Francsico", apellidos="Carmona", usuario="NEFELIN", correo="flcarmonac@yahoo.com", fecha=fechaql, is_active=True),
#   Usuario(id=2, nombres="Nicolas", apellidos="Carmona", usuario="KRATOS", correo="kratos@yahoo.com", fecha=fechaql, is_active=True),
#   Usuario(id=3, nombres="Michael", apellidos="Carmona", usuario="ZUMO", correo="zumo@yahoo.com", fecha=fechaql, is_active=True),
# ]

# root --------------------------------------------------------------------
@app.get("/")
async def root():
  return await getTesting();

@app.get("/usuario-logearse")
async def logearse(usuario: str, clave: str):
  query = "pa_usuario_logearse"
  params = (usuario, clave,)
  return await execute_sp(query, params)

@app.post("/usuario-registrarse")
async def registrarse(obj: Registrarse):
  query = "pa_usuario_registrarse"
  params = (obj.nombres, obj.apellidos, obj.usuario, obj.correo, obj.clave,)
  return await execute_sp(query, params)

# crud --------------------------------------------------------------------
#@app.get("/usuario")
#async def get_usuario_all():
#  query = "pa_usuario_get_all"
#  params = ()
#  return await getData(query, params)

#@app.get("/usuario/{id}")
#async def get_usuario_byid(id: int):
#  return ""

#@app.post("/usuario")
#async def post_usuario_byid(props: Usuario):
#  return Usuario

#@app.put("/usuario")
#async def put_usuario_byid(props: Usuario):
#  return Usuario

#@app.delete("/usuario/{id}")
#async def del_usuario_byid(id: int):
#  return Usuario
