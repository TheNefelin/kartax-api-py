from sql.sql_server import execute_sp
from fastapi import APIRouter

router = APIRouter(prefix="/negocio", tags=["negocios"])

@router.get("/")
async def get_negocio_all():
  result = await execute_sp("pa_negocio_getall", ())
  return result

