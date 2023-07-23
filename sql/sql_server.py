import pypyodbc
import os
from dotenv import load_dotenv

load_dotenv()

DB_DRIVER = os.getenv("BD_DRIVER")
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASWORD = os.getenv("DB_PASWORD")
DB_PATH = "DRIVER={" + DB_DRIVER + "};SERVER=" + DB_HOST + ";DATABASE=" + DB_DATABASE + ";UID=" + DB_USER + ";PWD=" + DB_PASWORD

def getTesting():
  return [
    { "driver": DB_DRIVER }
  ]

# funciones que ejecutan los procedimientos almacenados de SQL Server
async def getData(query):
  try:
    connection = pypyodbc.connect(DB_PATH)
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
