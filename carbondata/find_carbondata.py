""" function to find carbon data based on dg products """
from carbondata.carbondata import get_component_factors_A, get_fastener_factors_A, get_fastener_factors_D, get_fastener_factors_C, get_component_factors_D, get_component_factors_C
from models.models import CarbonData


def find_product_factors_A(material: str, fastener_factors, component_factors) -> CarbonData:
    if material in fastener_factors:
        # For fasteners, use the get_fastener_factors function to retrieve the emission factors
        fastener_factors = get_fastener_factors_A(material)
        return CarbonData(
            label=material,
            total=fastener_factors.total,
            unit=fastener_factors.unit
        )
    elif material in component_factors:
        # For components, use the get_component_factors function to retrieve the emission factors
        component_factors = get_component_factors_A(material)
        return CarbonData(
            label=material,
            total=component_factors.total,
            unit=component_factors.unit
        )
    else:
        # If the material is not found in the fastener_factors or component_factors, you can either raise an error or return a default value
        return CarbonData(
            label=material,
            total=0.0,
            unit=""
        )


def find_product_factors_C(material: str, fastener_factors, component_factors) -> CarbonData:
    if material in fastener_factors:
        # For fasteners, use the get_fastener_factors function to retrieve the emission factors
        fastener_factors = get_fastener_factors_C(material)
        return CarbonData(
            label=material,
            total=fastener_factors.total,
            unit=fastener_factors.unit
        )
    elif material in component_factors:
        # For components, use the get_component_factors function to retrieve the emission factors
        component_factors = get_component_factors_C(material)
        return CarbonData(
            label=material,
            total=component_factors.total,
            unit=component_factors.unit
        )
    else:
        # If the material is not found in the fastener_factors or component_factors, you can either raise an error or return a default value
        return CarbonData(
            label=material,
            total=0.0,
            unit=""
        )


def find_product_factors_D(material: str, fastener_factors, component_factors) -> CarbonData:
    if material in fastener_factors:
        # For fasteners, use the get_fastener_factors function to retrieve the emission factors
        fastener_factors = get_fastener_factors_D(material)
        return CarbonData(
            label=material,
            total=fastener_factors.total,
            unit=fastener_factors.unit
        )
    elif material in component_factors:
        # For components, use the get_component_factors function to retrieve the emission factors
        component_factors = get_component_factors_D(material)
        return CarbonData(
            label=material,
            total=component_factors.total,
            unit=component_factors.unit
        )
    else:
        # If the material is not found in the fastener_factors or component_factors, you can either raise an error or return a default value
        return CarbonData(
            label=material,
            total=0.0,
            unit=""
        )