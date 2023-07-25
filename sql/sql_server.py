import pymssql
import os
from dotenv import load_dotenv

load_dotenv()

DB_DRIVER = os.getenv("BD_DRIVER")
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASWORD = os.getenv("DB_PASWORD")

def getTesting():
  return [
    { "msge": "Kartax API v3.0", "swagger": "add '/docs' to the url", "driver": DB_DRIVER}
  ]

# funciones que ejecutan los procedimientos almacenados de SQL Server
async def getData(query):
  try:
    connection = pymssql.connect(DB_HOST, DB_USER, DB_PASWORD, DB_DATABASE)
    cursor = connection.cursor()
    cursor.execute(query)

    result = []
    columns = [column[0] for column in cursor.description]
    for row in  cursor.fetchall():
      result.append(dict(zip(columns, row)))
    
    print("Connection OK")
    return result
  except Exception as ex:
    print("Connection Failed")
    return [ {"ex": str(ex) } ]
