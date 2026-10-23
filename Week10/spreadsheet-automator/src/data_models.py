# spreadsheet-automator/src/data_models.py
# Structured data model for one row of sales data.
from dataclasses import dataclass


@dataclass
class SaleItem:
    """Represents one product row from the sales spreadsheet."""
    product_name: str
    quantity: int
    unit_price: float

    @property
    def total_price(self) -> float:
        """Total price for this item (Quantity x Unit Price)."""
        return self.quantity * self.unit_price

    @classmethod
    def from_row(cls, row):
        """
        Creates a SaleItem from a spreadsheet row (tuple of cell values).
        Raises ValueError / TypeError if Quantity or Unit Price is not a number.
        """
        product_name = row[0] if len(row) > 0 else None
        quantity = row[1] if len(row) > 1 else 0
        unit_price = row[2] if len(row) > 2 else 0.0
        return cls(product_name=product_name,
                   quantity=int(quantity),
                   unit_price=float(unit_price))
