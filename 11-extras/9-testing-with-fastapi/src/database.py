from src import models

_costs: dict[int, models.Cost] = {}
_next_id: int = 1


def get_all() -> list[models.Cost]:
    return list(_costs.values())


def get_by_id(cost_id: int) -> models.Cost | None:
    return _costs.get(cost_id)


def create(cost: models.Cost) -> models.Cost:
    _costs[cost.id] = cost
    return cost


def update(cost_id: int, data: dict[str, object]) -> models.Cost | None:
    existing: models.Cost | None = _costs.get(cost_id)
    if existing is None:
        return None
    updated: models.Cost = existing.model_copy(update=data)
    _costs[cost_id] = updated
    return updated


def delete(cost_id: int) -> bool:
    if cost_id not in _costs:
        return False
    del _costs[cost_id]
    return True


def next_id() -> int:
    global _next_id
    result: int = _next_id
    _next_id += 1
    return result


def reset() -> None:
    global _costs, _next_id
    _costs = {}
    _next_id = 1
