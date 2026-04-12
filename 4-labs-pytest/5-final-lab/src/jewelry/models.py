from enum import Enum

import pydantic


class Material(str, Enum):
    GOLD = "gold"
    SILVER = "silver"
    PLATINUM = "platinum"
    ROSE_GOLD = "rose_gold"


class Gemstone(str, Enum):
    DIAMOND = "diamond"
    RUBY = "ruby"
    EMERALD = "emerald"
    SAPPHIRE = "sapphire"
    NONE = "none"


class JewelryItem(pydantic.BaseModel):
    name: str = pydantic.Field(min_length=1, max_length=100)
    material: Material
    gemstone: Gemstone = Gemstone.NONE
    weight_grams: float = pydantic.Field(gt=0, le=500)
    base_price: float = pydantic.Field(gt=0)
    stock: int = pydantic.Field(ge=0, le=1000)
