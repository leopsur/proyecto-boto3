from dotenv import load_dotenv
import os
import boto3
import mysql.connector

load_dotenv()

config = {
       "user": os.getenv("DB_USER"),
       "password": os.getenv("DB_PASSWORD"),
       "host": os.getenv("ENDPOINT")
      
   }
DB_NAME = os.getenv("DB_NAME")
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor(dictionary=True)
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
cursor.execute(f"USE {DB_NAME}")

cursor.execute("SELECT * FROM libros l")
