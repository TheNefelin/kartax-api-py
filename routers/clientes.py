from sql.sql_server import execute_sp
from fastapi import APIRouter

router = APIRouter(prefix="/cliente", tags=["clientes"])

@router.get("/")
async def get_negocio_all():
  result = await execute_sp("pa_negocio_getall", ())
  return result

