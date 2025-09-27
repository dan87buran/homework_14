class Product:
    """
    Класс для представления товара в интернет-магазине.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    def __str__(self):
        """Строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Магический метод сложения продуктов.
        Возвращает сумму стоимости всех товаров на складе.
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")

        return (self.price * self.quantity) + (other.price * other.quantity)

    @property
    def price(self):
        """Геттер для цены"""
        return self._price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для цены с проверкой на положительное значение"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = new_price

    @classmethod
    def new_product(cls, product_data: dict):
        """
        Класс-метод для создания нового продукта из словаря
        """
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )


class Category:
    """
    Класс для представления категории товаров в интернет-магазине.
    """

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        """Строковое представление категории"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product):
        """
        Метод для добавления продукта в категорию
        """
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    @property
    def products(self):
        """Геттер для списка продуктов в формате строк"""
        products_str = ""
        for product in self.__products:
            products_str += f"{product}\n"  # Используем __str__ продукта
        return products_str.strip()

    def get_products_list(self):
        """Метод для получения списка объектов продуктов"""
        return self.__products

    def get_total_quantity(self):
        """Метод для получения общего количества товаров в категории"""
        return sum(product.quantity for product in self.__products)


def load_data_from_json(filename: str = "products.json"):
    """
    Загружает данные о категориях и товарах из JSON-файла.
    """
    import json
    from pathlib import Path

    try:
        file_path = Path(filename)
        if not file_path.is_absolute():
            file_path = Path(__file__).parent.parent / filename

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка чтения JSON из файла {filename}")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке файла: {e}")
        return []

    categories = []

    for category_data in data:
        products = []
        for product_data in category_data.get('products', []):
            product = Product.new_product(product_data)
            products.append(product)

        category = Category(
            name=category_data['name'],
            description=category_data['description'],
            products=products
        )
        categories.append(category)

    return categories