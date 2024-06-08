from fastapi import APIRouter
from src.api.v1.operations import *
from src.schemas.v1.schemas import Operation

router = APIRouter()

@router.post('/sum')
async def sum_values(request: Operation):
    try:
        return {'result': add(request.a, request.b)}
    except Exception as e:
        return {'result': str(e)}

@router.post('/subtract')
async def subtract_values(request: Operation):
    try:
        return {'result': subtract(request.a, request.b)}
    except Exception as e:
        return {'result': str(e)}
    
@router.post('/multiply')
async def multiply_values(request: Operation):
    try:
        return {'result': multiply(request.a, request.b)}
    except Exception as e:
        return {'result': str(e)}

@router.post('/divide')
async def divide_values(request: Operation):
    try:
        return {'result': divide(request.a, request.b)}
    except Exception as e:
        return {'result': str(e)}
