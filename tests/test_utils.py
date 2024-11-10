from unittest.mock import mock_open, patch

from src.utils import create_objects_from_json, read_json


@patch("builtins.open", new_callable=mock_open,
       read_data='[{"name": "Смартфоны", "description": "Samsung"}]')
def test_read_json(mock_file):        # type: ignore[no-untyped-def]
    data = read_json("../data/products.json")
    assert data == [{"name": "Смартфоны", "description": "Samsung"}]


def test_create_objects_from_json():             # type: ignore[no-untyped-def]
    result = create_objects_from_json(
        [
            {
                "name": "Смартфоны",
                "description": "Смартфоны, как средство не "
                               "только коммуникации",
                "products": [
                    {
                        "name": "Samsung Galaxy C23 Ultra",
                        "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5,
                    }
                ],
            }
        ]
    )
    assert result[0].name == "Смартфоны"
