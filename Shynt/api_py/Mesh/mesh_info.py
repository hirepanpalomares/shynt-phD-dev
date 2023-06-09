from Shynt.api_py.Geometry.utilities_geometry import get_equal_nodes, get_surface_equivalence
from Shynt.api_py.materials import Material



class MeshInfo:

    def __init__(self, coarse_nodes, fine_nodes, coarse_nodes_map):
        self.__coarse_nodes = coarse_nodes
        self.__fine_nodes = fine_nodes
        self.coarse_nodes_map = coarse_nodes_map
        # ------------------------------------------------------------
        self.coarse_order = list(coarse_nodes.keys())
        self.all_regions_order = []
        self.all_surfaces_order = []
        self.all_regions_vol = {}
        self.all_surfaces_area = {}
        self.region_coarse_rel = {}
        self.coarse_region_rel = {}
        self.coarse_surface_rel = {}
        self.equal_nodes_rel = {}
        self.equivalence_region_rel = {}
        self.equivalence_surface_rel = {}
        self.region_type_rel = {}
        self.region_type_rel_switched = {}
        self.equal_nodes = {}
        self.type_system = ""

        self.__get_volume_and_areas()
        self.__get_coarse_to_fine_rel_info()
        self.__get_region_content_relation()
        self.__equal_nodes()
        self.__equal_regions()
        self.__equal_surfaces()
        db = True

    def __get_volume_and_areas(self):
        for n_id in self.__coarse_nodes.keys():
            
            regions = self.__coarse_nodes[n_id].fine_nodes_ids
            surfaces = self.__coarse_nodes[n_id].surface_ids
            # print(surfaces)
            vols = self.__coarse_nodes[n_id].fine_nodes_volume
            areas = self.__coarse_nodes[n_id].surface_areas
            # print_ = [print(key, value) for key,value in self.__coarse_nodes[n_id].geometry_info["surfaces_for_detectors"]["boundary_guide"].items()]

            self.all_regions_vol.update(vols)
            self.all_surfaces_area.update(areas)
            self.all_regions_order += regions
            self.all_surfaces_order += surfaces

    def __get_coarse_to_fine_rel_info(self):
        for n_id in self.__coarse_nodes.keys():
            
            regions = self.__coarse_nodes[n_id].fine_nodes_ids
            surfaces = self.__coarse_nodes[n_id].surface_ids

            self.coarse_region_rel[n_id] = regions
            self.coarse_surface_rel[n_id] = surfaces

    def __get_region_content_relation(self):
        """
            This method is to generate a relation of what regions 
            have what material and what is the region of the material

            This is used to know which regions correspond to each other
            between two coarse nodes that are of the same type
            
        """
        for n_id, coarse_node in self.__coarse_nodes.items():
            self.region_type_rel[n_id] = {
                
            }
            self.region_type_rel_switched[n_id] = {}
            for r_id, fine_node  in self.__fine_nodes[n_id].items():
                self.region_coarse_rel[r_id] = n_id
                region_cell = fine_node.cell
                material_name = region_cell.content.name
                if material_name == "void": continue
                self.region_type_rel[n_id][material_name + f"_{region_cell.id}"] = r_id
                self.region_type_rel_switched[n_id][r_id] = material_name  + f"_{region_cell.id}"
                
      

    def __equal_nodes(self):
        """
            Method to get all the nodes that are of the same type
            and also the variable self.equal_nodes_rel

            
        """
        self.equal_nodes = get_equal_nodes(self.__coarse_nodes, self.__fine_nodes)
        # print(self.equal_nodes)

        # Turn equal_nodes into a list
        self.equal_nodes = [bin_ for bin_ in self.equal_nodes.values()]
        for bin_ in self.equal_nodes:
            head = bin_[0]
            for node_id in bin_:
                self.equal_nodes_rel[node_id] = head
    

    def __equal_regions(self):
        """
            The criteria for which a region is equal to other
            is based on  the order of the regions since the regions 
            are declared in the same order


        """
        for n_id, n_eq_id in self.equal_nodes_rel.items():
            type_regs = list(self.region_type_rel_switched[n_eq_id].keys())
            for r, reg_id in enumerate(self.coarse_region_rel[n_id]):
                reg_eq = type_regs[r]
                self.equivalence_region_rel[reg_id] = reg_eq
        


    def __equal_surfaces(self):
        """
            The criteria for which a surface is equal to other
            is based on  the order of the surfaces since the surfaces 
            are declared in the same order


        """
        for n_id, n_eq_id in self.equal_nodes_rel.items():
            node_ = self.__coarse_nodes[n_id]
            node_eq = self.__coarse_nodes[n_eq_id]
            surface_rel = get_surface_equivalence(node_, node_eq)
            # print(":"*75)
            # print(f"node = {n_id}\t node_equal = {n_eq_id}")
            # print("surface relation: ")
            # print(surface_rel)
            # print_surf_rel = [print(key,value)  for key,value in surface_rel.items()]
            # print("surface guide:")
            # print_guide = [print(key,value) for key,value in node_.geometry_info["surfaces_for_detectors"]["boundary_guide"].items()]
            # print("surface areas:")
            # print_areas = [print(key,value) for key,value in node_.geometry_info["surfaces_for_detectors"]["boundary_surfaces_areas"].items()]

            self.equivalence_surface_rel.update(surface_rel)
        




