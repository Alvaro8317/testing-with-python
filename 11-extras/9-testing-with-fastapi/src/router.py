import fastapi

from src import database, models

router = fastapi.APIRouter(prefix="/costs", tags=["costs"])


@router.get("/", response_model=list[models.Cost])
def list_costs() -> list[models.Cost]:
    return database.get_all()


@router.get("/{cost_id}", response_model=models.Cost)
def get_cost(cost_id: int) -> models.Cost:
    cost: models.Cost | None = database.get_by_id(cost_id)
    if cost is None:
        raise fastapi.HTTPException(status_code=404, detail="Cost not found")
    return cost


@router.post("/", response_model=models.Cost, status_code=201)
def create_cost(payload: models.CostCreate) -> models.Cost:
    cost: models.Cost = models.Cost(id=database.next_id(), **payload.model_dump())
    return database.create(cost)


@router.put("/{cost_id}", response_model=models.Cost)
def update_cost(cost_id: int, payload: models.CostUpdate) -> models.Cost:
    data: dict[str, object] = {k: v for k, v in payload.model_dump().items() if v is not None}
    cost: models.Cost | None = database.update(cost_id, data)
    if cost is None:
        raise fastapi.HTTPException(status_code=404, detail="Cost not found")
    return cost


@router.delete("/{cost_id}", status_code=204)
def delete_cost(cost_id: int) -> None:
    if not database.delete(cost_id):
        raise fastapi.HTTPException(status_code=404, detail="Cost not found")
