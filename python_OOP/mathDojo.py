class Mathdojo:
    def __init__(self):
        self.value = 0
    def add(self,*args):
        for val in args:
            self.value = self.value + val
        return self
    def subtract(self,*args):
        for val in args:
            self.value = self.value - val
        return self
    def result(self):
        return self.value
md = Mathdojo()
x = md.add(2).add(2,5,1).subtract(3,2).result()
print(x)
