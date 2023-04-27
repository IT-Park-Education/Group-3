from connection import connect
import datetime


def check_category(name):
    conn = connect()
    
    cur = conn.cursor()
    cur.execute(f"""
            SELECT name 
                FROM category
                WHERE name = '{name}'
                """)
    data = cur.fetchall()
    conn.commit()
    conn.close()
    if data:
        return True
    return False

def check_product(name):
    conn = connect()
    
    cur = conn.cursor()
    cur.execute(f"""
            SELECT name 
                FROM product
                WHERE name = '{name}'
                """)
    data = cur.fetchall()
    conn.commit()
    conn.close()
    if data:
        return True
    return False

def add_category(name):
    if check_category(name):
        print("Bu kategoriya mavjud!")
        return 0
    conn = connect()
    
    cur = conn.cursor()
    cur.execute(f"""
            INSERT INTO category (name)
            VALUES ('{name}')
                """)
    conn.commit()
    conn.close()

def add_product(data):
    if check_product(data.get('name')):
        print("Bu mahsulot mavjud!")
        return 0
    conn = connect()
    
    cur = conn.cursor()
    if data.get('discount'):
        cur.execute(f"""
                INSERT INTO product (category_id, name, price, discount, created_at)
                VALUES (
                    {data.get('category_id')},
                    '{data.get('name')}',
                    {data.get('price')},
                    {data.get('discount')},
                    '{datetime.datetime.now().strftime("%H:%M %d.%m.%Y")}')
                """)
    else:
        cur.execute(f"""
                INSERT INTO product (category_id, name, price, created_at)
                VALUES (
                    {data.get('category_id')},
                    '{data.get('name')}',
                    {data.get('price')},
                    '{datetime.datetime.now().strftime("%H:%M %d.%m.%Y")}')
                """)
    conn.commit()
    conn.close()
    

def get_categories():
    conn = connect()
    
    cur = conn.cursor()
    cur.execute("""
            SELECT id, name
	            FROM category;
                """)
    data = cur.fetchall()
    conn.commit()
    conn.close()
    return data

def get_category(category_id):
    conn = connect()
    
    cur = conn.cursor()
    cur.execute(f"""
            SELECT *
	            FROM category
                WHERE id = {category_id}
                """)
    data = cur.fetchone()
    conn.commit()
    conn.close()
    return data

def delete_category(category_id):
    conn = connect()
    
    cur = conn.cursor()
    cur.execute(f"""
            DELETE FROM category
                WHERE id = {category_id}
                """)
    conn.commit()
    conn.close()

def get_products(category_id):
    conn = connect()
    
    cur = conn.cursor()
    cur.execute(f"""
            SELECT *
	            FROM product
                WHERE category_id = {category_id}
                """)
    data = cur.fetchall()
    conn.commit()
    conn.close()

    return data

def get_product(product_id):
    conn = connect()
    
    cur = conn.cursor()
    cur.execute(f"""
            SELECT *
	            FROM product
                WHERE id = {product_id}
                """)
    data = cur.fetchone()
    conn.commit()
    conn.close()

    return data
