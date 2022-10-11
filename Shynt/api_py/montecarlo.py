class MontecarloParams:


    def __init__(self, histories, active, unactive, seed=None):
        self.__histories = histories
        self.__active_cycles = active
        self.__unactive_cycles = unactive
        self.__seed = seed
        self.serpent_syntax = f"set pop {histories} {active} {unactive}\n"
        if seed:
            self.serpent_syntax += f"set seed {self.__seed}\n"
        

    def setHistories(self, value):
        self.__histories = value
    
    def setActiveCycles(self, value):
        self.__active_cycles = value
    
    def setUnactiveCycles(self, value):
        self.__unactive_cycles = value
    
    def getHistories(self):
        return self.__histories
    
    def getActiveCycles(self):
        return self.__active_cycles
    
    def getUnactiveCycles(self):
        return self.__unactive_cycles
    

class BoundaryConditions:

    def __init__(self):
        pass