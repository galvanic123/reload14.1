class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description,
                 products=None):        # type: ignore[no-untyped-def]
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.product_count += len(products) if products else 0
        Category.category_count += 1


class Product:

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price,
                 quantity):     # type: ignore[no-untyped-def]
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
