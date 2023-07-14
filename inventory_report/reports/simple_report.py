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
            sorted_old = 

        return (
            f"Oldest manufacturing date: {}"
            f"Closest expiration date: {}"
            f"Company with the largest inventory: {}"
        )
