"""
store carbon data as dictionaries with emission factors
"""
from models.models import CarbonData, MachineData

machine_factors = {
    'drill': MachineData(
        label='drill',
        total=0.0234762,
        unit="kgCO2e"
    ),
    'impactwrench': MachineData(
        label='impactwrench',
        total=0.0405498,
        unit="kgCO2e"
    ),
}


def get_machine_factors(label):
    return machine_factors[label]


# emission factor for life cycle phase D
fastener_factors_D = {
    'screw': CarbonData(
        label='screw',
        total=-0.00166539,
        unit="kgCO2e/pc"
    ),
    'nail': CarbonData(
        label='nail',
        total=-0.00252616,
        unit="kgCO2e/pc"
    ),
    'bolt': CarbonData(
        label='bolt',
        total=-0.0029022,
        unit="kgCO2e/pc"
    ),
    'glue': CarbonData(
        label='glue',
        total=0.00835396,
        unit="kgCO2e/pc"
    )
}


def get_fastener_factors_D(label):
    return fastener_factors_D[label]


# emission factor for life cycle phase C1
fastener_factors_C = {
    'nail': CarbonData(
        label='nail',
        total=5.824E-07,
        unit="kgCO2e"
    ),
}

def get_fastener_factors_C(label):
    return fastener_factors_C[label]


# emission factor for life cycle phase A1-A3
fastener_factors_A = {
    'screw': CarbonData(
        label='screw',
        total=0.00549024,
        unit="kgCO2e/pc"
    ),
    'nail': CarbonData(
        label='nail',
        total=0.00645736,
        unit="kgCO2e/pc"
    ),
    'bolt': CarbonData(
        label='bolt',
        total=0.005688,
        unit="kgCO2e/pc"
    ),
    'glue': CarbonData(
        label='glue',
        total=0.06103692,
        unit="kgCO2e/pc"
    )
}


def get_fastener_factors_A(label):
    return fastener_factors_A[label]


# emission factor for life cycle phase A1-A3
component_factors_A = {
    'glass': CarbonData(
        label='glass',
        total=13.35,
        unit="kgCO2e/m2"
    ),
    'wood': CarbonData(
        label='wood',
        total=-226.3,
        unit="kgCO2e/m3"
    ),
    'aluminium': CarbonData(
        label='aluminium',
        total=17.04,
        unit="kgCO2e/m"
    ),
    'pvc': CarbonData(
        label='pvc',
        total=8.131,
        unit="kgCO2e/m"
    ),
    'gasket': CarbonData(
        label='gasket',
        total=862.4,
        unit="kgCO2e/m3"
    ),
    'glazingbead': CarbonData(
        label='glazingbead',
        total=12.45,
        unit="kgCO2e/m"
    ),
    'silicone': CarbonData(
        label='silicone',
        total=9232.8,
        unit="kgCO2e/m3"
    ),
    'alum_corner': CarbonData(
        label='alum_corner',
        total=12.45,
        unit="kgCO2e/m"
    ),
    'epdm': CarbonData(
        label='epdm',
        total=1.331,
        unit="kgCO2e/m"
    ),
}


def get_component_factors_A(label):
    return component_factors_A[label]


component_factors_C = {
    'glass': CarbonData(
        label='glass',
        total=0.21997,
        unit="kgCO2e/m2"
    ),
    'wood': CarbonData(
        label='wood',
        total=749.852,
        unit="kgCO2e/m3"
    ),
    'aluminium': CarbonData(
        label='aluminium',
        total=0.592124,
        unit="kgCO2e/m"
    ),
    'pvc': CarbonData(
        label='pvc',
        total=2.9775519,
        unit="kgCO2e/m"
    ),
    'gasket': CarbonData(
        label='gasket',
        total=212.97857,
        unit="kgCO2e/m3"
    ),
    'glazingbead': CarbonData(
        label='glazingbead',
        total=0.003189,
        unit="kgCO2e/m"
    ),
    'silicone': CarbonData(
        label='silicone',
        total=1221.0612,
        unit="kgCO2e/m3"
    ),
    'alum_corner': CarbonData(
        label='alum_corner',
        total=0.003189,
        unit="kgCO2e/m"
    ),
    'epdm': CarbonData(
        label='epdm',
        total=2.72163,
        unit="kgCO2e/m"
    ),
}


def get_component_factors_C(label):
    return component_factors_C[label]


# emission factor for life cycle phase A1-A3
component_factors_D = {
    'glass': CarbonData(
        label='glass',
        total=0.176,
        unit="kgCO2e/m2"
    ),
    'wood': CarbonData(
        label='wood',
        total=-159.8,
        unit="kgCO2e/m3"
    ),
    'aluminium': CarbonData(
        label='aluminium',
        total=-9.588,
        unit="kgCO2e/m"
    ),
    'pvc': CarbonData(
        label='pvc',
        total=-2.984,
        unit="kgCO2e/m"
    ),
    'gasket': CarbonData(
        label='gasket',
        total=-364,
        unit="kgCO2e/m3"
    ),
    'glazingbead': CarbonData(
        label='glazingbead',
        total=-7.131,
        unit="kgCO2e/m"
    ),
    'silicone': CarbonData(
        label='silicone',
        total=-355.32,
        unit="kgCO2e/m3"
    ),
    'alum_corner': CarbonData(
        label='alum_corner',
        total=-7.131,
        unit="kgCO2e/m"
    ),
    'epdm': CarbonData(
        label='epdm',
        total=-1.117,
        unit="kgCO2e/m"
    ),
}


def get_component_factors_D(label):
    return component_factors_D[label]