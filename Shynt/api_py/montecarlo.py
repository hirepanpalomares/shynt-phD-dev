class MontecarloParams:

    def __init__(self, histories, active, unactive):
        self.__histories = histories
        self.__active_cycles = active
        self.__unactive_cycles = unactive
    
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
    