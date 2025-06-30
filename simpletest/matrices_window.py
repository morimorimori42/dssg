"""
script to implement matrices for window case study
"""
from models.models import (
    CCMatrix, CCMatrixCell, CFMatrix, CFMatrixEntry,
    MCMatrix, MCMatrixCell, MFMatrix, MFMatrixEntry, PCMatrix, PCMatrixEntry
)

cc_matrix = CCMatrix(num_components=24, num_directions=6)
cc_matrix.data[0][0] = CCMatrixCell(components=[2, 5], fasteners=['f5'])
cc_matrix.data[0][1] = CCMatrixCell(components=[4, 8], fasteners=['f8'])
cc_matrix.data[0][2] = CCMatrixCell(components=[5, 8, 21],
                                    fasteners=['f1', 'f5', 'f8'])
cc_matrix.data[0][3] = CCMatrixCell(components=[2, 4, 5, 8, 18, 19, 21],
                                    fasteners=['f5', 'f8'])
cc_matrix.data[0][4] = CCMatrixCell(components=[5, 8], fasteners=['f5', 'f8'])
cc_matrix.data[0][5] = CCMatrixCell(components=[5, 8, 19, 21],
                                    fasteners=['f5', 'f8'])
cc_matrix.data[1][0] = CCMatrixCell(components=[5, 6, 22],
                                    fasteners=['f5', 'f6', 'f2'])
cc_matrix.data[1][1] = CCMatrixCell(components=[1, 3, 5, 6, 18, 19, 22],
                                    fasteners=['f5', 'f6'])
cc_matrix.data[1][2] = CCMatrixCell(components=[1, 5], fasteners=['f5'])
cc_matrix.data[1][3] = CCMatrixCell(components=[3, 6], fasteners=['f6'])
cc_matrix.data[1][4] = CCMatrixCell(components=[5, 6], fasteners=['f5', 'f6'])
cc_matrix.data[1][5] = CCMatrixCell(components=[5, 6, 19, 22],
                                    fasteners=['f5', 'f6'])
cc_matrix.data[2][0] = CCMatrixCell(components=[2, 6], fasteners=['f6'])
cc_matrix.data[2][1] = CCMatrixCell(components=[4, 7], fasteners=['f7'])
cc_matrix.data[2][2] = CCMatrixCell(components=[2, 4, 6, 7, 18, 19, 23],
                                    fasteners=['f6', 'f7'])
cc_matrix.data[2][3] = CCMatrixCell(components=[6, 7, 23],
                                    fasteners=['f3', 'f6', 'f7'])
cc_matrix.data[2][4] = CCMatrixCell(components=[6, 7], fasteners=['f6', 'f7'])
cc_matrix.data[2][5] = CCMatrixCell(components=[6, 7, 19, 23],
                                    fasteners=['f6', 'f7'])
cc_matrix.data[3][0] = CCMatrixCell(components=[1, 3, 7, 8, 18, 19, 24],
                                    fasteners=['f7', 'f8'])
cc_matrix.data[3][1] = CCMatrixCell(components=[7, 8, 24],
                                    fasteners=['f4', 'f7', 'f8'])
cc_matrix.data[3][2] = CCMatrixCell(components=[1, 8], fasteners=['f8'])
cc_matrix.data[3][3] = CCMatrixCell(components=[3, 7], fasteners=['f7'])
cc_matrix.data[3][4] = CCMatrixCell(components=[7, 8], fasteners=['f7', 'f8'])
cc_matrix.data[3][5] = CCMatrixCell(components=[7, 8, 19, 24],
                                    fasteners=['f7', 'f8'])
cc_matrix.data[4][0] = CCMatrixCell(components=[2], fasteners=['f2', 'f5'])
cc_matrix.data[4][1] = CCMatrixCell(components=[1], fasteners=['f5'])
cc_matrix.data[4][2] = CCMatrixCell(components=[1], fasteners=['f1', 'f5'])
cc_matrix.data[4][3] = CCMatrixCell(components=[2], fasteners=['f5'])
cc_matrix.data[4][4] = CCMatrixCell(components=[1, 2], fasteners=['f5'])
cc_matrix.data[4][5] = CCMatrixCell(components=[1, 2], fasteners=['f5'])
cc_matrix.data[5][0] = CCMatrixCell(components=[2], fasteners=['f2', 'f6'])
cc_matrix.data[5][1] = CCMatrixCell(components=[3], fasteners=['f6'])
cc_matrix.data[5][2] = CCMatrixCell(components=[2], fasteners=['f6'])
cc_matrix.data[5][3] = CCMatrixCell(components=[3], fasteners=['f3', 'f6'])
cc_matrix.data[5][4] = CCMatrixCell(components=[2, 3], fasteners=['f6'])
cc_matrix.data[5][5] = CCMatrixCell(components=[2, 3], fasteners=['f6'])
cc_matrix.data[6][0] = CCMatrixCell(components=[3], fasteners=['f7'])
cc_matrix.data[6][1] = CCMatrixCell(components=[4], fasteners=['f4', 'f7'])
cc_matrix.data[6][2] = CCMatrixCell(components=[4], fasteners=['f7'])
cc_matrix.data[6][3] = CCMatrixCell(components=[3], fasteners=['f3', 'f7'])
cc_matrix.data[6][4] = CCMatrixCell(components=[3, 4], fasteners=['f7'])
cc_matrix.data[6][5] = CCMatrixCell(components=[3, 4], fasteners=['f7'])
cc_matrix.data[7][0] = CCMatrixCell(components=[1], fasteners=['f8'])
cc_matrix.data[7][1] = CCMatrixCell(components=[4], fasteners=['f4', 'f8'])
cc_matrix.data[7][2] = CCMatrixCell(components=[1], fasteners=['f1', 'f8'])
cc_matrix.data[7][3] = CCMatrixCell(components=[4], fasteners=['f8'])
cc_matrix.data[7][4] = CCMatrixCell(components=[1, 4], fasteners=['f8'])
cc_matrix.data[7][5] = CCMatrixCell(components=[1, 4], fasteners=['f8'])
cc_matrix.data[8][0] = CCMatrixCell(components=[10, 13, 17, 20, 21],
                                    fasteners=['f13'])
cc_matrix.data[8][1] = CCMatrixCell(components=[12, 16, 17, 20, 21],
                                    fasteners=['f16'])
cc_matrix.data[8][2] = CCMatrixCell(components=[13, 16, 21],
                                    fasteners=['f9', 'f13', 'f16'])
cc_matrix.data[8][3] = CCMatrixCell(components=[10, 12, 13, 16, 17, 18, 20, 21],
                                    fasteners=['f13', 'f16'])
cc_matrix.data[8][4] = CCMatrixCell(components=[13, 16, 17, 21],
                                    fasteners=['f13', 'f16'])
cc_matrix.data[8][5] = CCMatrixCell(components=[13, 16, 20],
                                    fasteners=['f13', 'f16'])
