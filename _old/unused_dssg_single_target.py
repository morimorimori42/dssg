""" function to find disassembly sequence structure graphs (dssg) for a single target """
from collections import deque
import networkx as nx
from models.results import DSSGNode


def find_dssg_single_target(t: int, d_dir: int, dg, cc_matrix, cf_matrix,
               mc_matrix, mf_matrix, pc_matrix) -> tuple[dict[int, DSSGNode], nx.DiGraph, list[int]]:
    """ find dssg for a given target component t and direction d_dir """
    dssg = {}
    dssg_list = []
    queue = deque()

    # Start process, select target component out of DG, choose disassembly direction
    dssg[t] = DSSGNode(type='c', d_dir=d_dir, parent=None, blocked_components=None)
    queue.append(t)

    # create an empty graph
    G = nx.DiGraph()

    # Processing Loop - get p from the queue
    while queue:
        p = queue.popleft()
        p_type = dssg[p].type
        dssg_list.append(p)


        # add a node to the graph for the current part
        G.add_node(p, label=str(p), **dssg[p].dict())

        if p_type == 'c':
            # Rule 2 when p is a component c
            cc_row = cc_matrix.data[p - 1]
            d_dir = dssg[p].d_dir
            cc_cell = cc_row[d_dir - 1] if cc_row else None

            # components
            if cc_cell and cc_cell.components:
                for c_prime in cc_cell.components:
                    if c_prime in dssg:
                        continue
                    if c_prime in dg:
                        # Check if c_prime can only be disassembled in a different direction than d_dir
                        mc_row = mc_matrix.data[c_prime - 1]
                        index = dg.index(
                            c_prime)  # Get the index of the element
                        d_dir_prime = d_dir  # Assuming the same disassembly direction for the connected component
                        dssg[c_prime] = DSSGNode(type='c', d_dir=d_dir_prime, parent=p, blocked_components=None)
                        queue.append(c_prime)
                        del dg[index]

                        # add an edge to the graph from the current part to the connected part
                        G.add_edge(p, c_prime, label=str(d_dir_prime))

            # Rule 3 for fasteners
            if cc_cell and cc_cell.fasteners:
                for f_prime in cc_cell.fasteners:
                    if f_prime in dssg:
                        continue  # Fix: Use continue instead of break

                    cf_entry = next((entry for entry in cf_matrix.data if
                                     entry.fastener == f_prime), None)
                    if cf_entry:
                        index = dg.index(
                            f_prime)  # Get the index of the element
                        d_dir_prime = cf_entry.direction
                        dssg[f_prime] = DSSGNode(type='f', d_dir=d_dir_prime, parent=p, blocked_components=None)
                        queue.append(f_prime)
                        del dg[index]

                        # Add an edge to the graph from the current part to the connected part
                        G.add_edge(p, f_prime, label=str(d_dir_prime))

            # Check the fasteners that are connected to the current component in a different direction than the current component
            for i in range(len(cc_row)):
                if i == d_dir - 1:
                    continue
                cc_cell = cc_row[i]
                if cc_cell and cc_cell.fasteners:
                    for f_prime in cc_cell.fasteners:
                        if f_prime in dssg:
                            continue  # Fix: Use continue instead of break

                        cf_entry = next((entry for entry in cf_matrix.data if
                                         entry.fastener == f_prime), None)
                        if cf_entry:
                            # Check if f_prime is connected to a different component than the current component in the same direction as the current component
                            for j in range(len(cc_matrix.data)):
                                if j == p - 1:
                                    continue
                                cc_row_j = cc_matrix.data[j]
                                cc_cell_j = cc_row_j[
                                    d_dir - 1] if cc_row_j else None
                                if cc_cell_j and f_prime in cc_cell_j.fasteners:
                                    # Check if the different component can only be disassembled in a different direction than d_dir
                                    mc_row = mc_matrix.data[j]
                                    if any(mc_cell and mc_cell.components for
                                           mc_cell in mc_row[:d_dir - 1]) or \
                                            any(mc_cell and mc_cell.components
                                                for mc_cell in mc_row[d_dir:]):
                                        break
                            else:
                                # f_prime is not connected to a different component in the same direction as the current component
                                index = dg.index(
                                    f_prime)  # Get the index of the element
                                d_dir_prime = cf_entry.direction
                                dssg[f_prime] = DSSGNode(type='f', d_dir=d_dir_prime, parent=p, blocked_components=None)
                                queue.append(f_prime)
                                del dg[index]

                                # Add an edge to the graph from the current part to the connected part
                                G.add_edge(p, f_prime, label=str(d_dir_prime))

        elif p_type == 'f':
            # Rule 4
            cf_entry = next((entry for entry in cf_matrix.data if
                             entry.fastener == p), None)
            if cf_entry:
                d_dir = dssg[p].d_dir
                cf_entry_index = cf_matrix.data.index(cf_entry)
                mf_row = mf_matrix.data[cf_entry_index]

                # Check the components that are connected to the current fastener in the same direction as the current fastener
                mf_cell = mf_row[d_dir - 1] if mf_row else None
                if mf_cell and mf_cell.component:
                    c_prime = mf_cell.component
                    if c_prime in dssg:
                        continue
                    if c_prime in dg:
                        # Check if c_prime can only be disassembled in a different direction than d_dir
                        mc_row = mc_matrix.data[c_prime - 1]
                        if any(mc_cell and mc_cell.components for
                               mc_cell in mc_row[:d_dir - 1]) or \
                                any(mc_cell and mc_cell.components
                                    for mc_cell in mc_row[d_dir:]):
                            continue

                        index = dg.index(
                            c_prime)  # Get the index of the element
                        d_dir_prime = d_dir  # Assuming the same disassembly direction for the connected component
                        dssg[c_prime] = DSSGNode(type='c', d_dir=d_dir_prime, parent=c_prime, blocked_components=None)
                        queue.append(c_prime)
                        del dg[index]

                        # Add an edge to the graph from the current fastener to the connected component
                        G.add_edge(p, c_prime, label=str(d_dir))

                # Check the components that are connected to the current fastener in a different direction than the current fastener
                for i in range(len(mf_row)):
                    if i == d_dir - 1:
                        continue
                    mf_cell = mf_row[i]
                    if mf_cell and mf_cell.component:
                        c_prime = mf_cell.component
                        if c_prime in dssg:
                            continue
                        if c_prime in dg:
                            # Check if c_prime can only be disassembled in a different direction than i+1
                            mc_row = mc_matrix.data[c_prime - 1]
                            if any(mc_cell and mc_cell.components
                                   for mc_cell in mc_row[:i]) or \
                                    any(
                                        mc_cell and mc_cell.components
                                        for mc_cell in
                                        mc_row[i + 1:]):
                                continue

                            index = dg.index(
                                c_prime)  # Get the index of the element
                            d_dir_prime = i + 1  # Assuming the same disassembly direction for the connected component
                            dssg[c_prime] = DSSGNode(type='c', d_dir=d_dir_prime, parent=c_prime, blocked_components=None)
                            queue.append(c_prime)
                            del dg[index]

                            # Add an edge to the graph from the current fastener to the connected component
                            G.add_edge(p, c_prime, label=str(i+1))

    # Finalize DSSG
    for p in dssg:
        p_type = dssg[p].type
        if p_type == 'c':
            pc_entries = [entry for sublist in pc_matrix.data for entry in
                          sublist if
                          entry and entry.blocking_components == p]  # Get a list of matching PCMatrixEntry objects
            if pc_entries:
                pc_entry = pc_entries[
                    0]  # Extract the first matching PCMatrixEntry object from the list
                dssg[p].blocked_components = pc_entry.blocking_components

    return dssg, G, dssg_list