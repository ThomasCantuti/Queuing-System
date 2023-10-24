# default k= 0

class Formulas():
    def __init__(self, Y: int, avgArrivalRate: float, avgServiceRate: float, k: int = 0):
        self.Y = Y
        self.avgArrivalRate = avgArrivalRate # lambda
        self.avgServiceRate = avgServiceRate # mu
        self.k = k
        
    # GETTERS & SETTERS
    
    def getY(self):
        return self.Y
    
    def getavgArrivalRate(self):
        return self.avgArrivalRate
    
    def getavgServiceRate(self):
        return self.avgServiceRate
    
    def setY(self, Y: int):
        self.Y = Y
    
    def setavgArrivalRate(self, avgArrivalRate: float):
        self.avgArrivalRate = avgArrivalRate
    
    def setavgServiceRate(self, avgServiceRate: float):
        self.avgServiceRate = avgServiceRate
        
    # FORMULAS
    
    # return the traffic intensity (A)
    def getTrafficIntensity(self):
        return self.avgArrivalRate / self.avgServiceRate
    