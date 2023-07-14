from typing import Optional

from inventory_report.product import Product


class Inventory:
    def __init__(self, data:Optional[list[Product]] = None) -> None:
        self._data = data or []

    @property
    def data(self) -> Optional[list[Product]]:
        return self._data

    def add_data(self, new_product:list[Product]) -> None:
        for product in new_product:
            self._data.append(product)
