from fastapi import FastAPI
from pydantic import BaseModel

from . import schemas, models
from .routers import holding, user
from .database import get_db, engine

import psycopg2
from psycopg2.extras import RealDictCursor

import time


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='freefinance', user='postgres', password='cP2hhyp3qpc', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull!")
#         break
#     except Exception as e:
#         print("Connection to database failed: ")
#         print(f"Error: {e}")
#         time.sleep(2)



app.include_router(holding.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/holders")
def get_holders():
    # retrieve data from database
    # sort data based on holder amount
    # list top 10 companies
    return


    
