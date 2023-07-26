import pymssql
import os
from dotenv import load_dotenv

load_dotenv()

DB_DRIVER = os.getenv("BD_DRIVER")
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def getTesting():
  return [
    { "msge": "Kartax API v3.0", "swagger": "add '/docs' to the url", "driver": DB_DRIVER}
  ]

# funciones que ejecutan los procedimientos almacenados de SQL Server
async def getData(query, params):
  try:
    with pymssql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE) as connection:
      with connection.cursor(as_dict=True) as cursor:
        cursor.callproc(query, params)
        result = cursor.fetchall()
        return result
  except Exception as ex:
    return [{"error": str(ex)}]

async def setData(query, params):
  try:
    with pymssql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE) as connection:
      with connection.cursor(as_dict=True) as cursor:
        cursor.callproc(query, params)
        result = cursor.fetchall()
        connection.commit()
        return result
  except Exception as ex:
    return [{"error": str(ex)}]