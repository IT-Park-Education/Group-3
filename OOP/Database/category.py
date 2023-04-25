import supermarket_db as db

class Category():
    def __init__(self,name):
        self.name = name

    def add_category(self, name: str):
        if db.add_category(name) != 0:
            print(f"{name} nomli categoriya qo'shildi!")

    def get_category(self, id):
        category = db.get_category(id)
        print(f"id: {category[0]} name: {category[1]}")

    def get_product(self, id):
        product = db.get_product(id)
        print(f"id: {product[0]} name: {product[1]}")

        return product[1]

    def get_categories(self):
        categories = db.get_categories()
        for category in categories:
            print(f"id: {category[0]} name: {category[1]}")

    def get_products(self, category_id):
        products = db.get_products(category_id)
        for product in products:
            print(f"id: {product[0]}|name: {product[2]}|price: {product[3]}|discount: {product[4]}")

    def delete_category(self, id):
        name = self.get_category(id)
        if not self.verify():
            print(f"{name} nomli categoriya o'chirish bekor qilindi!")
            return
        db.delete_category(id)
        print(f"{name} nomli categoriya o'chirildi!")
        

    def verify(self):
        confirm_data = input("""O'chirishmoqchimisiz?\n
                             Xa: Ixtiyoriy so'zni yuboring\n
                             Yo'q: 0""")
        if confirm_data=='0':
            return False
        return True

    def __str__(self):
        return self.name