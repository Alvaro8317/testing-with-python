import pytest
from src.jewelry import exceptions, jewelry_store, models


@pytest.fixture
def fxt_invalid_jewelry_item() -> models.JewelryItem:
    return models.JewelryItem(
        name="A new stone",
        material=models.Material.ROSE_GOLD,
        gemstone=models.Gemstone.EMERALD,
        weight_grams=150.50,
        base_price=800.0,
        stock=5,
    )


@pytest.fixture
def fxt_jewelry_store_empty() -> jewelry_store.JewelryStore:
    return jewelry_store.JewelryStore()


def test_should_not_add_item_to_jewelry_store_because_is_invalid_gemstone(
    fxt_invalid_jewelry_item: models.JewelryItem,
    fxt_jewelry_store_empty: jewelry_store.JewelryStore,
) -> None:
    with pytest.raises(exceptions.InvalidGemstoneError):
        fxt_jewelry_store_empty.add_item(fxt_invalid_jewelry_item)


def test_should_add_item_to_jewelry_store(
    fxt_jewelry_store_empty: jewelry_store.JewelryStore,
) -> None:
    jewelry_item = models.JewelryItem(
        name="A new stone",
        material=models.Material.ROSE_GOLD,
        gemstone=models.Gemstone.NONE,
        weight_grams=150.50,
        base_price=800.0,
        stock=5,
    )
    assert fxt_jewelry_store_empty.inventory_count() == 0
    fxt_jewelry_store_empty.add_item(jewelry_item)
    assert fxt_jewelry_store_empty.inventory_count() == 1
