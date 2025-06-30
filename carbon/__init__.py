"""
package to store carbon emission calculations

idea:
- remove all fasteners and components to remove target component
- calculate carbon footprint for fasteners
    - with machines and their energy consumption
    - end of life scenario of fasteners (reuse, recycling, ...)
- calculate carbon footprint for components
    - end of life scenario of materials (reuse, recycling,...)

approach:
- function should be used inside the dssg function
- whenever a part is added to the dssg:
    - check if it is component or fastener
    - check which material / product it is
    - for each material / product / process we need an own calculation
        - f.e. for fasteners like screws we need energy consumption of drills
        and its impact to calculate the carbon emissions
        - f.e. for glue or nails we need no energy, just human power and machinery like tongs
        - the calculation will be done separately for
            - 1. disassembly process (machines, energy consumption)
            - 2. end of life scenario of material / product (reuse, recycling,...)
- whenever glue is used:
    - components have to be processed to disposal or recycling (only phase D)
    and a new component has to be created (A1-A3)

input:
- CarbonData as a class with attributes like fossil, biogenic, luluc, total
    - contains the emission factors for each material / product / process
"""