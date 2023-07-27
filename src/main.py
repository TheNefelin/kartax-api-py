from sql.sql_server import getTesting, execute_sp
from pydantic import BaseModel
from datetime import datetime
from fastapi import FastAPI
from routers import usuarios

app = FastAPI(title="Kartax", description="API", version="3.0")

# routers -----------------------------------------------------------------
app.include_router(usuarios.router)

# modelo ------------------------------------------------------------------
class Registrarse(BaseModel):
  nombres: str
  apellidos: str
  usuario: str
  correo: str
  clave: str

fechaql = datetime.strptime("20230725 15:42:00", "%Y%m%d %H:%M:%S")

# root --------------------------------------------------------------------
@app.get("/")
async def root():
  return await getTesting()

@app.get("/usuario-logearse")
async def logearse(usuario: str, clave: str):
  result = await execute_sp("pa_usuario_logearse", (usuario, clave,))
  return result

@app.post("/usuario-registrarse")
async def registrarse(obj: Registrarse):
  result = await execute_sp("pa_usuario_registrarse", (obj.nombres, obj.apellidos, obj.usuario, obj.correo, obj.clave,))
  return result

