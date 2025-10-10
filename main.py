from src.models import Product, Smartphone, LawnGrass, Category, Order


def main():
    """Основная функция для демонстрации работы классов."""
    print("=== Демонстрация работы классов ===\n")

    # Создание продуктов
    print("1. Создание продуктов:")

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
    print("\n2. Создание категорий:")
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
    print("\n3. Строковые представления:")
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
    print("4. Сложение продуктов:")
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
    print("\n5. Попытка сложить смартфон и газонную траву:")
    try:
        total = smartphone1 + lawn_grass1
        print(f"Общая стоимость: {total}")
    except TypeError as e:
        print(f"Ошибка: {e}")

    # Демонстрация добавления продуктов в категорию
    print("\n6. Добавление нового продукта в категорию:")
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
    print("\n7. Попытка добавить не продукт в категорию:")
    try:
        category1.add_product("не продукт")
    except TypeError as e:
        print(f"Ошибка: {e}")

    # Демонстрация заказов
    print("\n8. Создание заказов:")
    order1 = Order(smartphone1, 2)
    order2 = Order(lawn_grass1, 5)

    print("Заказ 1:")
    print(order1)
    print("\nЗаказ 2:")
    print(order2)

    # Демонстрация наследования
    print("\n9. Проверка наследования:")
    print(f"Smartphone является Product: {isinstance(smartphone1, Product)}")
    print(f"Smartphone является BaseProduct: {isinstance(smartphone1, type(smartphone1).__bases__[1])}")
    print(f"Category является BaseEntity: {isinstance(category1, type(category1).__bases__[0])}")
    print(f"Order является BaseEntity: {isinstance(order1, type(order1).__bases__[0])}")


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            f"Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством: {e}")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
