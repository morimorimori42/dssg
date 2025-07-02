from flask import Flask, request, jsonify
from carbon.carbonvisualization import create_co2_visualization
from dssg.dssg_single_target import find_dssg_single_target
from dssg.dssg_visualization import create_pgv
from simpletest.matrices_window import (
    cc_matrix, cf_matrix, mc_matrix,
    mf_matrix, pc_matrix
)

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_disassembly():
    try:
        # Get target component from request JSON
        data = request.get_json()
        t = int(data.get("t", 1))  # default to 1 if not provided
        d_dir = [1, 2, 3, 4, 5, 6]
        final_emissions_data = []

        for d in d_dir:
            dg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                20, 21, 22, 23, 24, 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7',
                'f8', 'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17']
            dg_products = {
                1: 'aluminium', 2: 'aluminium', 3: 'aluminium', 4: 'aluminium', 5: 'alum_corner', 6: 'alum_corner',
                7: 'alum_corner', 8: 'alum_corner', 9: 'aluminium', 10: 'aluminium', 11: 'aluminium', 12: 'aluminium',
                13: 'alum_corner', 14: 'alum_corner', 15: 'alum_corner', 16: 'alum_corner', 17: 'gasket', 18: 'glass',
                19: 'gasket', 20: 'gasket', 21: 'glazingbead', 22: 'glazingbead', 23: 'glazingbead', 24: 'glazingbead',
                'f1': 'screw', 'f2': 'screw', 'f3': 'screw', 'f4': 'screw', 'f5': 'glue',
                'f6': 'glue', 'f7': 'glue', 'f8': 'glue', 'f9': 'screw', 'f10': 'screw',
                'f11': 'screw', 'f12': 'screw', 'f13': 'glue', 'f14': 'glue',
                'f15': 'glue', 'f16': 'glue', 'f17': 'nail'
            }
            dg_quantities = {
                1: 1.20, 2: 1.20, 3: 1.20, 4: 1.20, 5: 0.17, 6: 0.17,
                7: 0.17, 8: 0.17, 9: 1.20, 10: 1.20, 11: 1.20, 12: 1.20,
                13: 0.17, 14: 0.17, 15: 0.17, 16: 0.17, 17: 0.000032, 18: 0.64,
                19: 0.000032, 20: 0.000032, 21: 1.20, 22: 1.20, 23: 1.20, 24: 1.20,
                'f1': 2, 'f2': 2, 'f3': 2, 'f4': 2, 'f5': 0.1,
                'f6': 0.1, 'f7': 0.1, 'f8': 0.1, 'f9': 2, 'f10': 2,
                'f11': 2, 'f12': 2, 'f13': 0.1, 'f14': 0.1,
                'f15': 0.1, 'f16': 0.1, 'f17': 4
            }
            dssg, G, dssg_list, final_emissions = find_dssg_single_target(t, d, dg,
                                                                          dg_products,
                                                                          dg_quantities,
                                                                          cc_matrix,
                                                                          cf_matrix,
                                                                          mc_matrix,
                                                                          mf_matrix,
                                                                          pc_matrix)
            create_pgv(G, f"graph-{t}-d_dir-{d}")
            final_emissions_data.append(final_emissions.model_dump())

        # create_co2_visualization(final_emissions_data, t)

        return jsonify({
            "message": "Process completed successfully",
            "target_component": t,
            "emissions_data": final_emissions_data
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