cc_matrix.data[9][0] = CCMatrixCell(components=[13, 14, 22],
                                    fasteners=['f10', 'f13', 'f14'])
cc_matrix.data[9][1] = CCMatrixCell(components=[9, 11, 13, 14, 17, 18, 20, 22],
                                    fasteners=['f13', 'f14'])
cc_matrix.data[9][2] = CCMatrixCell(components=[9, 13, 17, 20, 22],
                                    fasteners=['f13'])
cc_matrix.data[9][3] = CCMatrixCell(components=[11, 14, 17, 20, 22],
                                    fasteners=['f14'])
cc_matrix.data[9][4] = CCMatrixCell(components=[13, 14, 17, 22],
                                    fasteners=['f13', 'f14'])
cc_matrix.data[9][5] = CCMatrixCell(components=[13, 14, 20],
                                    fasteners=['f13', 'f14'])
cc_matrix.data[10][0] = CCMatrixCell(components=[10, 14, 17, 20, 23],
                                     fasteners=['f14'])
cc_matrix.data[10][1] = CCMatrixCell(components=[12, 15, 17, 20, 23],
                                     fasteners=['f15'])
cc_matrix.data[10][2] = CCMatrixCell(
    components=[10, 12, 14, 15, 17, 18, 20, 23], fasteners=['f14', 'f15'])
cc_matrix.data[10][3] = CCMatrixCell(components=[14, 15, 23],
                                     fasteners=['f11', 'f14', 'f15'])
cc_matrix.data[10][4] = CCMatrixCell(components=[14, 15, 17, 23],
                                     fasteners=['f14', 'f15'])
cc_matrix.data[10][5] = CCMatrixCell(components=[14, 15, 20],
                                     fasteners=['f14', 'f15'])
cc_matrix.data[11][0] = CCMatrixCell(components=[9, 11, 15, 16, 17, 18, 20, 24],
                                     fasteners=['f15', 'f16'])
cc_matrix.data[11][1] = CCMatrixCell(components=[15, 16, 23],
                                     fasteners=['f12', 'f15', 'f16'])
cc_matrix.data[11][2] = CCMatrixCell(components=[9, 16, 17, 18, 20, 24],
                                     fasteners=['f16'])
cc_matrix.data[11][3] = CCMatrixCell(components=[11, 15, 17, 18, 20, 24],
                                     fasteners=['f15'])
cc_matrix.data[11][4] = CCMatrixCell(components=[15, 16, 17, 24],
                                     fasteners=['f15', 'f16'])
cc_matrix.data[11][5] = CCMatrixCell(components=[15, 16, 20],
                                     fasteners=['f15', 'f16'])
cc_matrix.data[12][0] = CCMatrixCell(components=[10], fasteners=['f10', 'f13'])
cc_matrix.data[12][1] = CCMatrixCell(components=[9], fasteners=['f13'])
cc_matrix.data[12][2] = CCMatrixCell(components=[9], fasteners=['f9', 'f13'])
cc_matrix.data[12][3] = CCMatrixCell(components=[10], fasteners=['f13'])
cc_matrix.data[12][4] = CCMatrixCell(components=[9, 10], fasteners=['f13'])
cc_matrix.data[12][5] = CCMatrixCell(components=[9, 10], fasteners=['f13'])
cc_matrix.data[13][0] = CCMatrixCell(components=[10], fasteners=['f10', 'f14'])
cc_matrix.data[13][1] = CCMatrixCell(components=[11], fasteners=['f14'])
cc_matrix.data[13][2] = CCMatrixCell(components=[10], fasteners=['f14'])
cc_matrix.data[13][3] = CCMatrixCell(components=[11], fasteners=['f11', 'f14'])
cc_matrix.data[13][4] = CCMatrixCell(components=[10, 11], fasteners=['f14'])
cc_matrix.data[13][5] = CCMatrixCell(components=[10, 11], fasteners=['f14'])
cc_matrix.data[14][0] = CCMatrixCell(components=[11], fasteners=['f15'])
cc_matrix.data[14][1] = CCMatrixCell(components=[12], fasteners=['f12', 'f15'])
cc_matrix.data[14][2] = CCMatrixCell(components=[12], fasteners=['f15'])
cc_matrix.data[14][3] = CCMatrixCell(components=[11], fasteners=['f11', 'f15'])
cc_matrix.data[14][4] = CCMatrixCell(components=[11, 12], fasteners=['f15'])
cc_matrix.data[14][5] = CCMatrixCell(components=[11, 12], fasteners=['f15'])
cc_matrix.data[15][0] = CCMatrixCell(components=[9], fasteners=['f16'])
cc_matrix.data[15][1] = CCMatrixCell(components=[12], fasteners=['f12', 'f16'])
cc_matrix.data[15][2] = CCMatrixCell(components=[9], fasteners=['f9', 'f16'])
cc_matrix.data[15][3] = CCMatrixCell(components=[12], fasteners=['f16'])
cc_matrix.data[15][4] = CCMatrixCell(components=[9, 12], fasteners=['f16'])
cc_matrix.data[15][5] = CCMatrixCell(components=[9, 12], fasteners=['f16'])
cc_matrix.data[16][0] = CCMatrixCell(components=[10, 18], fasteners=[])
cc_matrix.data[16][1] = CCMatrixCell(components=[12, 18], fasteners=[])
cc_matrix.data[16][2] = CCMatrixCell(components=[9, 18], fasteners=[])
cc_matrix.data[16][3] = CCMatrixCell(components=[11, 18], fasteners=[])
cc_matrix.data[16][4] = CCMatrixCell(components=[18], fasteners=[])
cc_matrix.data[16][5] = CCMatrixCell(components=[9, 10, 11, 12], fasteners=[])
cc_matrix.data[17][0] = CCMatrixCell(components=[17], fasteners=[])
cc_matrix.data[17][1] = CCMatrixCell(components=[17], fasteners=[])
cc_matrix.data[17][2] = CCMatrixCell(components=[17], fasteners=[])
cc_matrix.data[17][3] = CCMatrixCell(components=[17], fasteners=[])
cc_matrix.data[17][4] = CCMatrixCell(components=[19], fasteners=[])
cc_matrix.data[17][5] = CCMatrixCell(components=[17], fasteners=[])
cc_matrix.data[18][0] = CCMatrixCell(components=[2, 18], fasteners=[])
cc_matrix.data[18][1] = CCMatrixCell(components=[4, 18], fasteners=[])
cc_matrix.data[18][2] = CCMatrixCell(components=[1, 18], fasteners=[])
cc_matrix.data[18][3] = CCMatrixCell(components=[3, 18], fasteners=[])
cc_matrix.data[18][4] = CCMatrixCell(components=[1, 2, 3, 4], fasteners=[])
cc_matrix.data[18][5] = CCMatrixCell(components=[18], fasteners=[])
cc_matrix.data[19][0] = CCMatrixCell(components=[10], fasteners=[])
cc_matrix.data[19][1] = CCMatrixCell(components=[12], fasteners=[])
cc_matrix.data[19][2] = CCMatrixCell(components=[9], fasteners=[])
cc_matrix.data[19][3] = CCMatrixCell(components=[11], fasteners=[])
cc_matrix.data[19][4] = CCMatrixCell(components=[9, 10, 11, 12], fasteners=[])
cc_matrix.data[19][5] = CCMatrixCell(components=[], fasteners=['f17'])
cc_matrix.data[20][0] = CCMatrixCell(components=[1, 9, 22], fasteners=[])
cc_matrix.data[20][1] = CCMatrixCell(components=[1, 9, 24], fasteners=[])
cc_matrix.data[20][2] = CCMatrixCell(components=[1, 9], fasteners=[])
cc_matrix.data[20][3] = CCMatrixCell(components=[1, 9], fasteners=[])
cc_matrix.data[20][4] = CCMatrixCell(components=[1], fasteners=[])
cc_matrix.data[20][5] = CCMatrixCell(components=[9], fasteners=[])
cc_matrix.data[21][0] = CCMatrixCell(components=[2, 10], fasteners=[])
cc_matrix.data[21][1] = CCMatrixCell(components=[2, 10], fasteners=[])
cc_matrix.data[21][2] = CCMatrixCell(components=[2, 10, 23], fasteners=[])
cc_matrix.data[21][3] = CCMatrixCell(components=[2, 10, 21], fasteners=[])
cc_matrix.data[21][4] = CCMatrixCell(components=[2], fasteners=[])
cc_matrix.data[21][5] = CCMatrixCell(components=[10], fasteners=[])
cc_matrix.data[22][0] = CCMatrixCell(components=[3, 11, 22], fasteners=[])
cc_matrix.data[22][1] = CCMatrixCell(components=[3, 11, 24], fasteners=[])
cc_matrix.data[22][2] = CCMatrixCell(components=[3, 11], fasteners=[])
cc_matrix.data[22][3] = CCMatrixCell(components=[3, 11], fasteners=[])
cc_matrix.data[22][4] = CCMatrixCell(components=[3], fasteners=[])
cc_matrix.data[22][5] = CCMatrixCell(components=[11], fasteners=[])
cc_matrix.data[23][0] = CCMatrixCell(components=[4, 12], fasteners=[])
cc_matrix.data[23][1] = CCMatrixCell(components=[4, 12], fasteners=[])
cc_matrix.data[23][2] = CCMatrixCell(components=[4, 12, 21], fasteners=[])
cc_matrix.data[23][3] = CCMatrixCell(components=[4, 12, 23], fasteners=[])
cc_matrix.data[23][4] = CCMatrixCell(components=[4], fasteners=[])
cc_matrix.data[23][5] = CCMatrixCell(components=[12], fasteners=[])

