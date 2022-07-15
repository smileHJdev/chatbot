from dotenv import load_dotenv
import os
import pymysql


load_dotenv()
HOST = os.environ.get("HOST")
PORT = int(os.environ.get("PORT"))
USER_NAME = os.environ.get("USER_NAME")
PASSWD = os.environ.get("PASSWD")


db = pymysql.connect(
    host=HOST,
    port=PORT,
    user=USER_NAME,
    passwd=PASSWD,
    db='chatbotDB',
    charset='utf8'
)
print("DB 연결 성공")
