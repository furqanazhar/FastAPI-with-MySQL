import json
from fastapi import APIRouter, status, Request
from fastapi.responses import JSONResponse
from common.utils import convert_response_to_json
from database.db_helper import Database
import requests

router = APIRouter()
db = Database()
customer_table = 'Customers'


@router.post('/customers', response_description='Create database and populate customer data')
async def populate_customer_data(limit: int):
    try:
        session = requests.Session()
        session.auth = ("mifos", "password")
        data = {}
        url = f"https://demo.mifos.io/fineract-provider/api/v1/clients?limit={limit}&offset=0"
        response = session.get(url)
        response_code = int(response.status_code)
        response = response.json()
        print('response_code', response_code)
        print('response', response)
        #data = await db.insert_row(customer_table, response)
        payload = {
            'message': 'Successfully created resource',
            'data': convert_response_to_json(data)
        }
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=payload)
    except Exception as ex:
        payload = {
            'message': 'Failed to create resource',
            'error': convert_response_to_json(ex)
        }
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=payload)


@router.get('/customers', response_description='Get all customers')
async def get_all_customers():
    try:
        data = await db.get_all_rows(customer_table)
        payload = {
            'message': 'Successfully retrieved resource',
            'data': convert_response_to_json(data)
        }
        return JSONResponse(status_code=status.HTTP_200_OK, content=payload)
    except Exception as ex:
        payload = {
            'message': 'Failed to retrieve resource',
            'error': convert_response_to_json(ex)
        }
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=payload)


@router.get('/customers/{customerId}', response_description='Get specific customer by id')
async def get_customer_by_id(customer_id: str):
    try:
        data = await db.get_row_by_id(customer_table, customer_id)
        payload = {
            'message': 'Successfully retrieved resource',
            'data': convert_response_to_json(data)
        }
        return JSONResponse(status_code=status.HTTP_200_OK, content=payload)
    except Exception as ex:
        payload = {
            'message': 'Failed to retrieve resource',
            'error': convert_response_to_json(ex)
        }
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=payload)
