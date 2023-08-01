from sql.sql_server import getTesting, execute_sp
from pydantic import BaseModel
from datetime import datetime
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.middleware.cors import CORSMiddleware #cors handler class
from fastapi.staticfiles import StaticFiles #img handler class
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from routers import negocios, usuarios

app = FastAPI(title="Kartax", description="API", version="3.0")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="logearse")

# origins = [
#     "http://localhost",
#     "http://localhost:8000",
#     "http://localhost:3000",
# ]
# fechaql = datetime.strptime("20230725 15:42:00", "%Y%m%d %H:%M:%S")

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

# root --------------------------------------------------------------------
@app.post("/logearse")
async def iniciar_sesion(form: OAuth2PasswordRequestForm = Depends()):
  result = await execute_sp("pa_usuario_logearse", (form.username, form.password,))
  estado, msge, sql_token = result[0]['estado'], result[0]['msge'], result[0]['sql_token']

  if not estado:
    raise HTTPException(
      status_code = status.HTTP_401_UNAUTHORIZED, 
      detail = msge,
      headers={"WWW-Authenticate": "Bearer"},)

  return {"access_token": sql_token, "token_type": "bearer", "msge": msge}

@app.post("/test")
async def test(token: str = Depends(oauth2_scheme)):
   print(token)
   return {"msge": "Aguna Wea"}
   

# @app.get("/", tags=["root"])
# async def root():
#   return await getTesting()

# @app.post("/usuario-registrarse", tags=["root"])
# async def registrarse(obj: Registrarse):
#   result = await execute_sp("pa_usuario_registrarse", (obj.nombres, obj.apellidos, obj.usuario, obj.correo, obj.clave,))
#   return result

# routers -----------------------------------------------------------------
app.include_router(negocios.router, dependencies=[Depends(oauth2_scheme)])
app.include_router(usuarios.router)
app.mount("/static", StaticFiles(directory="static"), name="static")
