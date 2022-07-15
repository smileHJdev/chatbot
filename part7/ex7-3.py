from dotenv import load_dotenv
import os
import pymysql


load_dotenv()
HOST = os.environ.get("HOST")
PORT = int(os.environ.get("PORT"))
USER_NAME = os.environ.get("USER_NAME")
PASSWD = os.environ.get("PASSWD")

db = None
try:
    db = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER_NAME,
        passwd=PASSWD,
        db='chatbotDB',
        charset='utf8'
    )
    sql = '''
        INSERT tb_student(name, age, address) values('Kei', 35, 'Korea')
    '''

    with db.cursor() as cursor:
        cursor.execute(sql)
        db.commit()
except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
