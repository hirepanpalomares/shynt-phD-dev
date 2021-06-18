import os

class SerpentLibraries:

    def __init__(self, acelib="", therm=""):
        self.__acelib = acelib
        self.__thermal_scattering_data = therm
    
    def getAcelib(self):
        return self.__acelib
    
    def getThermalScatteringData(self):
        return self.__thermal_scattering_data
    
