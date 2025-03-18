import pymysql
import pymysql.cursors
def connection_reg():
    """Подключение к базе данных с записями о регистрации"""
    try:
        global connection_to_data_base_reg
        connection_to_data_base_reg = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            password = 'sawa5692',
            database= 'reg',
            cursorclass= pymysql.cursors.DictCursor
    )
    except Exception as ex:
        print('Went wrong')
        print(ex)
