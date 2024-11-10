import json
import os

from src.task import Category, Product


def read_json(path: str):          # type: ignore[no-untyped-def]
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):       # type: ignore[no-untyped-def]
    category = []
    for product in data:
        products = []
        for product_list in product["products"]:
            products.append(Product(**product_list))
        product["products"] = products
        category.append(Category(**product))
    return category


if __name__ == '__main__':
    raw_data = read_json("../data/products.json")
    users_data = create_objects_from_json(raw_data)
    print(users_data[0].name)
    print(users_data[0].description)
    print(users_data[0].products)
    print(users_data[0].category_count)
    print(users_data[0].product_count)
