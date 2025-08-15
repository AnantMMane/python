import math

def sin(x):
    if 2 * x == pi:
        return 0.999999
    else:
        return None

pi = 3.14

print(sin(pi/2)) 
print(math.sin(math.pi/2))

for n in dir(math):
    print(n, end='\t')