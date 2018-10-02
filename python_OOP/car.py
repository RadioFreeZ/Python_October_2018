class Car:
    def __init__ (self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def display_all(self):
        print("Price:",self.price)
        print(f"Speed: {self.speed}mph")
        print("Fuel:",self.fuel)
        print(f"Mileage: {self.mileage}mpg")
        print("Tax:",self.tax,"\n")
        return self
Toyota = Car(5000,50,"Full",15)
GMC = Car(2000,10,"Empty",1)
Jeep = Car(7000,70,"Half-Full",30)
Ford = Car(10,"Really Slow","Always-Empty","Nope")
Chevrolet = Car(5000,50,"Full",50)
Tesla = Car(999999,"Really Fast","Always-Full","Yes")

Toyota.display_all()
GMC.display_all()
Jeep.display_all()
Ford.display_all()
Chevrolet.display_all()

Tesla.display_all()
