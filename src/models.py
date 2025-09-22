class Product:
    """
    Класс для представления товара в интернет-магазине.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """
    Класс для представления категории товаров в интернет-магазине.
    """

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        # Обновляем атрибуты класса
        Category.category_count += 1
        Category.product_count += len(self.products)


def load_data_from_json(filename: str = "products.json"):
    """
    Загружает данные о категориях и товарах из JSON-файла.
    """
    import json
    import os
    from pathlib import Path

    try:
        # Получаем абсолютный путь к файлу
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
            product = Product(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                quantity=product_data['quantity']
            )
            products.append(product)

        category = Category(
            name=category_data['name'],
            description=category_data['description'],
            products=products
        )
        categories.append(category)

    return categories