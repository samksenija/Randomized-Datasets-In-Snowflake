import snowflake.connector
from snowflake.snowpark import Session
import os

from dotenv import load_dotenv

load_dotenv() 

#Cursor
conn = snowflake.connector.connect(
    user=os.getenv("user"),
    password=os.getenv("password"),
    account=os.getenv("account"),
    warehouse=os.getenv("warehouse"),
    database=os.getenv("database"),
    schema=os.getenv("schema")
)

#Snowpark
connection_parameters = {
  "account": os.getenv("account"),
  "user": os.getenv("user"),
  "password": os.getenv("password"),
  "role": os.getenv("role"),
  "warehouse": os.getenv("warehouse"),  
  "database": os.getenv("database"),  
  "schema": os.getenv("schema"),  
}

new_session = Session.builder.configs(connection_parameters).create()