cf_matrix = CFMatrix(data=[
    CFMatrixEntry(fastener='f1', direction=3),
    CFMatrixEntry(fastener='f2', direction=1),
    CFMatrixEntry(fastener='f3', direction=4),
    CFMatrixEntry(fastener='f4', direction=2),
    CFMatrixEntry(fastener='f5', direction=1),
    CFMatrixEntry(fastener='f6', direction=1),
    CFMatrixEntry(fastener='f7', direction=2),
    CFMatrixEntry(fastener='f8', direction=2),
    CFMatrixEntry(fastener='f9', direction=3),
    CFMatrixEntry(fastener='f10', direction=1),
    CFMatrixEntry(fastener='f11', direction=4),
    CFMatrixEntry(fastener='f12', direction=2),
    CFMatrixEntry(fastener='f13', direction=1),
    CFMatrixEntry(fastener='f14', direction=1),
    CFMatrixEntry(fastener='f15', direction=2),
    CFMatrixEntry(fastener='f16', direction=2),
    CFMatrixEntry(fastener='f17', direction=6),
])

mc_matrix = MCMatrix(num_components=24, num_directions=6)
mc_matrix.data[0][0] = MCMatrixCell(components=[21, 22], fasteners=['f1', 'f2'])
mc_matrix.data[0][1] = MCMatrixCell(components=[21, 24], fasteners=['f1', 'f4'])
mc_matrix.data[0][2] = MCMatrixCell(components=[], fasteners=[])
mc_matrix.data[0][3] = MCMatrixCell(components=[3, 6, 7, 22, 23, 24],
                                    fasteners=['f2', 'f3', 'f4', 'f6', 'f7'])
mc_matrix.data[0][4] = MCMatrixCell(components=[], fasteners=['f1', 'f2', 'f4'])
mc_matrix.data[0][5] = MCMatrixCell(components=[9, 13, 16, 17, 18, 20],
                                    fasteners=['f1', 'f2', 'f4', 'f10', 'f12',
                                               'f13', 'f16', 'f17'])
mc_matrix.data[1][0] = MCMatrixCell(components=[], fasteners=[])
mc_matrix.data[1][1] = MCMatrixCell(components=[4, 7, 8, 21, 23, 24],
                                    fasteners=['f1', 'f3', 'f7', 'f8'])
mc_matrix.data[1][2] = MCMatrixCell(components=[21, 22], fasteners=['f1', 'f2'])
mc_matrix.data[1][3] = MCMatrixCell(components=[22, 23], fasteners=['f2', 'f3'])
mc_matrix.data[1][4] = MCMatrixCell(components=[],
                                    fasteners=['f1', 'f2', 'f3', 'f8'])
mc_matrix.data[1][5] = MCMatrixCell(components=[10, 13, 14, 17, 18, 20],
                                    fasteners=['f1', 'f2', 'f3', 'f9', 'f10',
                                               'f11', 'f13', 'f14', 'f17'])
mc_matrix.data[2][0] = MCMatrixCell(components=[22, 23],
                                    fasteners=['f2', 'f3', 'f6'])
mc_matrix.data[2][1] = MCMatrixCell(components=[23, 24], fasteners=['f3', 'f4'])
mc_matrix.data[2][2] = MCMatrixCell(components=[1, 5, 8, 21, 22, 24],
                                    fasteners=['f1', 'f2', 'f4', 'f5', 'f8'])
mc_matrix.data[2][3] = MCMatrixCell(components=[],
                                    fasteners=[])
mc_matrix.data[2][4] = MCMatrixCell(components=[], fasteners=['f2', 'f3', 'f4'])
mc_matrix.data[2][5] = MCMatrixCell(components=[11, 14, 15, 17, 18, 20],
                                    fasteners=['f2', 'f3', 'f4', 'f10', 'f11',
                                               'f12', 'f14', 'f15', 'f17'])
mc_matrix.data[3][0] = MCMatrixCell(components=[2, 5, 6, 21, 22, 23],
                                    fasteners=['f1', 'f2', 'f3', 'f5', 'f6'])
mc_matrix.data[3][1] = MCMatrixCell(components=[],
                                    fasteners=[])
