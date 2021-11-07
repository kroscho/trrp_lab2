import sqlite3
import sqlite_queries
import traceback
import sys

path = 'D:/online-store.db'

def delete_table():
    try:
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()

        sqlite_delete_table_query = sqlite_queries.delete_table
        cursor.execute(sqlite_delete_table_query)
        sqlite_connection.commit()
        print("Таблица удалена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def create_table():
    try:
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()

        sqlite_create_table_query = sqlite_queries.create_table
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        print("Таблица создана")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def add_data_in_table(str):
    try:
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")

        sqlite_insert_query = str
        count = cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        print("Запись успешно вставлена ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Не удалось вставить данные в таблицу sqlite")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def get_data():
    sqlite_connection = sqlite3.connect(path)
    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    
    columns = ['id', 'user_id', 'name', 'email', 'password', 'role', 'device_id', 'device_name', 'price', 'rating', 'type_id', 'type_name', 'brand_id', 'brand_name', 'title', 'description']
    sql = 'SELECT * FROM online_store;'

    cursor.execute(sql)

    data = cursor.fetchall()
    
    for row in data:
        print(row)
        d = {columns[i]: row[i] for i in range(len(row))}
        print(d)

if __name__ == '__main__':
    
    '''
    delete_table()
    create_table()
    
    add_data_in_table(sqlite_queries.add_str(1, 'nikita', 'kros@mail', 123, 'customer', 1, 'Poco x3', 20000, 4, 1, 'Смартфоны', 1, 'Xiaomi', 'Xizami Poco x3', '128 GB'))
    add_data_in_table(sqlite_queries.add_str(1, 'nikita', 'kros@mail', 123, 'customer', 2, 'Poco x3 Pro', 22000, 5, 1, 'Смартфоны', 1, 'Xiaomi', 'Xizami Poco x3', '256 GB'))
    add_data_in_table(sqlite_queries.add_str(2, 'nikolay', 'nik@mail', 12345, 'customer', 3, 'Iphone 11', 50000, 5, 1, 'Смартфоны', 2, 'Apple', 'Apple Iphone 11', '128 GB'))
    add_data_in_table(sqlite_queries.add_str(3, 'maksim', 'maks@mail', 1232, 'customer', 4, 'IdeaPad S145', 35000, 4, 2, 'Ноутбуки', 3, 'Lenovo', 'Lenovo IdeaPad S145', 'black'))
    add_data_in_table(sqlite_queries.add_str(3, 'maksim', 'maks@mail', 1232, 'customer', 5, 'Рюкзак 15.6', 1500, 5, 3, 'Рюкзаки для ноутбуков', 3, 'Lenovo', 'Lenovo Рюкзак 15.6', 'black'))
    add_data_in_table(sqlite_queries.add_str(4, 'ronaldo', 'ron@mail', 12321, 'customer', 1, 'Thin 9SCSR-102', 65000, 5, 2, 'Ноутбуки', 4, 'MSI', 'MSI Thin 9SCSR-102', 'black'))
    '''
    add_data_in_table(sqlite_queries.add_str(6, 'messi', 'mes@mail', 1232, 'customer', 6, 'Huawey P40 Lite', 20000, 5, 1, 'Смартфоны', 5, 'Huawey', 'Huawey P40 Lite', 'blue'))

    get_data()