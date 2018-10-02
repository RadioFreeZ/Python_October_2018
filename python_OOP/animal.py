class Animal:
    def __init__(self,name):
        self.health = 100
        self.name = name
    def walk(self):
        if self.health > 0:
            self.health-=1
        return self
    def run(self):
        if self.health > 0:
            self.health-=5
        return self
    def display_health(self):
        if self.health <= 0:
            print("He's dead jim...")
        else:
            print(f"{self.name}'s Health Is: {self.health}")
        return self
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
        self.health = 150
    def pet(self):
        if self.health > 0:
            self.health+=5
        else:
            print("Don't touch it, it's dead!")
        return self
class Dragon(Animal):
    def __init__(self,name):
        super().__init__(name)
        self.health = 170
    def fly(self):
        if self.health > 0:
            self.health -= 10
        return self
    def display_health(self):
        super().display_health()
        print("I am a Dragon")
dog = Dog("Fido")
dog.walk().walk().walk().run().run().pet().display_health()
dragon = Dragon("Smaug")
dragon.fly().fly().fly().display_health()
hamster = Animal("Bilbo")
hamster.display_health().walk()
