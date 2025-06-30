""" result models """
from typing import List, Optional
from pydantic import BaseModel


class DSSGNode(BaseModel):
    type: str
    d_dir: int
    parent: Optional[int]
    blocked_components: Optional[int]


class Result(BaseModel):
    total: float


class ProductResult(BaseModel):
    product: int | str
    material: str
    result: Result


class MachineResult(BaseModel):
    product: str
    machine: str | None
    result: Result


class EmissionResult(BaseModel):
    target_component: int
    d_dir: int
    product_results: List[ProductResult]
    machine_results: List[MachineResult]
    total_products: float
    total_machines: float
    result: Result