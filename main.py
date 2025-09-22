from src.models import Product, Category, load_data_from_json


def demonstrate_classes():
    """Демонстрация работы классов Product и Category"""
    print("=== Демонстрация создания товаров и категорий ===\n")

    # Создание товаров
    phone = Product(
        name="iPhone 15",
        description="Смартфон Apple",
        price=99990.0,
        quantity=5
    )

    laptop = Product(
        name="MacBook Pro",
        description="Ноутбук Apple",
        price=199990.0,
        quantity=3
    )

    # Создание категории
    electronics = Category(
        name="Электроника",
        description="Техника Apple",
        products=[phone, laptop]
    )

    # Вывод информации
    print(f"Категория: {electronics.name}")
    print(f"Описание: {electronics.description}")
    print(f"Количество товаров в категории: {len(electronics.products)}")
    print(f"Общее количество категорий: {Category.category_count}")
    print(f"Общее количество товаров: {Category.product_count}")

    print("\nТовары в категории:")
    for i, product in enumerate(electronics.products, 1):
        print(f"{i}. {product.name} - {product.price} руб. (в наличии: {product.quantity} шт.)")


def demonstrate_json_loading():
    """Демонстрация загрузки данных из JSON"""
    print("\n=== Демонстрация загрузки из JSON ===\n")

    categories = load_data_from_json("products.json")

    if not categories:
        print("Не удалось загрузить данные из JSON файла")
        return

    print(f"Загружено категорий: {len(categories)}")
    print(f"Общее количество товаров: {Category.product_count}\n")

    for category in categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Товаров: {len(category.products)}")

        for product in category.products:
            print(f"  - {product.name}: {product.price} руб. ({product.quantity} шт.)")
        print()


if __name__ == "__main__":
    demonstrate_classes()
    demonstrate_json_loading()