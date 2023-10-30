from math import factorial

class Formulas():
    def __init__(self, Y: int, arrivalRate: float, serviceRate: float, state = 0):
        self.Y = Y
        self.arrivalRate = arrivalRate # lambda
        self.serviceRate = serviceRate # mu
        self.state = state # state
        
        # backups for simulation
        self.backupArrivalRate = arrivalRate # backup lambda
        self.backupServiceRate = serviceRate # backup mu
        
    # GETTERS
    
    def getY(self):
        return self.Y
    
    def getArrivalRate(self):
        return self.arrivalRate
    
    def getServiceRate(self):
        return self.serviceRate
    
    def getState(self):
        return self.state
    
    # SETTERS
    
    def setY(self, Y: int):
        self.Y = Y
    
    def setArrivalRate(self, arrivalRate: float):
        self.arrivalRate = arrivalRate
    
    def setServiceRate(self, serviceRate: float):
        self.serviceRate = serviceRate
    
    def setState(self, state: int):
        self.state = state
        
    # UTILS
    
    def resetValues(self):
        self.arrivalRate = self.backupArrivalRate
        self.serviceRate = self.backupServiceRate
        
    # self
    
    # returns A
    def getTrafficIntensity(self):
        return self.arrivalRate / self.serviceRate
    
    # returns LambdaK (0 if state > Y)
    def getArrivalRateAtState(self, state: int):
        if state <= self.Y:
            return self.arrivalRate
        
        return 0
    
    # returns MuK
    def getServiceRateAtState(self, state: int):
        return state * self.serviceRate
    
    # returns Pk (0 if state > Y)
    def getProbabilityAtState(self, state: int):
        if state <= self.Y:
            return (self.getProbabilityAtStateZero()
                    * pow(self.getTrafficIntensity(), state)
                    / factorial(state))
            
        return 0
    
    # returns P0
    def getProbabilityAtStateZero(self):
        sum = 0
        for i in range(0, self.Y + 1):
            sum += pow(self.getTrafficIntensity(), i) / factorial(i)
            
        return pow(sum, -1)
    
    # returns PY (P{block})
    def getProbabilityAtStateY(self):
        return self.getProbabilityAtState(self.Y)
        
    # returns Lq
    def getQueueLength():
        return 0
    
    # returns Wq
    def getQueueWait():
        return 0
    
    # returns Ls
    def getServerLength(self):
        return self.getTrafficIntensity() * (1 - self.getProbabilityAtStateY())
    
    # returns Ws
    def getServerWait(self):
        return 1 / self.serviceRate
