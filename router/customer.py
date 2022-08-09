import json
from fastapi import APIRouter, status, Request
from fastapi.responses import JSONResponse
from common.utils import convert_response_to_json
from database.db_helper import Database
from model.customer import Customer
import requests
import traceback

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

        if response_code != 200:
            payload = {
                'message': 'Failed to invoke API',
                'error': convert_response_to_json(response)
            }
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=payload)
        else:
            totalRecords = response["totalFilteredRecords"]
            recordsList = response["pageItems"]

            print('Total Customers : ', totalRecords)
            customerList:Customer = []
            clientID = fullName = mobileNo = officeName = statusValue = None

            for i in range(len(recordsList)):
                try:
                    clientID = recordsList[i].get('id','N/A')
                    fullName = recordsList[i].get('fullname','N/A')
                    mobileNo = recordsList[i].get('mobileNo','N/A')
                    officeName = recordsList[i].get('officeName','N/A')
                    statusValue = recordsList[i].get('status','N/A').get('value','N/A')
                except Exception:
                    print('error', traceback.format_exc())
                finally:
                    if clientID != 'N/A' and mobileNo != 'N/A':
                        customerList.append([clientID, fullName, mobileNo, officeName, statusValue])
                        print('Record added')
                    else:
                        print('Record not inserted because mobileNo/clientID is not available')
            await db.insert_row(customerList)

            payload = {
                'message': 'Successfully created resource',
                'data': convert_response_to_json(data)
            }
            return JSONResponse(status_code=status.HTTP_201_CREATED, content=payload)
    except Exception as ex:
        payload = {
            'message': 'Failed to create resource',
            'error': traceback.print_tb(ex.__traceback__)
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
            'error': traceback.print_tb(ex.__traceback__)
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
            'error': traceback.print_tb(ex.__traceback__)
        }
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=payload)
