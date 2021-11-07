create_table = '''
    CREATE TABLE online_store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password text NOT NULL,
    role TEXT NOT NULL,
    device_id INTEGER NOT NULL,
    device_name TEXT NOT NULL,
    price INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    type_name TEXT NOT NULL,
    brand_id INTEGER NOT NULL,
    brand_name TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL
    );'''

delete_table = "DROP TABLE online_store"

def add_str(user_id, name, email, password, role, device_id, device_name, price, rating, type_id, type_name, brand_id, brand_name, title, description):
    str = """
        INSERT INTO online_store (user_id, name, email, password, role, device_id, device_name, price, rating, type_id, type_name, brand_id, brand_name, title, description) 
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (user_id, name, email, password, role, device_id, device_name, price, rating, type_id, type_name, brand_id, brand_name, title, description)
    return str

