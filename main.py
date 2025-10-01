from src.models import Product, Smartphone, LawnGrass, Category


def main():
    """Основная функция для демонстрации работы классов."""
    # Создание продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Черный цвет, 200MP камера", 180000, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000, 8)

    # Создание смартфонов
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Черный цвет, 200MP камера",
        180000,
        5,
        "Высокая",
        "S23 Ultra",
        256,
        "черный",
    )
    smartphone2 = Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000,
        8,
        "Высокая",
        "15",
        512,
        "серый",
    )

    # Создание газонной травы
    lawn_grass1 = LawnGrass(
        "Газонная трава",
        "Высококачественная трава",
        5000,
        10,
        "Россия",
        14,
        "зеленый",
    )
    lawn_grass2 = LawnGrass(
        "Газонная трава Премиум",
        "Премиум трава",
        7500,
        15,
        "Германия",
        7,
        "темно-зеленый",
    )

    # Создание категорий
    category1 = Category(
        "Смартфоны",
        "Мобильные устройства",
        [smartphone1, smartphone2],
    )
    category2 = Category(
        "Трава газонная",
        "Газонная трава для сада",
        [lawn_grass1, lawn_grass2],
    )

    # Демонстрация строкового представления
    print("Категории:")
    print(category1)
    print(category2)
    print()

    print("Продукты в категории Смартфоны:")
    print(category1.products)
    print()

    print("Продукты в категории Трава газонная:")
    print(category2.products)
    print()

    # Демонстрация сложения продуктов
    print("Сложение продуктов:")
    try:
        total = smartphone1 + smartphone2
        print(f"Общая стоимость смартфонов: {total}")
    except TypeError as e:
        print(f"Ошибка: {e}")

    try:
        total = lawn_grass1 + lawn_grass2
        print(f"Общая стоимость газонной травы: {total}")
    except TypeError as e:
        print(f"Ошибка: {e}")

    # Демонстрация ошибки при сложении разных типов
    print("\nПопытка сложить смартфон и газонную траву:")
    try:
        total = smartphone1 + lawn_grass1
        print(f"Общая стоимость: {total}")
    except TypeError as e:
        print(f"Ошибка: {e}")

    # Демонстрация добавления продуктов в категорию
    print("\nДобавление нового продукта в категорию:")
    new_smartphone = Smartphone(
        "Xiaomi Redmi Note 13",
        "128GB, Синий",
        35000,
        12,
        "Средняя",
        "Redmi Note 13",
        128,
        "синий",
    )

    category1.add_product(new_smartphone)
    print(f"После добавления: {category1}")
    print("Продукты в категории:")
    print(category1.products)

    # Демонстрация ошибки при добавлении неверного типа
    print("\nПопытка добавить не продукт в категорию:")
    try:
        category1.add_product("не продукт")
    except TypeError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
