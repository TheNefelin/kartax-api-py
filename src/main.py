from fastapi import FastAPI
from sql.sql_server import getTesting, getData

app = FastAPI(title="Kartax", description="API", version="3.0")

@app.get("/")
async def root():
  return [
    { "msge": "Kartax API v3.0", "swagger": "add '/docs' to the url"}
  ]

@app.get("/testing")
def testing():
  return getTesting()

@app.get("/negocio")
async def negocio_get_all():
  return await getData("EXECUTE pa_negocio_get_active")

