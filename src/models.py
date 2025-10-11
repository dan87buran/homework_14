from abc import ABC, abstractmethod


# Добавим недостающие классы
class ZeroQuantityError(Exception):
    """Пользовательское исключение для товаров с нулевым количеством."""
    pass


class BaseEntity:
    """Базовый класс для сущностей."""
    pass


class LoggingMixin:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args, **kwargs):
        # Вызываем следующий метод в MRO
        super().__init__(*args, **kwargs)
        # Формируем строку для логирования
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f"{key}={value!r}" for key, value in kwargs.items()]
        all_args = ", ".join(args_repr + kwargs_repr)
        # Исправляем вывод согласно тесту
        print(f"Создан объект {self.__class__.__name__}({all_args})")


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов."""

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        pass

    @abstractmethod
    def get_additional_info(self):
        """Возвращает дополнительную информацию о продукте."""
        pass


class Product(LoggingMixin, BaseProduct):
    """Класс продукта с наследованием от миксина и абстрактного класса."""

    def __init__(self, name, description, price, quantity):
        # Проверка на нулевое количество
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        # Вызов миксина должен быть в конце после инициализации атрибутов
        super().__init__(name, description, price, quantity)

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение продуктов с проверкой типа класса."""
        if type(self).__name__ != type(other).__name__:
            raise TypeError("Нельзя складывать товары разных классов")
        return self.price * self.quantity + other.price * other.quantity

    def get_additional_info(self):
        return {"type": "basic_product"}


class Smartphone(Product):
    """Класс смартфона."""

    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
        # Вызов конструктора родительского класса
        super().__init__(name, description, price, quantity)

    def __repr__(self):
        return (f"Smartphone('{self.name}', '{self.description}', {self.price}, {self.quantity}, "
                f"'{self.performance}', '{self.model}', '{self.memory}', '{self.color}')")

    def get_additional_info(self):
        return {
            "performance": self.performance,
            "model": self.model,
            "memory": self.memory,
            "color": self.color
        }


class LawnGrass(Product):
    """Класс газонной травы."""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        # Вызов конструктора родительского класса
        super().__init__(name, description, price, quantity)

    def __repr__(self):
        return (f"LawnGrass('{self.name}', '{self.description}', {self.price}, {self.quantity}, "
                f"'{self.country}', '{self.germination_period}', '{self.color}')")

    def get_additional_info(self):
        return {
            "country": self.country,
            "germination_period": self.germination_period,
            "color": self.color
        }


class Category(BaseEntity):  # Наследуем от BaseEntity
    """Класс категории товаров."""

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

    @property
    def products(self):
        return self.__products

    def get_products_list(self):
        """Метод для получения списка продуктов (для совместимости с тестами)."""
        return self.__products

    def average_price(self):
        """Подсчет среднего ценника всех товаров в категории (для совместимости с тестами)."""
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0

    def middle_price(self):
        """Подсчет среднего ценника всех товаров в категории."""
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)}"


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
            # Проверяем наличие полей для разных типов продуктов
            # Обратите внимание: в JSON поле называется "efficiency", а не "performance"
            has_smartphone_fields = all(field in product_data for field in ["efficiency", "model", "memory", "color"])
            has_lawn_grass_fields = all(field in product_data for field in ["country", "germination_period", "color"])

            if has_smartphone_fields:
                product = Smartphone(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=product_data["price"],
                    quantity=product_data["quantity"],
                    performance=product_data["efficiency"],  # Используем efficiency как performance
                    model=product_data["model"],
                    memory=product_data["memory"],
                    color=product_data["color"],
                )
            elif has_lawn_grass_fields:
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
                product = Product(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=product_data["price"],
                    quantity=product_data["quantity"],
                )
            products.append(product)

        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products
        )
        categories.append(category)

    return categories