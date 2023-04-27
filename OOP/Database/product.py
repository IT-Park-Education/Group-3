import supermarket_db as db

class Product():

    def add_product(self, **kwargs):
        if db.add_product(kwargs) != 0:
            print(f"{kwargs.get('name')} nomli mahsulot qo'shildi!")

    def get_products(category_id):
        print("\nMahsulotlar:\n")
        products = db.get_products(category_id)
        for product in products:
            print(f"id: {product[0]} name: {product[2]} price: {product[3]} discount: {product[4]} time: {product[5]}")

    def get_product(self, id):
        product = db.get_product(id)
        print(f"id: {product[0]} name: {product[2]} price: {product[3]} discount: {product[4]} time: {product[5]}")
        return product[2]