mc_matrix.data[3][2] = MCMatrixCell(components=[21, 24], fasteners=['f1', 'f4'])
mc_matrix.data[3][3] = MCMatrixCell(components=[23, 24], fasteners=['f3', 'f4'])
mc_matrix.data[3][4] = MCMatrixCell(components=[], fasteners=['f1', 'f3', 'f4'])
mc_matrix.data[3][5] = MCMatrixCell(components=[12, 15, 16, 17, 18, 20],
                                    fasteners=['f1', 'f3', 'f4', 'f9', 'f11',
                                               'f12', 'f15', 'f16', 'f17'])
mc_matrix.data[4][0] = MCMatrixCell(components=[22], fasteners=['f1'])
mc_matrix.data[4][1] = MCMatrixCell(
    components=[2, 4, 8, 17, 18, 19, 21, 22, 24],
    fasteners=['f1', 'f2', 'f4', 'f8'])
mc_matrix.data[4][2] = MCMatrixCell(components=[21], fasteners=['f2'])
mc_matrix.data[4][3] = MCMatrixCell(
    components=[1, 3, 6, 17, 18, 19, 21, 22, 23],
    fasteners=['f1', 'f2', 'f3', 'f6'])
mc_matrix.data[4][4] = MCMatrixCell(components=[21, 22], fasteners=['f1', 'f2'])
mc_matrix.data[4][5] = MCMatrixCell(components=[9, 10, 13, 21, 22],
                                    fasteners=['f1', 'f2', 'f9', 'f10', 'f13'])
mc_matrix.data[5][0] = MCMatrixCell(components=[22], fasteners=['f3'])
mc_matrix.data[5][1] = MCMatrixCell(
    components=[2, 4, 7, 17, 18, 19, 22, 23, 24],
    fasteners=['f2', 'f3', 'f4', 'f7'])
mc_matrix.data[5][2] = MCMatrixCell(components=[1, 5, 17, 18, 19, 21, 22, 23],
                                    fasteners=['f1', 'f2', 'f3', 'f5'])
mc_matrix.data[5][3] = MCMatrixCell(components=[23], fasteners=['f2'])
mc_matrix.data[5][4] = MCMatrixCell(components=[22, 23], fasteners=['f2', 'f3'])
mc_matrix.data[5][5] = MCMatrixCell(components=[10, 11, 14, 23],
                                    fasteners=['f2', 'f3', 'f10', 'f11', 'f14'])
mc_matrix.data[6][0] = MCMatrixCell(
    components=[2, 4, 6, 17, 18, 19, 22, 23, 24], fasteners=['f3', 'f4', 'f6'])
mc_matrix.data[6][1] = MCMatrixCell(components=[24], fasteners=['f3'])
mc_matrix.data[6][2] = MCMatrixCell(
    components=[1, 3, 8, 17, 18, 19, 21, 23, 24],
    fasteners=['f1', 'f3', 'f4', 'f8'])
mc_matrix.data[6][3] = MCMatrixCell(components=[23], fasteners=['f4'])
mc_matrix.data[6][4] = MCMatrixCell(components=[23, 24], fasteners=['f3', 'f4'])
mc_matrix.data[6][5] = MCMatrixCell(components=[11, 12, 15, 23, 24],
                                    fasteners=['f3', 'f11', 'f12', 'f15'])
mc_matrix.data[7][0] = MCMatrixCell(
    components=[2, 4, 5, 17, 18, 19, 21, 22, 24],
    fasteners=['f1', 'f2', 'f4', 'f5'])
mc_matrix.data[7][1] = MCMatrixCell(components=[24], fasteners=['f1'])
mc_matrix.data[7][2] = MCMatrixCell(components=[21], fasteners=['f4'])
mc_matrix.data[7][3] = MCMatrixCell(components=[1, 3, 17, 18, 19, 21, 23, 24],
                                    fasteners=['f1', 'f3', 'f4', 'f7'])
mc_matrix.data[7][4] = MCMatrixCell(components=[21, 24], fasteners=['f1', 'f4'])
mc_matrix.data[7][5] = MCMatrixCell(components=[9, 12, 16, 21, 24],
                                    fasteners=['f1', 'f4', 'f9', 'f12', 'f16'])
mc_matrix.data[8][0] = MCMatrixCell(components=[22],
                                    fasteners=['f9', 'f10'])
mc_matrix.data[8][1] = MCMatrixCell(components=[24],
                                    fasteners=['f9', 'f12'])
mc_matrix.data[8][2] = MCMatrixCell(components=[],
                                    fasteners=[])
mc_matrix.data[8][3] = MCMatrixCell(components=[11, 14, 15, 22, 23, 24],
                                    fasteners=['f10', 'f11', 'f12', 'f14',
                                               'f15', 'f17'])
mc_matrix.data[8][4] = MCMatrixCell(components=[1, 5, 8, 9, 18],
                                    fasteners=['f1', 'f2', 'f4', 'f5', 'f8',
                                               'f9', 'f10', 'f12'])
mc_matrix.data[8][5] = MCMatrixCell(components=[],
                                    fasteners=['f9', 'f10', 'f12'])
mc_matrix.data[9][0] = MCMatrixCell(components=[21],
                                    fasteners=[])
mc_matrix.data[9][1] = MCMatrixCell(components=[12, 15, 16, 21, 23, 24],
                                    fasteners=['f9', 'f11', 'f12', 'f15', 'f16',
                                               'f17'])
mc_matrix.data[9][2] = MCMatrixCell(components=[21],
                                    fasteners=['f9', 'f10'])
mc_matrix.data[9][3] = MCMatrixCell(components=[23],
                                    fasteners=['f10', 'f11'])
mc_matrix.data[9][4] = MCMatrixCell(components=[2, 5, 6, 18, 19, 20],
                                    fasteners=['f1', 'f2', 'f3', 'f5', 'f6',
                                               'f9', 'f10', 'f11', 'f17'])
mc_matrix.data[9][5] = MCMatrixCell(components=[],
                                    fasteners=['f9', 'f10', 'f11'])
mc_matrix.data[10][0] = MCMatrixCell(components=[22],
                                     fasteners=['f10', 'f11'])
mc_matrix.data[10][1] = MCMatrixCell(components=[24],
                                     fasteners=['f11', 'f12'])
mc_matrix.data[10][2] = MCMatrixCell(
    components=[9, 12, 13, 16, 21, 22, 23, 24],
    fasteners=['f9', 'f10', 'f12', 'f13', 'f16', 'f17'])
mc_matrix.data[10][3] = MCMatrixCell(components=[],
                                     fasteners=[])
mc_matrix.data[10][4] = MCMatrixCell(components=[3, 6, 7, 17, 18, 19, 20],
                                     fasteners=['f2', 'f3', 'f4', 'f6', 'f7',
                                                'f10', 'f11', 'f12', 'f17'])
mc_matrix.data[10][5] = MCMatrixCell(components=[],
                                     fasteners=['f10', 'f11', 'f12'])
