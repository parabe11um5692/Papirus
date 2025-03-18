import pymysql
import pymysql.cursors
def connection_to_book():
    """Подключение к базе данных с записями о книгах"""
    try:
        connection_to_data_base_book = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            password = 'sawa5692',
            database= 'library',
            cursorclass= pymysql.cursors.DictCursor
    )
        return connection_to_data_base_book
    except Exception as ex:
        print('Went wrong')
        print(ex)
        return None
    