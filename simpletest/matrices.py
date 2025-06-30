""" matrices of simple example test case """
from models.models import (
    CCMatrix, CCMatrixCell, CFMatrix, CFMatrixEntry, MCMatrix,
    MCMatrixCell, MFMatrix, MFMatrixEntry, PCMatrix, PCMatrixEntry
)

dg = [1, 2, 3, 'f1', 'f2', 'f3', 'f4']

# include the materials + types of components and fasteners
dg_type = ['plastic frame', 'glass', 'wood', 'screw', 'screw', 'glue', 'nail']

cc_matrix3 = CCMatrix(num_components=3, num_directions=4)
cc_matrix3.data[0][0] = CCMatrixCell(components=[3], fasteners=['f4'])
cc_matrix3.data[0][1] = CCMatrixCell(components=[], fasteners=[])
cc_matrix3.data[0][2] = CCMatrixCell(components=[2], fasteners=['f1', 'f2'])
cc_matrix3.data[0][3] = CCMatrixCell(components=[], fasteners=[])
cc_matrix3.data[1][0] = CCMatrixCell(components=[3], fasteners=['f3'])
cc_matrix3.data[1][1] = CCMatrixCell(components=[], fasteners=[])
cc_matrix3.data[1][2] = CCMatrixCell(components=[], fasteners=[])
cc_matrix3.data[1][3] = CCMatrixCell(components=[1], fasteners=['f1', 'f2'])
cc_matrix3.data[2][0] = CCMatrixCell(components=[], fasteners=['f3', 'f4'])
cc_matrix3.data[2][1] = CCMatrixCell(components=[1, 2], fasteners=[])
cc_matrix3.data[2][2] = CCMatrixCell(components=[], fasteners=[])
cc_matrix3.data[2][3] = CCMatrixCell(components=[], fasteners=[])

cf_matrix3 = CFMatrix(data=[
    CFMatrixEntry(fastener='f1', direction=4),
    CFMatrixEntry(fastener='f2', direction=4),
    CFMatrixEntry(fastener='f3', direction=1),
    CFMatrixEntry(fastener='f4', direction=1),
])

mc_matrix3 = MCMatrix(num_components=3, num_directions=4)
mc_matrix3.data[0][0] = MCMatrixCell(components=[], fasteners=['f1', 'f2'])
mc_matrix3.data[0][1] = MCMatrixCell(components=[], fasteners=['f1', 'f2'])
mc_matrix3.data[0][2] = MCMatrixCell(components=[], fasteners=['f4'])
mc_matrix3.data[0][3] = MCMatrixCell(components=[], fasteners=['f4'])
mc_matrix3.data[1][0] = MCMatrixCell(components=[], fasteners=['f1', 'f2'])
mc_matrix3.data[1][1] = MCMatrixCell(components=[], fasteners=['f1', 'f2'])
mc_matrix3.data[1][2] = MCMatrixCell(components=[], fasteners=['f3'])
mc_matrix3.data[1][3] = MCMatrixCell(components=[], fasteners=['f3'])
mc_matrix3.data[2][0] = MCMatrixCell(components=[], fasteners=[])
mc_matrix3.data[2][1] = MCMatrixCell(components=[], fasteners=[])
mc_matrix3.data[2][2] = MCMatrixCell(components=[], fasteners=['f3', 'f4'])
mc_matrix3.data[2][3] = MCMatrixCell(components=[], fasteners=['f3', 'f4'])

mf_matrix3 = MFMatrix(num_fasteners=4, num_directions=4)
mf_matrix3.data[0][0] = MFMatrixEntry(component=None)
mf_matrix3.data[0][1] = MFMatrixEntry(component=None)
mf_matrix3.data[0][2] = MFMatrixEntry(component=None)
mf_matrix3.data[0][3] = MFMatrixEntry(component=None)
mf_matrix3.data[1][0] = MFMatrixEntry(component=None)
mf_matrix3.data[1][1] = MFMatrixEntry(component=None)
mf_matrix3.data[1][2] = MFMatrixEntry(component=None)
mf_matrix3.data[1][3] = MFMatrixEntry(component=None)
mf_matrix3.data[2][0] = MFMatrixEntry(component=None)
mf_matrix3.data[2][1] = MFMatrixEntry(component=None)
mf_matrix3.data[2][2] = MFMatrixEntry(component=None)
mf_matrix3.data[2][3] = MFMatrixEntry(component=None)
mf_matrix3.data[3][0] = MFMatrixEntry(component=None)
mf_matrix3.data[3][1] = MFMatrixEntry(component=None)
mf_matrix3.data[3][2] = MFMatrixEntry(component=None)
mf_matrix3.data[3][3] = MFMatrixEntry(component=None)

pc_matrix3 = PCMatrix(num_components=3, num_directions=4)
pc_matrix3.data[0][0] = PCMatrixEntry(blocking_components=1)
pc_matrix3.data[0][1] = PCMatrixEntry(blocking_components=0)
pc_matrix3.data[0][2] = PCMatrixEntry(blocking_components=1)
pc_matrix3.data[0][3] = PCMatrixEntry(blocking_components=0)
pc_matrix3.data[1][0] = PCMatrixEntry(blocking_components=1)
pc_matrix3.data[1][1] = PCMatrixEntry(blocking_components=0)
pc_matrix3.data[1][2] = PCMatrixEntry(blocking_components=0)
pc_matrix3.data[1][3] = PCMatrixEntry(blocking_components=1)
pc_matrix3.data[2][0] = PCMatrixEntry(blocking_components=0)
pc_matrix3.data[2][1] = PCMatrixEntry(blocking_components=2)
pc_matrix3.data[2][2] = PCMatrixEntry(blocking_components=0)
pc_matrix3.data[2][3] = PCMatrixEntry(blocking_components=0)
