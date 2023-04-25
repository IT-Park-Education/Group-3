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

def add_product(category_id, product_name, product_price, product_discount=None):
    conn = connect()
    
    cur = conn.cursor()
    cur.execute(f"""
            INSERT INTO product (category_id, name, price, discount, created_at)
            VALUES ({category_id}, '{product_name}',
            {product_price}, {product_discount}, {datetime.datetime.now()})
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
