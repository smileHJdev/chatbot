from dotenv import load_dotenv
import os
import pymysql
import pandas as pd


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

    students = [
        {'name': 'Kei', 'age': 36, 'address': 'PUSAN'},
        {'name': 'Tony', 'age': 34, 'address': 'PUSAN'},
        {'name': 'Jeayoo', 'age': 39, 'address': 'GWANGJU'},
        {'name': 'Grace', 'age': 28, 'address': 'SEOUL'},
        {'name': 'Jenny', 'age': 27, 'address': 'SEOUL'},
    ]
    for s in students:
        with db.cursor() as cursor:
            sql = '''
                insert tb_student(name, age, address) values("%s",%d,"%s")
            ''' % (s['name'], s['age'], s['address'])
            cursor.execute(sql)
    db.commit()

    # 30대 학생만 조회
    cond_age = 30
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = ''' 
        select * from tb_student where age > %d
        ''' % cond_age
        cursor.execute(sql)
        results = cursor.fetchall()
    print(results)

    # 이름 검색
    cond_name = 'Grace'
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = ''' 
        select * from tb_student where name="%s"
        ''' % cond_name
        cursor.execute(sql)
        result = cursor.fetchone()
    print(result['name'], result['age'])

    df = pd.DataFrame(results)
    print(df)

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