mc_matrix.data[11][0] = MCMatrixCell(components=[10, 13, 14, 21, 22, 23],
                                     fasteners=['f9', 'f10', 'f11', 'f12',
                                                'f13', 'f14', 'f17'])
mc_matrix.data[11][1] = MCMatrixCell(components=[24],
                                     fasteners=[])
mc_matrix.data[11][2] = MCMatrixCell(components=[14, 21],
                                     fasteners=['f9', 'f12'])
mc_matrix.data[11][3] = MCMatrixCell(components=[12, 23],
                                     fasteners=['f11'])
mc_matrix.data[11][4] = MCMatrixCell(components=[4, 7, 8, 18, 19, 20],
                                     fasteners=['f1', 'f3', 'f4', 'f7', 'f8',
                                                'f9', 'f11', 'f12', 'f17'])
mc_matrix.data[11][5] = MCMatrixCell(components=[],
                                     fasteners=['f9', 'f11', 'f12'])
mc_matrix.data[12][0] = MCMatrixCell(components=[22], fasteners=['f9'])
mc_matrix.data[12][1] = MCMatrixCell(components=[10, 12, 16, 21, 22, 24],
                                     fasteners=['f9', 'f10', 'f12', 'f16'])
mc_matrix.data[12][2] = MCMatrixCell(components=[21], fasteners=['f10'])
mc_matrix.data[12][3] = MCMatrixCell(components=[9, 11, 14, 21, 22, 23],
                                     fasteners=['f9', 'f10', 'f11', 'f14'])
mc_matrix.data[12][4] = MCMatrixCell(components=[1, 2, 13, 21, 22],
                                     fasteners=['f1', 'f2', 'f9', 'f10'])
mc_matrix.data[12][5] = MCMatrixCell(components=[21, 22],
                                     fasteners=['f9', 'f10'])
mc_matrix.data[13][0] = MCMatrixCell(components=[22], fasteners=['f11'])
mc_matrix.data[13][1] = MCMatrixCell(components=[10, 12, 15, 22, 23, 24],
                                     fasteners=['f10', 'f11', 'f12', 'f15'])
mc_matrix.data[13][2] = MCMatrixCell(components=[9, 13, 21, 22, 23],
                                     fasteners=['f9', 'f10', 'f11', 'f13'])
mc_matrix.data[13][3] = MCMatrixCell(components=[23], fasteners=['f10'])
mc_matrix.data[13][4] = MCMatrixCell(components=[2, 3, 14, 22, 23],
                                     fasteners=['f2', 'f3', 'f10', 'f11'])
mc_matrix.data[13][5] = MCMatrixCell(components=[22, 23],
                                     fasteners=['f10', 'f11'])
mc_matrix.data[14][0] = MCMatrixCell(components=[10, 12, 14, 22, 23, 24],
                                     fasteners=['f10', 'f11', 'f12', 'f14'])
mc_matrix.data[14][1] = MCMatrixCell(components=[24], fasteners=['f11'])
mc_matrix.data[14][2] = MCMatrixCell(components=[9, 11, 16, 21, 23, 24],
                                     fasteners=['f9', 'f11', 'f12', 'f16'])
mc_matrix.data[14][3] = MCMatrixCell(components=[23], fasteners=['f12'])
mc_matrix.data[14][4] = MCMatrixCell(components=[3, 4, 15, 23, 24],
                                     fasteners=['f3', 'f4', 'f11', 'f12'])
mc_matrix.data[14][5] = MCMatrixCell(components=[23, 24],
                                     fasteners=['f11', 'f12'])
mc_matrix.data[15][0] = MCMatrixCell(components=[10, 12, 13, 21, 22, 24],
                                     fasteners=['f9', 'f10', 'f12', 'f13'])
mc_matrix.data[15][1] = MCMatrixCell(components=[24], fasteners=['f9', 'f15'])
mc_matrix.data[15][2] = MCMatrixCell(components=[21], fasteners=['f12'])
mc_matrix.data[15][3] = MCMatrixCell(components=[9, 11, 15, 21, 23, 24],
                                     fasteners=['f9', 'f11', 'f12', 'f15'])
mc_matrix.data[15][4] = MCMatrixCell(components=[1, 4, 16, 21, 24],
                                     fasteners=['f1', 'f4', 'f9', 'f12'])
mc_matrix.data[15][5] = MCMatrixCell(components=[21, 24],
                                     fasteners=['f9', 'f12'])
mc_matrix.data[16][0] = MCMatrixCell(components=[13, 14, 22],
                                     fasteners=['f9', 'f10', 'f11', 'f13',
                                                'f14'])
mc_matrix.data[16][1] = MCMatrixCell(components=[15, 16, 24],
                                     fasteners=['f9', 'f11', 'f12', 'f15',
                                                'f16'])
mc_matrix.data[16][2] = MCMatrixCell(components=[13, 16, 21],
                                     fasteners=['f9', 'f10', 'f12', 'f13',
                                                'f16'])
mc_matrix.data[16][3] = MCMatrixCell(components=[14, 15, 23],
                                     fasteners=['f10', 'f11', 'f12', 'f14',
                                                'f15'])
mc_matrix.data[16][4] = MCMatrixCell(components=[1, 2, 3, 4, 19],
                                     fasteners=['f1', 'f2', 'f3', 'f4'])
mc_matrix.data[16][5] = MCMatrixCell(components=[20, 21, 22, 23, 24],
                                     fasteners=['f9', 'f10', 'f11', 'f12',
                                                'f17'])
mc_matrix.data[17][0] = MCMatrixCell(components=[2, 5, 6, 10, 13, 14, 22],
                                     fasteners=['f1', 'f2', 'f3', 'f5', 'f6',
                                                'f9', 'f10', 'f11', 'f13',
                                                'f14'])
mc_matrix.data[17][1] = MCMatrixCell(
    components=[4, 7, 8, 9, 11, 12, 15, 16, 24],
    fasteners=['f1', 'f3', 'f4', 'f7', 'f8', 'f9', 'f11', 'f12', 'f15', 'f16'])
mc_matrix.data[17][2] = MCMatrixCell(components=[1, 5, 8, 9, 13, 16, 21],
                                     fasteners=['f1', 'f2', 'f4', 'f5', 'f8',
                                                'f9', 'f10', 'f12', 'f13',
                                                'f16'])
mc_matrix.data[17][3] = MCMatrixCell(components=[3, 6, 7, 11, 14, 15, 23],
                                     fasteners=['f2', 'f3', 'f4', 'f6', 'f7',
                                                'f10', 'f11', 'f12', 'f14',
                                                'f15'])
mc_matrix.data[17][4] = MCMatrixCell(components=[1, 2, 3, 4],
                                     fasteners=['f1', 'f2', 'f3', 'f4'])
mc_matrix.data[17][5] = MCMatrixCell(
    components=[9, 10, 11, 12, 20, 21, 22, 23, 24],
    fasteners=['f9', 'f10', 'f11', 'f12', 'f17'])
