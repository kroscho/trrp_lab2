import sqlite3

# получаем данные из ненормализованной бд и построчно добавляем в нормализованную бд
def get_data():
    db_file = 'D:/online-store.db'
    sqlite_connection = sqlite3.connect(db_file)
    cursor = sqlite_connection.cursor()
    
    columns = ['id', 'user_id', 'name', 'email', 'password', 'role', 'device_id', 'device_name', 'price', 'rating', 'type_id', 'type_name', 'brand_id', 'brand_name', 'title', 'description']
    sql = 'SELECT * FROM online_store;'

    cursor.execute(sql)

    data = cursor.fetchall()
    result = []
    for row in data:

        d = {columns[i]: row[i] for i in range(len(row))}
        result.append(d)

    return result
        #cr_data = Crypt_data(d)
        #crypto_data, key_des = cr_data.encrypt_data_des(key)
        #cr_key = Crypt_data(key_des)
        #crypto_key, privkey = cr_key.encrypt_key_rsa()
        #print("decr_data: ", cr_data.decrypt_data_des(crypto_data, key_des))
        
        #send_key(k)
        #import_data_to_db(d)