from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
  cnx = mysql.connector.connect(
    host = os.getenv("MYSQL_HOST"),
    user = os.getenv("MYSQL_username"),
    database = os.getenv("MYSQL_DATABASE")
  )
  return cnx

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

@app.get('/ref_division')
def  get_ref_division():
  cnx = get_db_connection()
  cursor = cnx.cursor()
  query = "SELECT * FROM ref_division"
  cursor.execute(query)
  rows = cursor.fetchall()
  cursor.close()
  cnx.close()
  return[dict(zip(cursor.column_names, row)) for row in rows]
