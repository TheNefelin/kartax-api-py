from sql.sql_server import getTesting, execute_sp
from pydantic import BaseModel
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import usuarios

app = FastAPI(title="Kartax", description="API", version="3.0")

# origins = [
#     "http://localhost",
#     "http://localhost:8000",
#     "http://localhost:3000",
# ]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# modelo ------------------------------------------------------------------
class Registrarse(BaseModel):
  nombres: str
  apellidos: str
  usuario: str
  correo: str
  clave: str

class Logearse(BaseModel):
  usuario: str
  clave: str

fechaql = datetime.strptime("20230725 15:42:00", "%Y%m%d %H:%M:%S")

# root --------------------------------------------------------------------
@app.get("/", tags=["root"])
async def root():
  return await getTesting()

@app.post("/usuario-registrarse", tags=["root"])
async def registrarse(obj: Registrarse):
  result = await execute_sp("pa_usuario_registrarse", (obj.nombres, obj.apellidos, obj.usuario, obj.correo, obj.clave,))
  return result

@app.post("/usuario-logearse", tags=["root"])
async def logearse(obj: Logearse):
  result = await execute_sp("pa_usuario_logearse", (obj.usuario, obj.clave,))
  return result

# routers -----------------------------------------------------------------
app.include_router(usuarios.router)