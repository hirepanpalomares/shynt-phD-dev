import numpy as np
import math

from Shynt.api_py.Mesh.mesh_nodes import CoarseNode, FineNode

from Shynt.api_py.materials import Material
from Shynt.api_py.Geometry.universes import HexagonalLatticeTypeX, Pin, SquareLattice, Universe
from Shynt.api_py.Geometry.cells import Cell
from Shynt.api_py.Geometry.surfaces import PlaneParametric, PieQuadrant

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
                    pin_cell_id = universe.array[y][x]
                    map_row.append(node_counter)
                    pin_cell = universe.cells[pin_cell_id]
                    coarse_node = CoarseNode(pin_cell)
                    coarse_node.id = node_counter
                    coarse_nodes[node_counter] = coarse_node
                    node_counter += 1
                map_nodes.append(map_row)
            self.coarse_nodes_map = np.array(map_nodes)
        elif isinstance(universe, HexagonalLatticeTypeX):
            for y in range(universe.ny):
                map_row = []
                for x in range(universe.nx):
                    pin_cell_id = universe.array[y][x]
                    if pin_cell_id is None:
                        map_row.append(None)
                        continue
                    map_row.append(node_counter)
                    pin_cell = universe.cells[pin_cell_id]
                    coarse_node = CoarseNode(pin_cell)
                    coarse_node.id = node_counter
                    coarse_nodes[node_counter] = coarse_node
                    node_counter += 1
                map_nodes.append(map_row)
            self.coarse_nodes_map = np.array(map_nodes)
        elif isinstance(universe, Pin):
            coarse_node = CoarseNode(self.__cell)
            coarse_node.id = node_counter
            coarse_nodes[node_counter] = coarse_node
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
        fine_nodes = {}
        if self.type == "material":
            for n_id, coarse_node in self.coarse_nodes.items():
                nodes = self.get_material_nodes(coarse_node)
                fine_nodes[n_id] = nodes
                coarse_node.setFineNodes(nodes)
            return fine_nodes
        elif self.type == "fuel_cross":
            for n_id, coarse_node in self.coarse_nodes.items():
                nodes = self.get_fuel_cross_nodes(coarse_node)
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
            

    def get_fuel_cross_nodes(self, coarse_node):
        """
            Method to extract the fine nodes from a given cell in the form of
            a cross in the fuel, with the other regions (coolant) intact
            
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
                if cell.content.isFuel:
                    # Generate cell in a Pie slice form, clock-wise numeration
                    circle = cell.region.surface

                    x0, y0 = circle.center
                    z0 = 0
                    x2, y2 = 0, 0
                    z2 = 1
                    
                    pT = PlaneParametric(x0, y0, z0, x0, y0+circle.radius, z0, x2, y2, z2)
                    pR = PlaneParametric(x0, y0, z0, x0+circle.radius, y0, z0, x2, y2, z2)
                    pB = PlaneParametric(x0, y0, z0, x0, y0-circle.radius, z0, x2, y2, z2)
                    pL = PlaneParametric(x0, y0, z0, x0-circle.radius, y0, z0, x2, y2, z2)

                    

                    volume_pie_slice = math.pi * circle.radius * circle.radius / 4
                    pie_top_left_region = -PieQuadrant(circle, pT, pL, "top_left")          # f1
                    pie_top_right_region = -PieQuadrant(circle, pT, pR, "top_right")        # f2
                    pie_bottom_right_region = -PieQuadrant(circle, pB, pR, "bottom_right")  # f3
                    pie_bottom_left_region = -PieQuadrant(circle, pB, pL, "bottom_left")    # f4
            
                    pie_cell_top_left = Cell(name="pie_cell_top_left", fill=cell.content, region=pie_top_left_region, universe=cell.universe, volume=volume_pie_slice)
                    pie_cell_top_right = Cell(name="pie_cell_top_right", fill=cell.content, region=pie_top_right_region, universe=cell.universe, volume=volume_pie_slice)
                    pie_cell_bottom_right = Cell(name="pie_cell_bottom_right", fill=cell.content, region=pie_bottom_right_region, universe=cell.universe, volume=volume_pie_slice)
                    pie_cell_bottom_left = Cell(name="pie_cell_bottom_left", fill=cell.content, region=pie_bottom_left_region, universe=cell.universe, volume=volume_pie_slice)

                    # Generate an instance of FineNode with the pie slice
                    fine_nodes[pie_cell_top_left.id] = FineNode(pie_cell_top_left)
                    fine_nodes[pie_cell_top_right.id] = FineNode(pie_cell_top_right)
                    fine_nodes[pie_cell_bottom_left.id] = FineNode(pie_cell_bottom_left)
                    fine_nodes[pie_cell_bottom_right.id] = FineNode(pie_cell_bottom_right)
                else:
                    fine_node = FineNode(cell)
                    fine_nodes[c_id] = fine_node
            new_cells = {fn_id: fn.cell for fn_id,fn in fine_nodes.items()}
            coarse_node.cell.content.cells = new_cells
            return fine_nodes
        
        else:
            print("***Error**** Cell has not been filled with Universe Pin, to divide the fuel in a cross")
            print(f"Cell: {coarse_node.cell.name}")
            raise SystemExit
        pass

    def __str__(self):
        return self.type
    


