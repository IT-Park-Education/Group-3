from product import Product
from category import Category

class Supermarket(Category, Product):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

supermarket = Supermarket('Korzinka')

def command():
    print("addCat | getCat| remCat")
    print("addPro | getPro| remPro")
    command = input("Buyruqlardan birini tanlang:")
    return command

def choose_product():
    product_id = int(input("Mahsulotlardan birini tanlang:"))
    product = supermarket.get_product(product_id) # Qilish kerak
    print(f"{product} ni tanladingiz")

def choose_category():
    supermarket.get_categories()
    category_id = int(input("Kategoriya birini tanlang:"))
    category = supermarket.get_category(category_id)
    print(f"{category} ni tanladingiz\n{category}ga tegishli mahsulotlar\n")
    supermarket.get_products(category_id)
    choose_product()

def start():
    print("Assalom alaykum. Xush kelibsiz!!!")
    while True:
        comm = command()
        if comm=='exit':
            break
        elif comm == 'addCat':
            new_cat = input("Yangi kategoriya nomini kiring:")
            supermarket.add_category(new_cat)
        elif comm == 'remCat':
            supermarket.get_categories()
            category_id = int(input("Kategoriya birini tanlang:"))
            supermarket.delete_category(category_id)
        elif comm == 'getCat':
            choose_category()
        # Product part
        elif comm == 'addPro':
            supermarket.get_categories()
            category_id = int(input("Kategoriya birini tanlang:"))
            print("Quyidagi formani to'ldiring:")
            name = input("Nomi:")
            price = int(input("Narxi:"))
            discount = input("Chegirma(1-100)(%):")

            while True:
                print(discount.isdecimal())
                print(discount.isnumeric())
                print(discount.isdigit())
                if discount.isnumeric():
                    discount = int(discount)
                    break
                elif discount == '':
                    discount = None
                    break
                discount = input("Chegirma(1-100)(%):")
            supermarket.add_product(category_id=category_id,
                                    name=name,
                                    price=price,
                                    discount=discount)
        elif comm == 'getPro':
            supermarket.get_categories()
            category_id = int(input("Kategoriya birini tanlang:"))
            supermarket.get_products(category_id)

if __name__ == '__main__':
    start()
    