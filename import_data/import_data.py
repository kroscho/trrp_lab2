import psycopg2
from enum import Enum
import sys, os.path

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_dir)

from normalized_db_Postgres.config import config
import normalized_db_Postgres.sql_queries as sql_queries

class Action(Enum):
    Insert = 1
    Check = 2

class Import:

    # импорт данных в нормализованную структуру таблиц
    def import_data_to_db(self, data):
        # если нет данных, то обнуляем последовательность
        self.reset_seq_tables()
        
        # Users
        param = (data['name'], data['email'], data['password'], data['role'], )
        id_user, exist_user = self.execute_check(sql_queries.check_user(), param)
        if exist_user:
            id_user = self.execute_insert(sql_queries.add_user(), param)
        
        # Brand
        param = (data['brand_name'], )
        id_brand, exist_brand = self.execute_check(sql_queries.check_brand(), param)
        if exist_brand:    
            id_brand = self.execute_insert(sql_queries.add_brand(), param)
        
        # Type
        param = (data['type_name'], )
        id_type, exist_type = self.execute_check(sql_queries.check_type(), param)
        if exist_type:
            id_type = self.execute_insert(sql_queries.add_type(), param)

        # Device
        param = (data['device_name'], data['price'], data['rating'], id_type, id_brand, )
        id_device, exist_device = self.execute_check(sql_queries.check_device(), param)
        if exist_device:
            id_device = self.execute_insert(sql_queries.add_device(), param)
        
        # DeviceInfo
        param = (id_device, data['title'], data['description'], )
        id_deviceInfo, exist_deviceInfo = self.execute_check(sql_queries.check_device_info(), param)
        if exist_deviceInfo:
            id_deviceInfo = self.execute_insert(sql_queries.add_device_info(), param)
        
        # Rating
        param = (id_device, id_user, data['rating'], )
        id_rating, exist_rating = self.execute_check(sql_queries.check_rating(), param)
        if exist_rating:
            id_rating = self.execute_insert(sql_queries.add_rating(), param)
        
        # Basket
        param = (id_user, )
        id_basket, exist_basket = self.execute_check(sql_queries.check_basket(), param)
        if exist_basket:
            id_basket = self.execute_insert(sql_queries.add_basket(), param)

        # BasketDevice
        param = (id_device, id_basket, )
        id_basketDev, exist_basketDev = self.execute_check(sql_queries.check_basketDevice(), param)
        if exist_basketDev:
            id_basketDev = self.execute_insert(sql_queries.add_basketDevice(), param)

        # TypeBrand
        param = (id_type, id_brand, )
        id_typeBrand, exist_typeBrand = self.execute_check(sql_queries.check_typeBrand(), param)
        if exist_typeBrand:
            id_typeBrand = self.execute_insert(sql_queries.add_typeBrand(), param)
        
        print("Импорт данных прошел успешно!")
        

    # выполнение запроса
    def execute_insert(self, sql, data):
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql, data)
            id = cur.fetchone()[0]
            cur.close()
            conn.commit()
            return id
            
        except (Exception, psycopg2.DatabaseError) as error:
            print("Ошибка: ", error)
        finally:
            if conn is not None:
                conn.close()

    # выполнение запроса
    def execute_check(self, sql, data):
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql, data)
            data = cur.fetchone()
        
            if data == [] or data == None:
                cur.close()
                print("Не найдено")
                return -1, True
            else:
                cur.close()
                #print("Найдено")
                return data[0], False 
        
        except (Exception, psycopg2.DatabaseError) as error:
            print("Ошибка: ", error)
        finally:
            if conn is not None:
                conn.close()


    # сбрасываем последовательность, чтобы начиналось с 1
    def reset_seq_tables(self):
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute('SELECT email FROM Users;')
            data = cur.fetchall()
            if data == []:
                cur.execute(sql_queries.reset_seq_users)
                cur.execute(sql_queries.reset_seq_basket)
                cur.execute(sql_queries.reset_seq_basketDevice)
                cur.execute(sql_queries.reset_seq_brand)
                cur.execute(sql_queries.reset_seq_device)
                cur.execute(sql_queries.reset_seq_rating)
                cur.execute(sql_queries.reset_seq_type)
                cur.execute(sql_queries.reset_seq_typeBrand)
                cur.execute(sql_queries.reset_seq_deviceInfo)
            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Ошибка: ", error)
        finally:
            if conn is not None:
                conn.close()