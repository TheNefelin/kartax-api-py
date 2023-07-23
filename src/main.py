from fastapi import FastAPI

app = FastAPI(title="Kartax", description="API", version="3.0")

@app.get("/")
async def root():
  return [
    { "msge": "Kartax API v3.0", "swagger": "add '/docs' to the url"}
  ]

