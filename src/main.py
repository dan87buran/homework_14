import json


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    total_categories = 1
    total_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        Category.total_categories += 1
        Category.total_products += len(products)


def load_data_from_json(file_path: str) -> list:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []
    for category_data in data:
        products = []
        for product_data in category_data["products"]:
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
            products=products,
        )
        categories.append(category)

    return categories


if __name__ == "__main__":
    # Сбрасываем счетчики для чистоты демонстрации
    Category.total_categories = 0
    Category.total_products = 0

    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print("Информация о продуктах:")
    print(product1.name)
    print(product1.description)
    print(f"Цена: {product1.price} руб.")
    print(f"Количество: {product1.quantity} шт.")
    print()

    print(product2.name)
    print(product2.description)
    print(f"Цена: {product2.price} руб.")
    print(f"Количество: {product2.quantity} шт.")
    print()

    print(product3.name)
    print(product3.description)
    print(f"Цена: {product3.price} руб.")
    print(f"Количество: {product3.quantity} шт.")
    print("\n" + "=" * 50 + "\n")

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print("Информация о категории 1:")
    print(f"Название: {category1.name}")
    print(f"Описание: {category1.description}")
    print(f"Количество продуктов в категории: {len(category1.products)}")
    print(f"Общее количество категорий: {Category.total_categories}")
    print(f"Общее количество продуктов: {Category.total_products}")
    print("\n" + "=" * 50 + "\n")

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print("Информация о категории 2:")
    print(f"Название: {category2.name}")
    print(f"Описание: {category2.description}")
    print(f"Количество продуктов в категории: {len(category2.products)}")
    print(f"Продукты в категории: {[p.name for p in category2.products]}")
    print("\n" + "=" * 50 + "\n")

    print("Итоговые счетчики:")
    print(f"Всего категорий: {Category.total_categories}")
    print(f"Всего продуктов: {Category.total_products}")
