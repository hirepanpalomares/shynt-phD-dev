
from Shynt.api_py.Geometry.regions import SurfaceSide


class SerpentSurfaces:
    
    def __init__(self) -> None:
        pass


class SerpentUniverses:

    def __init__(self) -> None:
        pass


class SerpentCells:

    def __init__(self) -> None:
        pass


class SerpentMaterials:

    def __init__(self) -> None:
        pass


class SerpentIsotopes:

    def __init__(self) -> None:
        pass


class SerpentXsLibraries:

    def __init__(self) -> None:
        pass


class SerpentGroupConstantGeneration:

    def __init__(self) -> None:
        pass


class SerpentDetectors:

    def __init__(self) -> None:
        pass



def print_cell(cell):
    print_statement = f"cell {cell.name} "
    if cell.filled_by_universe:
        #cell was filled with universe 
        # RECURSIVE CALL   
        if cell.universe:
            print_statement += f"{cell.universe} "
        universe = cell.filled_by_universe
        print_statement += f"fill {universe.name} "
        region = cell.region
        if isinstance(region, SurfaceSide):
            print_statement += f"{region.side}{region.surface.name}\n"
        
    else:
        #cell was filled with material
        # print directly Serpent cell definition
        if cell.universe:
            print_statement += f"{cell.universe} "
        material = cell.material
        print_statement += f"fill {material.name} "
        region = cell.region
        if isinstance(region, SurfaceSide):
            print_statement += f"{region.side}{region.surface.name}\n"
        
    return print_statement