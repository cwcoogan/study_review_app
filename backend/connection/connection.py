import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    username=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
    )
print("connected successfully")
cursor = connection.cursor()
query = ("INSERT INTO studyspaces.user (username) VALUES ('grace')")
cursor.execute(query)
connection.commit

query1 = ("SELECT * FROM user;")
cursor.execute(query1)

results = cursor.fetchall()

for result in results:
    print(result)
cursor.close()
connection.close()