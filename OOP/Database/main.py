from category import Category

class Supermarket(Category):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

supermarket = Supermarket('Korzinka')

def command():
    print("addCat | removeCat | getCat")
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
        elif comm == 'getCat':
            choose_category()

if __name__ == '__main__':
    start()
    