mc_matrix.data[18][0] = MCMatrixCell(components=[1, 3, 4, 5, 6, 22],
                                     fasteners=['f1', 'f2', 'f3', 'f4', 'f5',
                                                'f6'])
mc_matrix.data[18][1] = MCMatrixCell(components=[1, 2, 3, 7, 8, 24],
                                     fasteners=['f1', 'f2', 'f3', 'f4', 'f7',
                                                'f8'])
mc_matrix.data[18][2] = MCMatrixCell(components=[2, 3, 4, 5, 8, 21],
                                     fasteners=['f2', 'f3', 'f4', 'f5', 'f8'])
mc_matrix.data[18][3] = MCMatrixCell(components=[1, 2, 3, 4, 6, 7, 23],
                                     fasteners=['f1', 'f2', 'f3', 'f4', 'f6',
                                                'f7'])
mc_matrix.data[18][4] = MCMatrixCell(components=[],
                                     fasteners=['f1', 'f2', 'f3', 'f4'])
mc_matrix.data[18][5] = MCMatrixCell(
    components=[9, 10, 11, 12, 19, 20, 21, 22, 23, 24],
    fasteners=['f9', 'f10', 'f11', 'f12', 'f17'])
mc_matrix.data[19][0] = MCMatrixCell(components=[13, 14, 22],
                                     fasteners=['f9', 'f10', 'f11', 'f13',
                                                'f14', 'f17'])
mc_matrix.data[19][1] = MCMatrixCell(components=[15, 16, 24],
                                     fasteners=['f9', 'f11', 'f12', 'f15',
                                                'f16', 'f17'])
mc_matrix.data[19][2] = MCMatrixCell(components=[13, 16, 21],
                                     fasteners=['f9', 'f10', 'f12', 'f13',
                                                'f16', 'f17'])
mc_matrix.data[19][3] = MCMatrixCell(components=[14, 15, 23],
                                     fasteners=['f10', 'f11', 'f12', 'f14',
                                                'f15', 'f17'])
mc_matrix.data[19][4] = MCMatrixCell(components=[1, 2, 3, 4, 17, 18, 19],
                                     fasteners=['f1', 'f2', 'f3', 'f4', 'f9',
                                                'f10', 'f11', 'f12'])
mc_matrix.data[19][5] = MCMatrixCell(components=[], fasteners=[])
mc_matrix.data[20][0] = MCMatrixCell(components=[5, 13],
                                     fasteners=['f2', 'f5', 'f13'])
mc_matrix.data[20][1] = MCMatrixCell(components=[4, 8, 16],
                                     fasteners=['f4', 'f8', 'f16'])
mc_matrix.data[20][2] = MCMatrixCell(components=[], fasteners=['f1', 'f9'])
mc_matrix.data[20][3] = MCMatrixCell(
    components=[2, 3, 4, 10, 11, 12, 17, 18, 19, 22, 23, 24],
    fasteners=['f1', 'f2', 'f4', 'f10', 'f11', 'f12'])
mc_matrix.data[20][4] = MCMatrixCell(components=[5, 8],
                                     fasteners=['f1', 'f5', 'f8'])
mc_matrix.data[20][5] = MCMatrixCell(components=[13, 16],
                                     fasteners=['f9', 'f13', 'f16'])
mc_matrix.data[21][0] = MCMatrixCell(components=[], fasteners=['f2', 'f10'])
mc_matrix.data[21][1] = MCMatrixCell(components=[1, 3, 4, 12, 17, 18, 19],
                                     fasteners=['f1', 'f3', 'f4', 'f12'])
mc_matrix.data[21][2] = MCMatrixCell(components=[1, 5, 13, 21],
                                     fasteners=['f1', 'f5', 'f13'])
mc_matrix.data[21][3] = MCMatrixCell(components=[3, 6, 14, 23],
                                     fasteners=['f3', 'f6', 'f14'])
mc_matrix.data[21][4] = MCMatrixCell(components=[5, 6],
                                     fasteners=['f2', 'f5', 'f6'])
mc_matrix.data[21][5] = MCMatrixCell(components=[13, 14],
                                     fasteners=['f10', 'f13', 'f14'])
mc_matrix.data[22][0] = MCMatrixCell(components=[2, 6, 10, 14],
                                     fasteners=['f2', 'f6', 'f10', 'f14'])
mc_matrix.data[22][1] = MCMatrixCell(components=[7, 15],
                                     fasteners=['f3', 'f7', 'f11', 'f15'])
mc_matrix.data[22][2] = MCMatrixCell(
    components=[1, 2, 4, 10, 12, 17, 18, 19, 21, 22, 24],
    fasteners=['f1', 'f2', 'f4', 'f10', 'f12'])
mc_matrix.data[22][3] = MCMatrixCell(components=[], fasteners=['f3', 'f11'])
mc_matrix.data[22][4] = MCMatrixCell(components=[6, 7],
                                     fasteners=['f3', 'f6', 'f7'])
mc_matrix.data[22][5] = MCMatrixCell(components=[14, 15],
                                     fasteners=['f11', 'f14', 'f15'])
mc_matrix.data[23][0] = MCMatrixCell(
    components=[1, 2, 3, 9, 10, 11, 17, 18, 19, 22],
    fasteners=['f1', 'f2', 'f3', 'f9', 'f10', 'f11'])
mc_matrix.data[23][1] = MCMatrixCell(components=[], fasteners=['f4', 'f12'])
mc_matrix.data[23][2] = MCMatrixCell(components=[1, 8, 9, 16],
                                     fasteners=['f1', 'f8', 'f9', 'f16'])
mc_matrix.data[23][3] = MCMatrixCell(components=[7, 15],
                                     fasteners=['f4', 'f7', 'f12', 'f15'])
mc_matrix.data[23][4] = MCMatrixCell(components=[7, 8],
                                     fasteners=['f4', 'f7', 'f8'])
mc_matrix.data[23][5] = MCMatrixCell(components=[15, 16],
                                     fasteners=['f12', 'f15', 'f16'])

