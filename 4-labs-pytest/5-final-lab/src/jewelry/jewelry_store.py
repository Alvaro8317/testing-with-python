from src.jewelry import exceptions, models

MATERIAL_PRICE_MULTIPLIER = {
    models.Material.GOLD: 1.8,
    models.Material.SILVER: 1.0,
    models.Material.PLATINUM: 2.5,
    models.Material.ROSE_GOLD: 1.6,
}

GEMSTONE_PRICE_ADDITION = {
    models.Gemstone.DIAMOND: 5000.0,
    models.Gemstone.RUBY: 3000.0,
    models.Gemstone.EMERALD: 2500.0,
    models.Gemstone.SAPPHIRE: 2000.0,
    models.Gemstone.NONE: 0.0,
}

COMPATIBLE_GEMSTONES = {
    models.Material.GOLD: [
        models.Gemstone.DIAMOND,
        models.Gemstone.RUBY,
        models.Gemstone.SAPPHIRE,
        models.Gemstone.NONE,
    ],
    models.Material.SILVER: [
        models.Gemstone.EMERALD,
        models.Gemstone.SAPPHIRE,
        models.Gemstone.NONE,
    ],
    models.Material.PLATINUM: [
        models.Gemstone.DIAMOND,
        models.Gemstone.RUBY,
        models.Gemstone.EMERALD,
        models.Gemstone.SAPPHIRE,
        models.Gemstone.NONE,
    ],
    models.Material.ROSE_GOLD: [
        models.Gemstone.RUBY,
        models.Gemstone.SAPPHIRE,
        models.Gemstone.NONE,
    ],
}


class JewelryStore:
    def __init__(self) -> None:
        self._inventory: list[models.JewelryItem] = []
        self._sales_log: list[dict] = []

    # ── Inventory management ─────────────────────────────────────────────────

    def add_item(self, item: models.JewelryItem) -> None:
        """Add a jewelry item to the inventory."""
        if item.gemstone != models.Gemstone.NONE:
            compatible = COMPATIBLE_GEMSTONES.get(item.material, [])
            if item.gemstone not in compatible:
                raise exceptions.InvalidGemstoneError(
                    f"Gemstone '{item.gemstone}' is not compatible with material '{item.material}'"
                )
        self._inventory.append(item)

    def remove_item(self, name: str) -> models.JewelryItem:
        """Remove and return a jewelry item from the inventory by name."""
        for i, item in enumerate(self._inventory):
            if item.name == name:
                return self._inventory.pop(i)
        raise KeyError(f"Item '{name}' not found in inventory")

    def get_item(self, name: str) -> models.JewelryItem:
        """Retrieve a jewelry item by name without removing it."""
        for item in self._inventory:
            if item.name == name:
                return item
        raise KeyError(f"Item '{name}' not found in inventory")

    def update_stock(self, name: str, quantity: int) -> None:
        """Update the stock of a jewelry item. Quantity can be positive or negative."""
        item = self.get_item(name)
        new_stock = item.stock + quantity
        if new_stock < 0:
            raise exceptions.InsufficientStockError(
                f"Cannot reduce stock of '{name}' by {abs(quantity)}. Current stock: {item.stock}"
            )
        if new_stock > 1000:
            raise ValueError(f"Stock cannot exceed 1000 units for item '{name}'")
        object.__setattr__(item, "stock", new_stock)

    # ── Pricing ──────────────────────────────────────────────────────────────

    def calculate_price(self, name: str) -> float:
        """Calculate the final price of an item based on material and gemstone."""
        item = self.get_item(name)
        multiplier = MATERIAL_PRICE_MULTIPLIER[item.material]
        gemstone_addition = GEMSTONE_PRICE_ADDITION[item.gemstone]
        return round((item.base_price * multiplier) + gemstone_addition, 2)

    def apply_discount(self, name: str, discount_percent: float) -> float:
        """Apply a discount to an item and return the discounted price."""
        if discount_percent < 0 or discount_percent > 100:
            raise exceptions.InvalidDiscountError(
                f"Discount must be between 0 and 100. Got: {discount_percent}"
            )
        price = self.calculate_price(name)
        discount_amount = price * (discount_percent / 100)
        return round(price - discount_amount, 2)

    def calculate_bulk_discount(self, name: str, quantity: int) -> float:
        """
        Calculate a bulk discount based on quantity purchased.
        - 1-4 units:   no discount
        - 5-9 units:   5% discount
        - 10-19 units: 10% discount
        - 20+ units:   15% discount
        """
        if quantity <= 0:
            raise ValueError(f"Quantity must be greater than 0. Got: {quantity}")

        item = self.get_item(name)
        if quantity > item.stock:
            raise exceptions.InsufficientStockError(
                f"Requested quantity ({quantity}) exceeds available stock ({item.stock})"
            )

        if quantity >= 20:
            discount = 15.0
        elif quantity >= 10:
            discount = 10.0
        elif quantity >= 5:
            discount = 5.0
        else:
            discount = 0.0

        unit_price = self.calculate_price(name)
        discounted_price = unit_price * (1 - discount / 100)
        return round(discounted_price * quantity, 2)

    # ── Sales ─────────────────────────────────────────────────────────────────

    def sell_item(self, name: str, quantity: int) -> float:
        """
        Sell a quantity of an item. Reduces stock and logs the sale.
        Returns the total sale amount.
        """
        if quantity <= 0:
            raise ValueError(f"Quantity must be greater than 0. Got: {quantity}")

        total = self.calculate_bulk_discount(name, quantity)
        self.update_stock(name, -quantity)
        self._sales_log.append(
            {
                "item": name,
                "quantity": quantity,
                "total": total,
            }
        )
        return total

    def total_sales(self) -> float:
        """Return the total amount from all sales."""
        return round(sum(sale["total"] for sale in self._sales_log), 2)

    def sales_count(self) -> int:
        """Return the number of sales transactions."""
        return len(self._sales_log)

    # ── Inventory queries ─────────────────────────────────────────────────────

    def inventory_count(self) -> int:
        """Return the number of distinct items in the inventory."""
        return len(self._inventory)

    def items_by_material(self, material: models.Material) -> list[models.JewelryItem]:
        """Return all items made of a specific material."""
        if not isinstance(material, models.Material):
            raise exceptions.InvalidMaterialError(f"'{material}' is not a valid material")
        return [item for item in self._inventory if item.material == material]

    def most_valuable_item(self) -> models.JewelryItem | None:
        """Return the item with the highest calculated price, or None if inventory is empty."""
        if not self._inventory:
            return None
        return max(self._inventory, key=lambda item: self.calculate_price(item.name))
