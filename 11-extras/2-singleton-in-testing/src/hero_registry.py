class HeroRegistry:
    _instance = None
    _heroes = {}

    def __new__(cls) -> "HeroRegistry":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._heroes = {}
        return cls._instance

    def add(self, name: str, power: int) -> None:
        self._heroes[name] = power

    def get(self, name: str) -> int | None:
        return self._heroes.get(name)

    def count(self) -> int:
        return len(self._heroes)
