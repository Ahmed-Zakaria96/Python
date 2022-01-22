class Car:

    def __init__(self, name, fuelRate, velocity=0):
        self.name = name
        self._fuelRate = fuelRate
        self._velocity = velocity

    # use gas
    @property
    def fuelRate(self):
        return self._fuelRate

    @fuelRate.setter
    def fuelRate(self, d):
        if self.fuelRate - d <= 100 and self.fuelRate -d >=0:
            self._fuelRate -= d
        else:
            print("Fuel rate must be between 0 and 100.")

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, v):
        if 0 <= v <= 200:
            self._velocity = v
            return True
        else:
            print("Velocity must be between 0 and 200.")
            return False

    # add gas
    def reFuel(self, f):
        if self.fuelRate + f <= 100 and self.fuelRate + f >=0:
            self._fuelRate += f
            print(f"Successfully refueled, Current fuel rate is {self.fuelRate}")
            return True
        else:
            print("Fuel rate must be between 0 and 100.")
            return False

    def run(self, dtw, d, v):
        self.velocity = v
        reqFuel = self.calcReqFuel(d)
        if self.fuelRate - reqFuel >= 0:
            if dtw - d > 0:
                self.fuelRate -= reqFuel
                dtw -= d
                print("car is running")
                self.stop(dtw)
                return dtw
            else:
                ddFuel = self.calcReqFuel(dtw)
                print(f"Arrived work after {dtw} KM.")
                self.fuelRate -= ddFuel
                dtw = 0
                self.stop(dtw)
                return dtw
        else:
            driveDistance = self.calcDistance()
            dtw -= driveDistance
            print(f"Car Stopped after {driveDistance} KM.")
            self.stop(dtw)
            self.fuelRate = 0
            return dtw

    def stop(self, dtw):
        print("Stopped the car")
        print(f"distance to work = {dtw}")
        self.velocity = 0

    def calcReqFuel(self, d):
        reqFuel = (self.fuelRate * .1) * (d//10) + d % 10
        # currFuel = self.fuelRate
        # c = 0
        # dd = d // 10
        # while c < dd:
        #     reqFuel += currFuel * .1
        #     currFuel = currFuel - reqFuel
        #     d = d - 10
        #     c = c + 1
        # remDFuel = ((d % 10) * .1) /10 * currFuel
        # reqFuel += remDFuel
        return reqFuel

    def calcDistance(self):
        currFuel = self.fuelRate
        distance = 0
        if currFuel % 10 == 0:
            distance = currFuel / 10 * 10
        else:
            rem = currFuel % 10
            currFuel = currFuel - rem
            distance = currFuel / 10 * 10 + rem
        return distance

    def prepareCarData(self):
        data = {
            "Type": self.name,
            "Fuel Rate": self.fuelRate,
        }
        return data
