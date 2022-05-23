from .utilities import get_equal_nodes
from .utilities import get_surface_equality



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
        self.__get_equalities()
        db = True

    def __get_volume_and_areas(self):
        for n_id in self.__coarse_nodes.keys():
            
            regions = self.__coarse_nodes[n_id].fine_nodes_ids
            surfaces = self.__coarse_nodes[n_id].surface_ids
            vols = self.__coarse_nodes[n_id].fine_nodes_volume
            areas = self.__coarse_nodes[n_id].surface_areas

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
        for n_id, coarse_node in self.__coarse_nodes.items():
            self.region_type_rel[n_id] = {}
            self.region_type_rel_switched[n_id] = {}
            for r_id, fine_node  in self.__fine_nodes[n_id].items():
                self.region_coarse_rel[r_id] = n_id
                region_cell = fine_node.cell
                if region_cell.content.isFuel:
                    self.region_type_rel[n_id]["fuel"] = r_id
                    self.region_type_rel_switched[n_id][r_id] = "fuel"
                else:
                    self.region_type_rel[n_id]["other"] = r_id
                    self.region_type_rel_switched[n_id][r_id] = "other"
      
    def __get_equalities(self):
        self.equal_nodes = get_equal_nodes(self.__coarse_nodes, self.__fine_nodes)
        for bin_ in self.equal_nodes:
            head = bin_[0]
            for node_id in bin_:
                self.equal_nodes_rel[node_id] = head
        
        for n_id, n_eq_id in self.equal_nodes_rel.items():
            for reg in self.coarse_region_rel[n_id]:
                type_reg = self.region_type_rel_switched[n_id][reg]
                reg_eq = self.region_type_rel[n_eq_id][type_reg]
                self.equivalence_region_rel[reg] = reg_eq

        for n_id, n_eq_id in self.equal_nodes_rel.items():
            node_ = self.__coarse_nodes[n_id]
            node_eq = self.__coarse_nodes[n_eq_id]
            surface_rel = get_surface_equality(node_, node_eq)
            self.equivalence_surface_rel.update(surface_rel)




