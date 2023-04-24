class MontecarloParams:


    def __init__(self, histories, active, unactive, seed=None):
        self.__histories = histories
        self.__active_cycles = active
        self.__unactive_cycles = unactive
        self.__seed = seed
        self.serpent_syntax = f"set pop {histories} {active} {unactive}\n"
        if seed:
            self.serpent_syntax += f"set seed {self.__seed}\n"
        
    @property
    def histories(self):
        return self.__histories
    
    @property
    def active_cycles(self):
        return self.__active_cycles
    
    @property
    def unactive_cycles(self):
        return self.__unactive_cycles
    
    @histories.setter
    def histories(self, value):
        self.__histories = value
    
    @active_cycles.setter
    def active_cycles(self, value):
        self.__active_cycles = value
    
    @unactive_cycles.setter
    def unactive_cycles(self, value):
        self.__unactive_cycles = value
    

class BoundaryConditions:

    def __init__(self):
        pass