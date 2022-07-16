import pymysql
import openpyxl
from dotenv import load_dotenv
import os

currentPath = os.getcwd()
print('currentPath', currentPath)
load_dotenv()
HOST = os.environ.get("HOST")
PORT = int(os.environ.get("PORT"))
USER_NAME = os.environ.get("USER_NAME")
PASSWD = os.environ.get("PASSWD")


def all_clear_train_data(db):
    sql = '''
        delete from chatbot_train_data
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)

    sql = '''
        ALTER TABLE chatbot_train_data AUTO_INCREMENT=1
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)


def insert_data(db, xls_row):
    intent, ner, query, answer, answer_img_url = xls_row

    sql = '''
        INSERT chatbot_train_data(intent, ner, query, answer, answer_image)
        value(
            '%s', '%s', '%s', '%s', '%s'
        )
    ''' % (intent.value, ner.value, query.value, answer.value, answer_img_url.value)

    sql = sql.replace("'None'", "null")

    with db.cursor() as cursor:
        cursor.execute(sql)
        print('{}저장'.format(query.value))
        db.commit()


print('여기까지 실행')
train_file = 'train_tools/qna/train_data.xlsx'
print(train_file)
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

    # 기존 학습 데이터 초기화
    all_clear_train_data(db)

    # 학습 엑셀 파일 불러오기
    wb = openpyxl.load_workbook(train_file)
    sheet = wb['Sheet1']
    for row in sheet.iter_rows(min_row=2):  # 해더는 불러오지 않음
        # 데이터 저장
        insert_data(db, row)

    wb.close()

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
