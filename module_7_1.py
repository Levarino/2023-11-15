class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = "products.txt"
        file = open(self.__file_name, "a")
        file.close()

    def get_products(self):
        file = open(self.__file_name, "r")
        file_content = file.read()
        file.close()
        return file_content

    def add(self, *products):
        products_file = self.get_products().splitlines()  # Разделяем строки
        file = open(self.__file_name, "a")
        for i in products:
            product_str = f"{i.name}, {i.weight}, {i.category}"
            if product_str not in products_file:
                file.write(f"{product_str}\n")
            else:
                print(f"Продукт {product_str} уже есть в магазине")
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # Вывод: Spaghetti, 3.4, Groceries

s1.add(p1, p2, p3)  # Добавление продуктов

print(s1.get_products())  # Вывод всех продуктов
