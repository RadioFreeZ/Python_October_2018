class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print("Bike price is ",self.price,"\nBike speed is ",self.speed,"\nTotal miles is ",self.miles,"\n")
        return self
    def ride(self):
        self.miles = self.miles + 10
        print("Riding")
        return self
    def reverse(self):
        if self.miles > 0:
            self.miles = self.miles - 5
        print("Reversing")
        return self

Fuji = Bike(250,20)
Scott = Bike(500,30)
Gt = Bike (1000,50)
Fuji.displayInfo().ride().ride().ride().reverse().displayInfo()
Scott.displayInfo().ride().ride().reverse().reverse().displayInfo()
Gt.displayInfo().reverse().reverse().reverse().displayInfo()
