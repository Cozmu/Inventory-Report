from collections import Counter
from datetime import date

from inventory_report.inventory import Inventory
from inventory_report.product import Product


class SimpleReport:
    def __init__(self) -> None:
        self.stock: list[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.stock.append(inventory)

    def generate(self) -> str:
        for inventory in self.stock:
            def get_closest(product: Product) -> str:
                if product.expiration_date >= str(date.today()):
                    return product.expiration_date
                else:
                    return str(date.max)

            sort_oldest = sorted(inventory.data, key=lambda x: x.manufacturing_date)
            sort_closest = sorted(inventory.data, key=get_closest)
            count_biggest_stock = Counter(product.company_name for product in inventory.data).most_common()

        return (
            f"Oldest manufacturing date: {sort_oldest[0].manufacturing_date}\n"
            f"Closest expiration date: {sort_closest[0].expiration_date}\n"
            f"Company with the largest inventory: {count_biggest_stock[0][0]}\n"
        )
