from enum import Enum

from pydantic import BaseModel, Field, field_validator

# ===========================================================================
# Enumeraciones
# ===========================================================================


class SocketType(str, Enum):
    AM5 = "AM5"
    LGA1700 = "LGA1700"
    LGA1851 = "LGA1851"


class RAMType(str, Enum):
    DDR4 = "DDR4"
    DDR5 = "DDR5"


class StorageInterface(str, Enum):
    SATA = "SATA"
    NVME = "NVMe"


class FormFactor(str, Enum):
    ATX = "ATX"
    MATX = "mATX"
    ITX = "ITX"


# ===========================================================================
# Componentes
# ===========================================================================


class CPU(BaseModel):
    name: str = Field(..., min_length=2)
    brand: str = Field(..., min_length=2)
    socket: SocketType
    cores: int = Field(..., ge=1, le=128)
    tdp_watts: int = Field(..., gt=0)
    base_ghz: float = Field(..., gt=0)

    @field_validator("brand")
    @classmethod
    def brand_must_be_known(cls, v: str) -> str:
        allowed = {"Intel", "AMD"}
        if v not in allowed:
            raise ValueError(f"Brand debe ser uno de {allowed}")
        return v


class RAM(BaseModel):
    name: str = Field(..., min_length=2)
    ram_type: RAMType
    capacity_gb: int = Field(..., gt=0)
    speed_mhz: int = Field(..., gt=0)
    sticks: int = Field(1, ge=1, le=4)


class Storage(BaseModel):
    name: str = Field(..., min_length=2)
    interface: StorageInterface
    capacity_gb: int = Field(..., gt=0)


class GPU(BaseModel):
    name: str = Field(..., min_length=2)
    vram_gb: int = Field(..., gt=0)
    tdp_watts: int = Field(..., gt=0)


class Motherboard(BaseModel):
    name: str = Field(..., min_length=2)
    socket: SocketType
    form_factor: FormFactor
    ram_type: RAMType
    ram_slots: int = Field(..., ge=2, le=8)
    storage_slots: int = Field(..., ge=1, le=6)
    has_pcie_slot: bool = True


class PSU(BaseModel):
    name: str = Field(..., min_length=2)
    wattage: int = Field(..., gt=0)


class PCCase(BaseModel):
    name: str = Field(..., min_length=2)
    form_factor: FormFactor
    max_gpu_length_mm: int = Field(..., gt=0)