mf_matrix = MFMatrix(num_fasteners=17, num_directions=6)
mf_matrix.data[0][0] = MFMatrixEntry(component=None)
mf_matrix.data[0][1] = MFMatrixEntry(component=None)
mf_matrix.data[0][2] = MFMatrixEntry(component=None)
mf_matrix.data[0][3] = MFMatrixEntry(component=None)
mf_matrix.data[0][4] = MFMatrixEntry(component=None)
mf_matrix.data[0][5] = MFMatrixEntry(component=None)
mf_matrix.data[1][0] = MFMatrixEntry(component=None)
mf_matrix.data[1][1] = MFMatrixEntry(component=None)
mf_matrix.data[1][2] = MFMatrixEntry(component=None)
mf_matrix.data[1][3] = MFMatrixEntry(component=None)
mf_matrix.data[1][4] = MFMatrixEntry(component=None)
mf_matrix.data[1][5] = MFMatrixEntry(component=None)
mf_matrix.data[2][0] = MFMatrixEntry(component=None)
mf_matrix.data[2][1] = MFMatrixEntry(component=None)
mf_matrix.data[2][2] = MFMatrixEntry(component=None)
mf_matrix.data[2][3] = MFMatrixEntry(component=None)
mf_matrix.data[2][4] = MFMatrixEntry(component=None)
mf_matrix.data[2][5] = MFMatrixEntry(component=None)
mf_matrix.data[3][0] = MFMatrixEntry(component=None)
mf_matrix.data[3][1] = MFMatrixEntry(component=None)
mf_matrix.data[3][2] = MFMatrixEntry(component=None)
mf_matrix.data[3][3] = MFMatrixEntry(component=None)
mf_matrix.data[3][4] = MFMatrixEntry(component=None)
mf_matrix.data[3][5] = MFMatrixEntry(component=None)
mf_matrix.data[4][0] = MFMatrixEntry(component=2)
mf_matrix.data[4][1] = MFMatrixEntry(component=None)
mf_matrix.data[4][2] = MFMatrixEntry(component=None)
mf_matrix.data[4][3] = MFMatrixEntry(component=None)
mf_matrix.data[4][4] = MFMatrixEntry(component=None)
mf_matrix.data[4][5] = MFMatrixEntry(component=None)
mf_matrix.data[5][0] = MFMatrixEntry(component=2)
mf_matrix.data[5][1] = MFMatrixEntry(component=None)
mf_matrix.data[5][2] = MFMatrixEntry(component=None)
mf_matrix.data[5][3] = MFMatrixEntry(component=None)
mf_matrix.data[5][4] = MFMatrixEntry(component=None)
mf_matrix.data[5][5] = MFMatrixEntry(component=None)
mf_matrix.data[6][0] = MFMatrixEntry(component=None)
mf_matrix.data[6][1] = MFMatrixEntry(component=4)
mf_matrix.data[6][2] = MFMatrixEntry(component=None)
mf_matrix.data[6][3] = MFMatrixEntry(component=None)
mf_matrix.data[6][4] = MFMatrixEntry(component=None)
mf_matrix.data[6][5] = MFMatrixEntry(component=None)
mf_matrix.data[7][0] = MFMatrixEntry(component=None)
mf_matrix.data[7][1] = MFMatrixEntry(component=4)
mf_matrix.data[7][2] = MFMatrixEntry(component=None)
mf_matrix.data[7][3] = MFMatrixEntry(component=None)
mf_matrix.data[7][4] = MFMatrixEntry(component=None)
mf_matrix.data[7][5] = MFMatrixEntry(component=None)
mf_matrix.data[8][0] = MFMatrixEntry(component=None)
mf_matrix.data[8][1] = MFMatrixEntry(component=None)
mf_matrix.data[8][2] = MFMatrixEntry(component=None)
mf_matrix.data[8][3] = MFMatrixEntry(component=None)
mf_matrix.data[8][4] = MFMatrixEntry(component=None)
mf_matrix.data[8][5] = MFMatrixEntry(component=None)
mf_matrix.data[9][0] = MFMatrixEntry(component=None)
mf_matrix.data[9][1] = MFMatrixEntry(component=None)
mf_matrix.data[9][2] = MFMatrixEntry(component=None)
mf_matrix.data[9][3] = MFMatrixEntry(component=None)
mf_matrix.data[9][4] = MFMatrixEntry(component=None)
mf_matrix.data[9][5] = MFMatrixEntry(component=None)
mf_matrix.data[10][0] = MFMatrixEntry(component=None)
mf_matrix.data[10][1] = MFMatrixEntry(component=None)
mf_matrix.data[10][2] = MFMatrixEntry(component=None)
mf_matrix.data[10][3] = MFMatrixEntry(component=None)
mf_matrix.data[10][4] = MFMatrixEntry(component=None)
mf_matrix.data[10][5] = MFMatrixEntry(component=None)
mf_matrix.data[11][0] = MFMatrixEntry(component=None)
mf_matrix.data[11][1] = MFMatrixEntry(component=None)
mf_matrix.data[11][2] = MFMatrixEntry(component=None)
mf_matrix.data[11][3] = MFMatrixEntry(component=None)
mf_matrix.data[11][4] = MFMatrixEntry(component=None)
mf_matrix.data[11][5] = MFMatrixEntry(component=None)
mf_matrix.data[12][0] = MFMatrixEntry(component=2)
mf_matrix.data[12][1] = MFMatrixEntry(component=None)
mf_matrix.data[12][2] = MFMatrixEntry(component=None)
mf_matrix.data[12][3] = MFMatrixEntry(component=None)
mf_matrix.data[12][4] = MFMatrixEntry(component=None)
mf_matrix.data[12][5] = MFMatrixEntry(component=None)
mf_matrix.data[13][0] = MFMatrixEntry(component=2)
mf_matrix.data[13][1] = MFMatrixEntry(component=None)
mf_matrix.data[13][2] = MFMatrixEntry(component=None)
mf_matrix.data[13][3] = MFMatrixEntry(component=None)
mf_matrix.data[13][4] = MFMatrixEntry(component=None)
mf_matrix.data[13][5] = MFMatrixEntry(component=None)
mf_matrix.data[14][0] = MFMatrixEntry(component=None)
mf_matrix.data[14][1] = MFMatrixEntry(component=4)
mf_matrix.data[14][2] = MFMatrixEntry(component=None)
mf_matrix.data[14][3] = MFMatrixEntry(component=None)
mf_matrix.data[14][4] = MFMatrixEntry(component=None)
mf_matrix.data[14][5] = MFMatrixEntry(component=None)
mf_matrix.data[15][0] = MFMatrixEntry(component=None)
mf_matrix.data[15][1] = MFMatrixEntry(component=4)
mf_matrix.data[15][2] = MFMatrixEntry(component=None)
mf_matrix.data[15][3] = MFMatrixEntry(component=None)
mf_matrix.data[15][4] = MFMatrixEntry(component=None)
mf_matrix.data[15][5] = MFMatrixEntry(component=None)
mf_matrix.data[16][0] = MFMatrixEntry(component=None)
mf_matrix.data[16][1] = MFMatrixEntry(component=None)
mf_matrix.data[16][2] = MFMatrixEntry(component=None)
mf_matrix.data[16][3] = MFMatrixEntry(component=None)
mf_matrix.data[16][4] = MFMatrixEntry(component=None)
mf_matrix.data[16][5] = MFMatrixEntry(component=None)

