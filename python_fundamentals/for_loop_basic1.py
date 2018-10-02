for i in range(0,151):
    print(i)

for i in range(5,1000001,5):
    print (i)

for i in range(1,101):
    if i % 10 == 0:
        print("Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

sum = 0
for i in range(1,500000,2):
    sum = i + sum
print(sum)

for i in range (2018,0,-4):
    print(i)

def flex(lowNum,highNum,mult):
    for i in range(lowNum,highNum+1):
        if i % mult == 0:
            print(i)
flex(2,9,3)
