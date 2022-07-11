from fastapi import FastAPI
from router import customer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_ROUTE = '/customer/v1'

app.include_router(
    router=customer.router,
    prefix=f'{API_ROUTE}',
    tags=['customers']
)
