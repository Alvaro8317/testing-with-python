class JewelryError(Exception):
    """Base exception for jewelry store errors."""

    pass


class InvalidMaterialError(JewelryError):
    """Raised when an invalid material is provided."""

    pass


class InvalidGemstoneError(JewelryError):
    """Raised when an invalid gemstone is provided."""

    pass


class InsufficientStockError(JewelryError):
    """Raised when there is not enough stock to complete an operation."""

    pass


class InvalidDiscountError(JewelryError):
    """Raised when a discount value is out of the allowed range."""

    pass
