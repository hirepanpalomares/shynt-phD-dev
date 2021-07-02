class StructuredMesh:

    def __init__(self):
        pass
    

class GlobalMesh(StructuredMesh):

    def __init__(self, cell, mesh):
        super().__init__()
        self.__cell = cell
        self.__mesh = mesh
        self.__nodes = self.__create_nodes()
    
    def __create_nodes(self):
        if isinstance(self.__mesh, list):
            return self.__mesh_by_points(self.__mesh)
        elif isinstance(self.__mesh, str):
            return self.__mesh_by_type(self.__mesh)
        return None
    
    def __mesh_by_points(self, points):
        pass

    def __mesh_by_type(self, mesh_type):
        if mesh_type == "pin_cell":
            return self.__pin_cell_mesh()
        return None

    def __pin_cell_mesh(self):
        print(self.__cell)
        # is cell is filled with universe check that the universe is the Lattice
        return []

    def __str__(self):
        return self.type


class LocalMesh(StructuredMesh):

    def __init__(self, global_mesh):
        super().__init__()
        self.type = "material_by_material"


    def __str__(self):
        return self.type
    


def make_mesh(cell, global_mesh=[], local_mesh=[]):
    """
    Helper method to construct the global and local meshes
    """
    global_mesh = GlobalMesh(cell, global_mesh)
    local_mesh = LocalMesh(global_mesh)

    

    cell.global_mesh = global_mesh
    cell.local_mesh = local_mesh

    return cell