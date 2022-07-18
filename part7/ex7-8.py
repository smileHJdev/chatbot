import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from config.DatabaseConfig import *
import pymysql


import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# load_dotenv()
# HOST = os.environ.get("HOST")
# PORT = int(os.environ.get("PORT"))
# USER_NAME = os.environ.get("USER_NAME")
# PASSWD = os.environ.get("PASSWD")

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
        CREATE TABLE IF NOT EXISTS `chatbot_train_data` (
        `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
        `intent` VARCHAR(45) NULL,
        `ner` VARCHAR(1024) NULL,
        `query` TEXT NULL,
        `answer` TEXT NOT NULL,
        `answer_image` VARCHAR(2048) NULL,
        PRIMARY KEY (`id`)
        ) 
        ENGINE = InnoDB DEFAULT CHARSET=utf8
    '''

    with db.cursor() as cursor:
        cursor.execute(sql)
except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
