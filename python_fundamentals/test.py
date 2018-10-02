print("*"*80)
def beCheerful(name='', repeat=98):
	print(f"good morning {name}\n"*repeat)
beCheerful(name="john")

import random
def randInt(max=100, min=0):
    return int(random.random() * (max-min) + min)
print(randInt(max=200, min = 100))
