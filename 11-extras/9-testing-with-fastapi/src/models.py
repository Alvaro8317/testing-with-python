import datetime

from pydantic import BaseModel, Field


class CostCreate(BaseModel):
    description: str = Field(..., min_length=1, max_length=200)
    amount: float = Field(..., gt=0)
    category: str = Field(..., min_length=1, max_length=100)
    date: datetime.date = Field(default_factory=datetime.date.today)


class CostUpdate(BaseModel):
    description: str | None = Field(None, min_length=1, max_length=200)
    amount: float | None = Field(None, gt=0)
    category: str | None = Field(None, min_length=1, max_length=100)
    date: datetime.date | None = None


class Cost(CostCreate):
    id: int
