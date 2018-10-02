class Product:
    def __init__ (self,price,name,weight,brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def tax(self,rate):
        return self.price + self.price * rate
    def return_item(self,reason):
        if reason == "defective":
            self.price = 0
            self.status = "defective"
        if reason == "like new":
            self.status = "for sale"
        if reason == "opened":
            self.price = self.price * .8
            self.status = "used"
        return self
    def displayInfo(self):
        print(f"Price: {self.price}\nName: {self.name}\nWeight: {self.weight}\nBrand: {self.brand}\nStatus: {self.status}")
        return self
potato = Product(50,"potato",50,"potato")
potato.displayInfo()
print(potato.tax(.15))
potato.sell()
potato.displayInfo()
potato.return_item("opened")
potato.displayInfo()
