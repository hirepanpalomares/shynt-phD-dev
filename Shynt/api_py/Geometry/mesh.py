from Shynt.api_py.materials import Material
from Shynt.api_py.Geometry.cells import Cell
from Shynt.api_py.Geometry.universes import Pin, SquareLattice, Universe

class StructuredMesh:
    """
        A structured mesh has all of its coarse nodes 
        with the same geometry.
    """
    def __init__(self):
        pass


class GlobalMesh(StructuredMesh):

    """
    
    
    """
    def __init__(self, cell, mesh):
        super().__init__()
        self.__cell = cell
        self.__mesh = mesh
        self.coarse_nodes = self.__create_nodes()
    
    def __create_nodes(self):
        nodes = None
        if isinstance(self.__mesh, list):
            return self.__mesh_by_points(self.__mesh)
        elif isinstance(self.__mesh, str):
            if self.__mesh == "pin_cell":
                nodes = self.__pin_cell_mesh()
        return nodes
    
    def __mesh_by_points(self, points):
        pass


    def __pin_cell_mesh(self):
        # if cell is filled with universe check and ensure that 
        # the universe is the Lattice
        #print(self.__cell)
        coarse_nodes = {}
        node_counter = 1
        universe = self.__cell.content
        if isinstance(universe, SquareLattice):
            for y in range(universe.ny):
                for x in range(universe.nx):
                    coarse_nodes[node_counter] = universe.array[y][x]
                    node_counter += 1
        elif isinstance(universe, Pin):
            coarse_nodes[node_counter] = self.__cell
        else:
            print("*** Error Trying to build coarse mesh no Lattice nor Pin universe provided *** ")
            raise SystemExit
        return coarse_nodes

    def __str__(self):
        return self.type


class LocalMesh(StructuredMesh):

    def __init__(self, coarse_nodes, local_mesh_type):
        super().__init__()
        self.type = local_mesh_type
        self.coarse_nodes = coarse_nodes
        self.fine_nodes = {}
        self.generate_fine_nodes()

    def generate_fine_nodes(self):
        if self.type == "material":
            for key, node in self.coarse_nodes.items():
                self.fine_nodes[key] = self.get_material_nodes(node)
        else:
            return None
    
    def get_material_nodes(self, node):
        """
            Method to extract the fine nodes by material from a given cell
            
            Parameters
            -------------------------------------------------------------
            node        :   Cell type filled with universe or material
            -------------------------------------------------------------

            returns Array(node_1, node_2, ..., node_N)
            
            each node is a Cell type
        """
        fill = node.content
        if isinstance(fill, Universe):
            if isinstance(fill, Pin):
                # get a cell for each level of the pin
                fine_nodes = [l.cell for l in fill.pin_levels]
                return fine_nodes
        elif isinstance(fill, Material):
            print("Material here")
            return [node]
        else:
            print("***Error**** Cell has not been filled with no Material nor Universe ")
            print(f"Cell: {node.name}")
            raise SystemExit
            


    def __str__(self):
        return self.type
    

class Node:

    def __init__(self) -> None:
        pass

class CoarseNode(Node):

    def __init__(self) -> None:
        super().__init__()

class FineNode(Node):

    def __init__(self) -> None:
        super().__init__()
        self.from_coarse_node = None


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
    local_mesh = LocalMesh(global_mesh.coarse_nodes, local_mesh_type)
    # print(local_mesh.fine_nodes)
    

    cell.global_mesh = global_mesh.coarse_nodes
    cell.local_mesh = local_mesh.fine_nodes

    return cell