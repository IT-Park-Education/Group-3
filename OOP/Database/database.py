import psycopg2

DATABASE = 'postgres'
USER = 'postgres'
NAME = 'northwind'
HOST = 'localhost'
PASSWORD = 123
PORT = 5432

def connect():
    conn = psycopg2.connect(database = NAME,
                            user = USER, 
                            host= HOST,
                            password = PASSWORD,
                            port = PORT)
    return conn



def get_fruit():
    conn = connect()
    
    cur = conn.cursor()
    cur.execute("""
            SELECT a, fruit_a
	            FROM public.basket_a;
                """)
    data = cur.fetchall()
    conn.commit()
    conn.close()

    return data

def create_fruit():
    conn = connect()
    
    cur = conn.cursor()
    cur.execute("""
            INSERT INTO basket_a (a, fruit_a)
            VALUES (7, 'Kiwi')
                """)
    conn.commit()
    conn.close()

# create_fruit()
friuts = get_fruit()
for fruit in friuts:
    print(f"| {fruit[0]} | {fruit[1]} |")


