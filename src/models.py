from abc import ABC, abstractmethod


class PrintObjectMixin:
    """Миксин для вывода информации о создании объекта."""

    def __init__(self, *args, **kwargs):
        """Инициализация с выводом информации о создании объекта."""
        # Сначала выводим информацию
        class_name = self.__class__.__name__
        str_args = []
        for arg in args:
            if isinstance(arg, str):
                str_args.append(f"'{arg}'")
            else:
                str_args.append(str(arg))
        params = ", ".join(str_args)
        print(f"Создан объект {class_name}({params})")

        # Затем вызываем следующий __init__ в MRO
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        pass

    @abstractmethod
    def __str__(self):
        """Абстрактный метод для строкового представления."""
        pass

    @abstractmethod
    def __add__(self, other):
        """Абстрактный метод для сложения продуктов."""
        pass

    @property
    @abstractmethod
    def price(self):
        """Абстрактный геттер для цены."""
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        """Абстрактный сеттер для цены."""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: dict):
        """Абстрактный класс-метод для создания продукта."""
        pass


class Product(PrintObjectMixin, BaseProduct):
    """Класс для представления товара в интернет-магазине."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        # Вызываем миксин и базовый класс через super()
        super().__init__(name, description, price, quantity)
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    def __str__(self):
        """Строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Магический метод сложения продуктов.

        Возвращает сумму стоимости всех товаров на складе.
        """
        if type(self) is not type(other):  # Исправлено: is not вместо !=
            raise TypeError("Нельзя складывать товары разных типов")

        return (self.price * self.quantity) + (other.price * other.quantity)

    @property
    def price(self):
        """Геттер для цены."""
        return self._price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для цены с проверкой на положительное значение."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = new_price

    @classmethod
    def new_product(cls, product_data: dict):
        """Класс-метод для создания нового продукта из словаря."""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )


class Smartphone(Product):
    """Класс для представления смартфона. Наследуется от класса Product."""

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            efficiency: float,
            model: str,
            memory: int,
            color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        """Строковое представление смартфона."""
        return (
            f"{self.name} {self.model}, {self.price} руб. Остаток: {self.quantity} шт.\n"
            f"Характеристики: {self.memory}ГБ, {self.color}, производительность: {self.efficiency}"
        )


class LawnGrass(Product):
    """Класс для представления газонной травы. Наследуется от класса Product."""

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            country: str,
            germination_period: int,
            color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        """Строковое представление газонной травы."""
        return (
            f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n"
            f"Характеристики: {self.country}, срок прорастания: "
            f"{self.germination_period} дней, цвет: {self.color}"
        )


class BaseEntity(ABC):
    """Абстрактный базовый класс для сущностей с общими свойствами."""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self):
        """Абстрактный метод для строкового представления."""
        pass


class Category(BaseEntity):
    """Класс для представления категории товаров в интернет-магазине."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        super().__init__(name, description)
        self.__products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product):
        """
        Метод для добавления продукта в категорию.

        Проверяет, что добавляемый объект является продуктом или его наследником.
        """
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников"
            )

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для списка продуктов в формате строк."""
        products_str = ""
        for product in self.__products:
            products_str += f"{product}\n"
        return products_str.strip()

    def get_products_list(self):
        """Метод для получения списка объектов продуктов."""
        return self.__products

    def get_total_quantity(self):
        """Метод для получения общего количества товаров в категории."""
        return sum(product.quantity for product in self.__products)


class Order(BaseEntity):
    """Класс для представления заказа."""

    def __init__(self, product: Product, quantity: int):
        super().__init__(f"Заказ {product.name}", f"Заказ товара {product.name}")
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self):
        """Строковое представление заказа."""
        return (
            f"Заказ: {self.product.name}\n"
            f"Количество: {self.quantity}\n"
            f"Итоговая стоимость: {self.total_price} руб."
        )


def load_data_from_json(filename: str = "products.json"):
    """Загружает данные о категориях и товарах из JSON-файла."""
    import json
    from pathlib import Path

    try:
        file_path = Path(filename)
        if not file_path.is_absolute():
            file_path = Path(__file__).parent.parent / filename

        with open(file_path, "r", encoding="utf-8") as file:
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
        for product_data in category_data.get("products", []):
            if "efficiency" in product_data and "model" in product_data:
                product = Smartphone(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=product_data["price"],
                    quantity=product_data["quantity"],
                    efficiency=product_data["efficiency"],
                    model=product_data["model"],
                    memory=product_data["memory"],
                    color=product_data["color"],
                )
            elif "country" in product_data and "germination_period" in product_data:
                product = LawnGrass(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=product_data["price"],
                    quantity=product_data["quantity"],
                    country=product_data["country"],
                    germination_period=product_data["germination_period"],
                    color=product_data["color"],
                )
            else:
                product = Product.new_product(product_data)

            products.append(product)

        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products,
        )
        categories.append(category)

    return categories
