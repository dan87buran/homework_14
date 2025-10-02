import src.models


def main():
    """Основная функция для демонстрации работы классов."""

    # Создание смартфонов
    smartphone1 = src.models.Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Черный цвет, 200MP камера",
        180000,
        5,
        "Высокая",
        "S23 Ultra",
        256,
        "черный",
    )
    smartphone2 = src.models.Smartphone(
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
    lawn_grass1 = src.models.LawnGrass(
        "Газонная трава",
        "Высококачественная трава",
        5000,
        10,
        "Россия",
        14,
        "зеленый",
    )
    lawn_grass2 = src.models.LawnGrass(
        "Газонная трава Премиум",
        "Премиум трава",
        7500,
        15,
        "Германия",
        7,
        "темно-зеленый",
    )

    # Создание категорий
    category1 = src.models.Category(
        "Смартфоны",
        "Мобильные устройства",
        [smartphone1, smartphone2],
    )
    category2 = src.models.Category(
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
    new_smartphone = src.models.Smartphone(
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


if __name__ == '__main__':
    smartphone1 = src.models.Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                                        "S23 Ultra", 256, "Серый")
    smartphone2 = src.models.Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = src.models.Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)

    print(smartphone2.name)
    print(smartphone2.description)
    print(smartphone2.price)
    print(smartphone2.quantity)
    print(smartphone2.efficiency)
    print(smartphone2.model)
    print(smartphone2.memory)
    print(smartphone2.color)

    print(smartphone3.name)
    print(smartphone3.description)
    print(smartphone3.price)
    print(smartphone3.quantity)
    print(smartphone3.efficiency)
    print(smartphone3.model)
    print(smartphone3.memory)
    print(smartphone3.color)

    grass1 = src.models.LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = src.models.LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)

    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)

    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)

    grass_sum = grass1 + grass2
    print(grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = src.models.Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = src.models.Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    category_smartphones.add_product(smartphone3)

    print(category_smartphones.products)

    print(src.models.Category.product_count)

    try:
        category_smartphones.add_product("Not a product")
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")
