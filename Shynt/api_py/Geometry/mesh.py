import numpy as np
from Shynt.api_py.Geometry.mesh_nodes import CoarseNode, FineNode

from Shynt.api_py.materials import Material
from Shynt.api_py.Geometry.universes import HexagonalLatticeTypeX, Pin, SquareLattice, Universe

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
        self.__mesh_type = mesh
        self.coarse_nodes_map = []
        self.coarse_nodes = self.__create_nodes()
    
    def __create_nodes(self):
        nodes = None
        if isinstance(self.__mesh_type, list):
            return self.__mesh_type_by_points(self.__mesh_type)
        elif isinstance(self.__mesh_type, str):
            if self.__mesh_type == "pin_cell":
                nodes = self.__pin_cell_mesh()
        
        return nodes
    
    def __mesh_by_points(self, points):
        return {}

  

    def __pin_cell_mesh(self):
        # if cell is filled with universe check and ensure that 
        # the universe is the Lattice
        #print(self.__cell)
        coarse_nodes = {}
        map_nodes = []
        node_counter = 1
        universe = self.__cell.content
        if isinstance(universe, SquareLattice) or isinstance(universe, HexagonalLatticeTypeX):
            for y in range(universe.ny):
                map_row = []
                for x in range(universe.nx):
                    map_row.append(node_counter)
                    pin_cell_id = universe.array[y][x]
                    pin_cell = universe.cells[pin_cell_id]
                    coarse_nodes[node_counter] = CoarseNode(pin_cell)
                    node_counter += 1
                map_nodes.append(map_row)
            self.coarse_nodes_map = np.array(map_nodes)
        elif isinstance(universe, Pin):
            coarse_nodes[node_counter] = CoarseNode(self.__cell)
            self.coarse_nodes_map = np.array([[1]])
        else:
            print("*** Error Trying to build coarse mesh no Lattice nor Pin universe provided *** ")
            raise SystemExit
        return coarse_nodes

    # def __str__(self):
    #     return self.__mesh_type


class FineMesh(StructuredMesh):

    def __init__(self, coarse_nodes, local_mesh_type):
        super().__init__()
        self.type = local_mesh_type
        self.coarse_nodes = coarse_nodes
        self.fine_nodes = self.generate_fine_nodes()

    def generate_fine_nodes(self):
        if self.type == "material":
            fine_nodes = {}
            for n_id, coarse_node in self.coarse_nodes.items():
                nodes = self.get_material_nodes(coarse_node)
                fine_nodes[n_id] = nodes
                coarse_node.setFineNodes(nodes)
            return fine_nodes
        else:
            return None
    
    def get_material_nodes(self, coarse_node):
        """
            Method to extract the fine nodes by material from a given cell
            
            Parameters
            -------------------------------------------------------------
            node        :   Cell type filled with universe or material
            -------------------------------------------------------------

            returns Array(node_1, node_2, ..., node_N)
            
            each node is a Cell type
        """
        fill = coarse_node.cell.content
        if isinstance(fill, Universe):
            # if isinstance(fill, Pin):
            # get a cell for each level of the pin
            fine_nodes = {}
            universe_cells = fill.cells
            for c_id, cell in universe_cells.items():
                fine_node = FineNode(cell)
                fine_nodes[c_id] = fine_node
            return fine_nodes
        elif isinstance(fill, Material):
            print("Material here")
            fine_node = FineNode(coarse_node.cell)
            fine_nodes = {
                coarse_node.cell.id: fine_node
            }
            return fine_nodes
        else:
            print("***Error**** Cell has not been filled with no Material nor Universe ")
            print(f"Cell: {coarse_node.cell.name}")
            raise SystemExit
            


    def __str__(self):
        return self.type
    


