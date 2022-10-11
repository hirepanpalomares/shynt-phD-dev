from Shynt.api_py.Mesh.mesh import GlobalMesh, FineMesh


def make_mesh(cell, global_mesh_type="", local_mesh_type=""):
    """
    Helper method to construct the global and local meshes

    Probabbly the right way to get the GLOBAL MESH  and LOCAL MESH 
    is the following:
        1. Build the coarse nodes by getting the coordinates of the surfaces,
            being these circles, rectangles, squares or triangles, etc, etc.
        2. Now that you have the coordinates of all of these nodes we make for 
            each of these refine the space (pin, region etc) i.e. local mesh
        3. Once you refine (local meshes) of every corse node, determine which 
            are different to be able to compute the probabilities in serpent

    """
    
    global_mesh = GlobalMesh(cell, global_mesh_type)
    # print(global_mesh.coarse_nodes)
    local_mesh = FineMesh(global_mesh.coarse_nodes, local_mesh_type)
    # print(local_mesh.fine_nodes)
    
    

    cell.global_mesh = global_mesh
    # print(global_mesh.surface_relation)
    # print(cell.surface_relation)
    cell.local_mesh = local_mesh

    return cell