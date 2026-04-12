from src import catalog, models


def test_should_add_a_game_to_the_catalog_and_increate_the_size_of_this_one() -> None:
    subject = catalog.CatalogGames()
    assert subject.catalog_size() == 0
    game_to_add = models.Game(
        title="Clair Obscur: Expedition 33", genre="RPG", price=39.99, rating=4.9
    )
    subject.add_to_catalog(game=game_to_add)
    assert subject.catalog_size() == 1
