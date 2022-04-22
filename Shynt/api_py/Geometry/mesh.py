import numpy as np

from Shynt.api_py.Geometry.regions import SurfaceSide
from Shynt.api_py.Geometry.surfaces import InfiniteSquareCylinderZ, Surface
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
        if isinstance(universe, SquareLattice):
            for y in range(universe.ny):
                map_row = []
                for x in range(universe.nx):
                    map_row.append(node_counter)
                    pin_cell = universe.array[y][x]
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


class LocalMesh(StructuredMesh):

    def __init__(self, coarse_nodes, local_mesh_type):
        super().__init__()
        self.type = local_mesh_type
        self.coarse_nodes = coarse_nodes
        self.fine_nodes = self.generate_fine_nodes()

    def generate_fine_nodes(self):
        print(self.type)
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
            if isinstance(fill, Pin):
                # get a cell for each level of the pin
                fine_nodes = {}
                for l in fill.pin_levels:
                    fine_node = FineNode(l.cell)
                    fine_nodes[l.cell.id] = fine_node
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
    

class Node:

    def __init__(self) -> None:
        pass

class CoarseNode(Node):

    def __init__(self, cell) -> None:
        super().__init__()
        self.__cell = cell
        
        self.__surfaces = self.__getSurfaces()                      # Dictionary of surface classes {id: <Surface class>}
        self.__surface_ids = list(self.__surfaces.keys())           # Array with surface ids
        self.__surface_areas = self.__getSurfaceAreas()             # Dictionary of surfaces areas {id: area}
        self.__surface_directions = self.__getSurfaceDirections()   # Dictionary with the direction of the surfaces
        self.__fine_nodes = {}                                      # Dictionary of cell classes {id: <FineNode class>}
        self.__fine_nodes_ids = []                                  # Array with fine nodes ids
        self.__fine_nodes_volume = {}                               # Dictionary of fine nodes volume {id: vol}


    def __getSurfaces(self):
        region = self.cell.region

        relation = {}
        if isinstance(region, SurfaceSide):
            relation = region.surface.get_surface_relation()


        return relation

    def __getSurfaceAreas(self):
        areas = {}
        
        region = self.cell.region

        if isinstance(region, SurfaceSide):
            surface = self.cell.region.surface
            if isinstance(surface, InfiniteSquareCylinderZ):
                areas = surface.evaluate_surface_area() 
        else: 
            for s_id in self.surface_ids:
                a = self.surfaces[s_id].evaluate_surface_area()
                areas[s_id] = a
        return areas
    
    def __getSurfaceDirections(self):
        directions = {}

        region = self.cell.region
        if isinstance(region, SurfaceSide):
            surface = self.cell.region.surface
            if isinstance(surface, InfiniteSquareCylinderZ):
                directions = surface.get_surface_orientation()
        return directions


    def setFineNodes(self, fine_nodes):
        for id_, node in fine_nodes.items():
            self.__fine_nodes[id_] = node
            self.__fine_nodes_volume[id_] = node.cell.volume
            self.__fine_nodes_ids.append(id_)
        

    @property
    def cell(self):
        return self.__cell

    @property
    def surfaces(self):
        return self.__surfaces

    @property
    def surface_ids(self):
        return self.__surface_ids

    @property
    def surface_areas(self):
        return self.__surface_areas

    @property
    def surface_directions(self):
        return self.__surface_directions

    @property
    def fine_nodes(self):
        return self.__fine_nodes

    @property
    def fine_nodes_ids(self):
        return self.__fine_nodes_ids

    @property
    def fine_nodes_volume(self):
        return self.__fine_nodes_volume
    
        


class FineNode(Node):

    def __init__(self, cell) -> None:
        super().__init__()
        self.__cell = cell
        self.from_coarse_node = None
    
    @property
    def cell(self):
        return self.__cell



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
    local_mesh = LocalMesh(global_mesh.coarse_nodes, local_mesh_type)
    # print(local_mesh.fine_nodes)
    
    

    cell.global_mesh = global_mesh
    # print(global_mesh.surface_relation)
    # print(cell.surface_relation)
    cell.local_mesh = local_mesh

    return cell