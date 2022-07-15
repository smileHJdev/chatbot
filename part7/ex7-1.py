import pymysql

db = pymysql.connect(

    db='chatbotDB',
    charset='utf8'
)
print("DB 연결 성공")
