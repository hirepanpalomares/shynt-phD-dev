class Detector():

    """
        Class for a single detector

        Parameters:
        -------------------------------------------------------------------
        - name  :   Name for the detector in serpent card
        - type  :   Type of detector regarding the probability that 
                    we  want to calculate.
        -------------------------------------------------------------------
    """
    def __init__(self, name, type_):
        self.name = name
        self.type = type_
        self.surface = None
        self.energy_bins = None
        self.response = None
        self.flag = None
        self.cell = None


    @property
    def surface_det(self):
        pass
    
    @property
    def energy_bins(self):
        pass

    @property
    def response(self):
        pass

    @property
    def flag(self):
        pass
    
    @property
    def cell(self):
        pass

    @property.setter
    def surface_det(self):
        pass
    
    @property.setter
    def energy_bins(self):
        pass

    @property.setter
    def response(self):
        pass

    @property.setter
    def flag(self):
        pass
    
    @property.setter
    def cell(self):
        pass


class DetectorTotalRate():

    def __init__(self) -> None:
        pass

class DetectorTotalRate():

    def __init__(self) -> None:
        pass

class DetectorTotalRate():

    def __init__(self) -> None:
        pass

class DetectorTotalRate():

    def __init__(self) -> None:
        pass