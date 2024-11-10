import pytest

from src.task import Category, Product


@pytest.fixture
def category():          # type: ignore[no-untyped-def]
    return Category(
        "Смартфоны",
        """Смартфоны, как средство не только коммуникации,
           но и получение дополнительных функций для удобства жизни""",
        [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5,
            },
            {"name": "Iphone 15", "description": "512GB, Gray space",
             "price": 210000.0, "quantity": 8},
            {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий",
             "price": 31000.0, "quantity": 14},
        ],
    )


def test_init_category(category):          # type: ignore[no-untyped-def]
    assert category.name == "Смартфоны"
    assert (
        category.description
        == """Смартфоны, как средство не только коммуникации,
           но и получение дополнительных функций для удобства жизни""",
    )
    assert category.products == [
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        },
        {"name": "Iphone 15", "description": "512GB, "
                                             "Gray space",
         "price": 210000.0, "quantity": 8},
        {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий",
         "price": 31000.0, "quantity": 14},
    ]


@pytest.fixture
def product():       # type: ignore[no-untyped-def]
    return Product("Samsung Galaxy C23 Ultra",
                   "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_init_product(product):            # type: ignore[no-untyped-def]
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_count(category):            # type: ignore[no-untyped-def]
    assert Category.category_count == 2
    assert Category.product_count == 6
