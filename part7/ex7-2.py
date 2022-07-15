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
    # sql문
    sql = '''
    CREATE TABLE tb_student(
        id int primary key auto_increment not null,
        name varchar(32),
        age int,
        address varchar(32)
    ) ENGINT = InnoDB DEFAULT CHARSET = utf8 
    '''

    # 생성
    with db.sursor() as cursor:
        cursor.exute(sql)
# 에러
except Exception as e:
    print(e)
# 생성후 연결 종료
finally:
    if db is not None:
        db.close()
