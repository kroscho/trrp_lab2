create_User_table = """
    CREATE TABLE IF NOT EXISTS Users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL, 
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL  
    )
    """

create_Device_table = """
    CREATE TABLE IF NOT EXISTS Device (
    id SERIAL PRIMARY KEY, 
    name TEXT NOT NULL, 
    price INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    typeId INTEGER REFERENCES Type(id),
    brandId INTEGER REFERENCES Brand(id)
    )
    """

create_Brand_table = """
    CREATE TABLE IF NOT EXISTS Brand (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
    )
    """

create_Type_table = """
    CREATE TABLE IF NOT EXISTS Type (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
    )
    """

create_TypeBrand_table = """
    CREATE TABLE IF NOT EXISTS TypeBrand (
    id SERIAL PRIMARY KEY,
    typeId INTEGER REFERENCES Type(id),
    brandId INTEGER REFERENCES Brand(id)
    )
    """

create_DeviceInfo_table = """
    CREATE TABLE IF NOT EXISTS DeviceInfo (
    id SERIAL PRIMARY KEY,
    deviceId INTEGER REFERENCES Device(id),
    title TEXT NOT NULL,
    description TEXT NOT NULL
    )
    """

create_Rating_table = """
    CREATE TABLE IF NOT EXISTS Rating (
    id SERIAL PRIMARY KEY,
    deviceId INTEGER REFERENCES Device(id),
    userId INTEGER REFERENCES Users(id),
    rate INTEGER NOT NULL
    )
    """

create_Basket_table = """
    CREATE TABLE IF NOT EXISTS Basket (
    id SERIAL PRIMARY KEY,
    userId INTEGER REFERENCES Users(id)
    )
    """

create_BasketDevice_table = """
    CREATE TABLE IF NOT EXISTS BasketDevice (
    id SERIAL PRIMARY KEY,
    basketId INTEGER REFERENCES Basket(id),
    deviceId INTEGER REFERENCES Device(id)
    )
    """

def add_user():
    str = "INSERT INTO Users (name, email, password, role) VALUES (%s, %s, %s, %s) RETURNING id;"        
    return str

def check_user():
    str = "SELECT id FROM Users WHERE name=%s AND email=%s AND password=%s AND role=%s;"        
    return str

def add_brand():
    str = "INSERT INTO Brand (name) VALUES (%s) RETURNING id"
    return str

def check_brand():
    str = "SELECT id FROM Brand WHERE name=%s;"        
    return str

def add_type():
    str = "INSERT INTO Type (name) VALUES (%s) RETURNING id"
    return str

def check_type():
    str = "SELECT id FROM Type WHERE name=%s;"       
    return str

def add_device():
    str = "INSERT INTO Device (name, price, rating, typeId, brandId) VALUES (%s, %s, %s, %s, %s) RETURNING id"        
    return str

def check_device():
    str = "SELECT id FROM Device WHERE name=%s AND price=%s AND rating=%s AND typeId=%s AND brandId=%s;"       
    return str

def add_device_info():
    str = "INSERT INTO DeviceInfo (deviceId, title, description) VALUES (%s, %s, %s) RETURNING id"    
    return str

def check_device_info():
    str = "SELECT id FROM DeviceInfo WHERE deviceId=%s AND title=%s AND description=%s;"      
    return str

def add_rating():
    str = "INSERT INTO Rating (deviceId, userId, rate) VALUES (%s, %s, %s) RETURNING id"      
    return str

def check_rating():
    str = "SELECT id FROM Rating WHERE deviceId=%s AND userId=%s AND rate=%s;"        
    return str
    
def add_basketDevice():
    str = "INSERT INTO BasketDevice (deviceId, basketId) VALUES (%s, %s) RETURNING id"       
    return str

def check_basketDevice():
    str = "SELECT id FROM BasketDevice WHERE deviceId=%s AND basketId=%s;"        
    return str

def add_typeBrand():
    str = "INSERT INTO TypeBrand (typeId, brandId) VALUES (%s, %s) RETURNING id"     
    return str

def check_typeBrand():
    str = "SELECT id FROM TypeBrand WHERE typeId=%s AND brandId=%s;"        
    return str

def add_basket():
    str = "INSERT INTO Basket (userId) VALUES (%s) RETURNING id"       
    return str

def check_basket():
    str = "SELECT id FROM Basket WHERE userId=%s;"        
    return str

reset_seq_users = """
    ALTER SEQUENCE users_id_seq RESTART WITH 1
"""

reset_seq_type = """
    ALTER SEQUENCE type_id_seq RESTART WITH 1
"""

reset_seq_brand = """
    ALTER SEQUENCE brand_id_seq RESTART WITH 1
"""

reset_seq_device = """
    ALTER SEQUENCE device_id_seq RESTART WITH 1
"""

reset_seq_deviceInfo = """
    ALTER SEQUENCE deviceInfo_id_seq RESTART WITH 1
"""

reset_seq_rating = """
    ALTER SEQUENCE rating_id_seq RESTART WITH 1
"""

reset_seq_typeBrand = """
    ALTER SEQUENCE TypeBrand_id_seq RESTART WITH 1
"""

reset_seq_basket = """
    ALTER SEQUENCE basket_id_seq RESTART WITH 1
"""

reset_seq_basketDevice = """
    ALTER SEQUENCE basketDevice_id_seq RESTART WITH 1
"""