pc_matrix = PCMatrix(num_components=24, num_directions=6)
pc_matrix.data[0][0] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[0][1] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[0][2] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[0][3] = PCMatrixEntry(blocking_components=13)
pc_matrix.data[0][4] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[0][5] = PCMatrixEntry(blocking_components=10)
pc_matrix.data[1][0] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[1][1] = PCMatrixEntry(blocking_components=13)
pc_matrix.data[1][2] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[1][3] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[1][4] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[1][5] = PCMatrixEntry(blocking_components=10)
pc_matrix.data[2][0] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[2][1] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[2][2] = PCMatrixEntry(blocking_components=13)
pc_matrix.data[2][3] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[2][4] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[2][5] = PCMatrixEntry(blocking_components=10)
pc_matrix.data[3][0] = PCMatrixEntry(blocking_components=13)
pc_matrix.data[3][1] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[3][2] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[3][3] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[3][4] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[3][5] = PCMatrixEntry(blocking_components=10)
pc_matrix.data[4][0] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[4][1] = PCMatrixEntry(blocking_components=9)
pc_matrix.data[4][2] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[4][3] = PCMatrixEntry(blocking_components=9)
pc_matrix.data[4][4] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[4][5] = PCMatrixEntry(blocking_components=7)
pc_matrix.data[5][0] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[5][1] = PCMatrixEntry(blocking_components=9)
pc_matrix.data[5][2] = PCMatrixEntry(blocking_components=9)
pc_matrix.data[5][3] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[5][4] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[5][5] = PCMatrixEntry(blocking_components=7)
pc_matrix.data[6][0] = PCMatrixEntry(blocking_components=9)
pc_matrix.data[6][1] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[6][2] = PCMatrixEntry(blocking_components=9)
pc_matrix.data[6][3] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[6][4] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[6][5] = PCMatrixEntry(blocking_components=7)
pc_matrix.data[7][0] = PCMatrixEntry(blocking_components=9)
pc_matrix.data[7][1] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[7][2] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[7][3] = PCMatrixEntry(blocking_components=9)
pc_matrix.data[7][4] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[7][5] = PCMatrixEntry(blocking_components=7)
pc_matrix.data[8][0] = PCMatrixEntry(blocking_components=4)
pc_matrix.data[8][1] = PCMatrixEntry(blocking_components=4)
pc_matrix.data[8][2] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[8][3] = PCMatrixEntry(blocking_components=14)
pc_matrix.data[8][4] = PCMatrixEntry(blocking_components=10)
pc_matrix.data[8][5] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[9][0] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[9][1] = PCMatrixEntry(blocking_components=14)
pc_matrix.data[9][2] = PCMatrixEntry(blocking_components=4)
pc_matrix.data[9][3] = PCMatrixEntry(blocking_components=4)
pc_matrix.data[9][4] = PCMatrixEntry(blocking_components=10)
pc_matrix.data[9][5] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[10][0] = PCMatrixEntry(blocking_components=4)
pc_matrix.data[10][1] = PCMatrixEntry(blocking_components=4)
pc_matrix.data[10][2] = PCMatrixEntry(blocking_components=14)
pc_matrix.data[10][3] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[10][4] = PCMatrixEntry(blocking_components=10)
pc_matrix.data[10][5] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[11][0] = PCMatrixEntry(blocking_components=14)
pc_matrix.data[11][1] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[11][2] = PCMatrixEntry(blocking_components=4)
pc_matrix.data[11][3] = PCMatrixEntry(blocking_components=4)
pc_matrix.data[11][4] = PCMatrixEntry(blocking_components=10)
pc_matrix.data[11][5] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[12][0] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[12][1] = PCMatrixEntry(blocking_components=9)
pc_matrix.data[12][2] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[12][3] = PCMatrixEntry(blocking_components=9)
pc_matrix.data[12][4] = PCMatrixEntry(blocking_components=7)
pc_matrix.data[12][5] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[13][0] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[13][1] = PCMatrixEntry(blocking_components=9)
pc_matrix.data[13][2] = PCMatrixEntry(blocking_components=9)
pc_matrix.data[13][3] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[13][4] = PCMatrixEntry(blocking_components=7)
pc_matrix.data[13][5] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[14][0] = PCMatrixEntry(blocking_components=9)
pc_matrix.data[14][1] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[14][2] = PCMatrixEntry(blocking_components=9)
pc_matrix.data[14][3] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[14][4] = PCMatrixEntry(blocking_components=7)
pc_matrix.data[14][5] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[15][0] = PCMatrixEntry(blocking_components=9)
pc_matrix.data[15][1] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[15][2] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[15][3] = PCMatrixEntry(blocking_components=9)
pc_matrix.data[15][4] = PCMatrixEntry(blocking_components=7)
pc_matrix.data[15][5] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[16][0] = PCMatrixEntry(blocking_components=1)
pc_matrix.data[16][1] = PCMatrixEntry(blocking_components=1)
pc_matrix.data[16][2] = PCMatrixEntry(blocking_components=1)
pc_matrix.data[16][3] = PCMatrixEntry(blocking_components=1)
pc_matrix.data[16][4] = PCMatrixEntry(blocking_components=6)
pc_matrix.data[16][5] = PCMatrixEntry(blocking_components=5)
pc_matrix.data[17][0] = PCMatrixEntry(blocking_components=1)
pc_matrix.data[17][1] = PCMatrixEntry(blocking_components=1)
pc_matrix.data[17][2] = PCMatrixEntry(blocking_components=1)
pc_matrix.data[17][3] = PCMatrixEntry(blocking_components=1)
pc_matrix.data[17][4] = PCMatrixEntry(blocking_components=5)
pc_matrix.data[17][5] = PCMatrixEntry(blocking_components=6)
pc_matrix.data[18][0] = PCMatrixEntry(blocking_components=1)
pc_matrix.data[18][1] = PCMatrixEntry(blocking_components=1)
pc_matrix.data[18][2] = PCMatrixEntry(blocking_components=1)
pc_matrix.data[18][3] = PCMatrixEntry(blocking_components=1)
pc_matrix.data[18][4] = PCMatrixEntry(blocking_components=4)
pc_matrix.data[18][5] = PCMatrixEntry(blocking_components=7)
pc_matrix.data[19][0] = PCMatrixEntry(blocking_components=1)
pc_matrix.data[19][1] = PCMatrixEntry(blocking_components=1)
pc_matrix.data[19][2] = PCMatrixEntry(blocking_components=1)
pc_matrix.data[19][3] = PCMatrixEntry(blocking_components=1)
pc_matrix.data[19][4] = PCMatrixEntry(blocking_components=11)
pc_matrix.data[19][5] = PCMatrixEntry(blocking_components=0)
pc_matrix.data[20][0] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[20][1] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[20][2] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[20][3] = PCMatrixEntry(blocking_components=16)
pc_matrix.data[20][4] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[20][5] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[21][0] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[21][1] = PCMatrixEntry(blocking_components=16)
pc_matrix.data[21][2] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[21][3] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[21][4] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[21][5] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[22][0] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[22][1] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[22][2] = PCMatrixEntry(blocking_components=16)
pc_matrix.data[22][3] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[22][4] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[22][5] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[23][0] = PCMatrixEntry(blocking_components=16)
pc_matrix.data[23][1] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[23][2] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[23][3] = PCMatrixEntry(blocking_components=2)
pc_matrix.data[23][4] = PCMatrixEntry(blocking_components=3)
pc_matrix.data[23][5] = PCMatrixEntry(blocking_components=3)
