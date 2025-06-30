""" function to calculate carbon footprint for dssg """
from typing import List
from models.models import MachineData
from models.results import EmissionResult, MachineResult, ProductResult, Result


def calculate_process_emissions(material, machine_data: dict[str, MachineData]) -> MachineResult:

    if material == 'screw':
        machine = machine_data['drill']
        total_factor = machine.total
    elif material == 'bolt':
        machine = machine_data['impactwrench']
        total_factor = machine.total

    else:
        machine = None
        total_factor = 0

    return MachineResult(
                product=material,
                machine=machine.label if machine else None,
                result=Result(total=total_factor)
            )


def calculate_product_emissions(p, p_type, material, quantities: dict, factors_a, factors_c, factors_d) -> ProductResult:
    result = 0

    if p_type is None:
        raise ValueError(f"Unknown product type for {p}")

    if p_type == 'c':
        quantity = quantities[p]
        result_A = factors_a.total * quantity
        result_C = factors_c.total * quantity
        result_D = factors_d.total * quantity
        result = result_A + result_C + result_D

    elif p_type == 'f':
        quantity = quantities[p]
        if material == 'glue':
            result_A = factors_a.total * quantity
            result_C = factors_c.total * quantity
            result_D = factors_d.total * quantity
            result = result_A + result_C + result_D
        else:
            result_C = factors_c.total * quantity
            result = result_C

    return ProductResult(
        product=p,
        material=material,
        result=Result(total=result)
    )


def calculate_final_emissions(products: List[ProductResult], machines: List[MachineResult], target_component, d) -> EmissionResult:
    total = 0
    total_products = 0
    total_machines = 0

    for product in products:
        total_products += product.result.total
        total += product.result.total

    for machine in machines:
        total_machines += machine.result.total
        total += machine.result.total

    return EmissionResult(
        target_component=target_component,
        d_dir=d,
        product_results=products,
        machine_results=machines,
        total_products=total_products,
        total_machines=total_machines,
        result=Result(
            total=total
        )
    )
