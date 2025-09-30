from src.models import Product, Smartphone, LawnGrass, Category, load_data_from_json
from pathlib import Path


def demonstrate_inheritance():
    """Демонстрация классов-наследников"""
    print("=== Демонстрация классов-наследников ===\n")

    # Создание смартфона
    smartphone = Smartphone(
        name="iPhone 15 Pro",
        description="Флагманский смартфон Apple",
        price=129990.0,
        quantity=8,
        efficiency=3.5,
        model="15 Pro",
        memory=512,
        color="титан"
    )

    print("Смартфон:")
    print(smartphone)
    print(f"\nТип: {type(smartphone)}")
    print(f"Является ли Product: {isinstance(smartphone, Product)}")

    # Создание газонной травы
    lawn_grass = LawnGrass(
        name="Газонная трава Премиум",
        description="Высококачественная газонная трава",
        price=2500.0,
        quantity=50,
        country="Германия",
        germination_period=12,
        color="изумрудный"
    )

    print("\n" + "=" * 50)
    print("Газонная трава:")
    print(lawn_grass)
    print(f"\nТип: {type(lawn_grass)}")
    print(f"Является ли Product: {isinstance(lawn_grass, Product)}")


def demonstrate_addition_restrictions():
    """Демонстрация ограничений сложения"""
    print("\n=== Демонстрация ограничений сложения ===\n")

    # Создание товаров одного типа
    smartphone1 = Smartphone("Смартфон1", "Описание", 50000.0, 3, 2.5, "Модель1", 128, "черный")
    smartphone2 = Smartphone("Смартфон2", "Описание", 70000.0, 2, 3.0, "Модель2", 256, "белый")

    print("Сложение смартфонов:")
    total_value = smartphone1 + smartphone2
    print(f"Суммарная стоимость: {total_value} руб.")

    # Создание товаров разных типов
    lawn_grass = LawnGrass("Трава", "Описание", 1500.0, 10, "Россия", 14, "зеленый")

    print("\nПопытка сложить смартфон и газонную траву:")
    try:
        smartphone1 + lawn_grass
    except TypeError as e:
        print(f"Ошибка: {e}")


def demonstrate_category_restrictions():
    """Демонстрация ограничений добавления в категорию"""
    print("\n=== Демонстрация ограничений добавления в категорию ===\n")

    category = Category("Электроника", "Гаджеты и устройства")

    # Успешное добавление продукта
    smartphone = Smartphone("Смартфон", "Описание", 50000.0, 2, 2.5, "Модель", 128, "черный")
    category.add_product(smartphone)
    print("✓ Смартфон успешно добавлен в категорию")

    # Попытка добавления неверного типа
    print("\nПопытка добавить строку в категорию:")
    try:
        category.add_product("не продукт")
    except TypeError as e:
        print(f"Ошибка: {e}")

    # Попытка добавления словаря
    print("\nПопытка добавить словарь в категорию:")
    try:
        category.add_product({"name": "тест", "price": 100})
    except TypeError as e:
        print(f"Ошибка: {e}")


def demonstrate_all_features():
    """Демонстрация всех новых функций"""
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ КЛАССОВ-НАСЛЕДНИКОВ И ОГРАНИЧЕНИЙ")
    print("=" * 60)

    demonstrate_inheritance()
    demonstrate_addition_restrictions()
    demonstrate_category_restrictions()


if __name__ == "__main__":
    demonstrate_all_features()