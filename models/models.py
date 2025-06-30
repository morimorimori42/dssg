""" models for calculations """
from typing import List, Optional, Union
from pydantic import BaseModel


class CCMatrixCell(BaseModel):
    components: List[int]
    fasteners: List[str]


class CCMatrix(BaseModel):
    data: List[List[Optional[CCMatrixCell]]]

    def __init__(self, num_components: int, num_directions: int):
        super().__init__(data=[[None for _ in range(num_directions)] for _ in range(num_components)])


class CFMatrixEntry(BaseModel):
    fastener: str
    direction: int


class CFMatrix(BaseModel):
    data: List[CFMatrixEntry]


class MCMatrixCell(BaseModel):
    components: List[int | None]
    fasteners: List[str | None]


class MCMatrix(BaseModel):
    data: List[List[Optional[MCMatrixCell]]]

    def __init__(self, num_components: int, num_directions: int):
        super().__init__(data=[[None for _ in range(num_directions)] for _ in range(num_components)])


class MFMatrixEntry(BaseModel):
    component: int | None


class MFMatrix(BaseModel):
    data: List[List[Optional[MFMatrixEntry]]]

    def __init__(self, num_fasteners: int, num_directions: int):
        super().__init__(data=[[None for _ in range(num_directions)] for _ in range(num_fasteners)])


class PCMatrixEntry(BaseModel):
    blocking_components: int


class PCMatrix(BaseModel):
    data: List[List[Optional[PCMatrixEntry]]]

    def __init__(self, num_components: int, num_directions: int):
        super().__init__(data=[[None for _ in range(num_directions)] for _ in range(num_components)])


class DisassemblyTime(BaseModel):
    time: float
    unit: str


class MachineData(BaseModel):
    label: str
    total: float
    unit: str


class CarbonData(BaseModel):
    label: str | None
    total: float
    unit: str
