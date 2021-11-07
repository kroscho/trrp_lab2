import psycopg2
import os, sys

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_dir)
print(path_dir)

from normalized_db_Postgres.config import config
import normalized_db_Postgres.sql_queries as sql_queries

def execute_query(query):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка: ", error)
    finally:
        if conn is not None:
            conn.close()


def create_tables():
    
    execute_query(sql_queries.create_User_table)
    execute_query(sql_queries.create_Brand_table)
    execute_query(sql_queries.create_Type_table)
    execute_query(sql_queries.create_Device_table)
    execute_query(sql_queries.create_DeviceInfo_table)
    execute_query(sql_queries.create_Rating_table)
    execute_query(sql_queries.create_Basket_table)
    execute_query(sql_queries.create_BasketDevice_table)
    execute_query(sql_queries.create_TypeBrand_table)
    print("Таблицы добавлены")
    
'''   
if __name__ == '__main__':
    create_tables()
'''