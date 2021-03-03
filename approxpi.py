from numpy import random
import numpy as np
import matplotlib.pyplot as plt


N = int(input("Enter how many darts you want to throw (the more, the more precise): ")) # thrown darts

circle_x = []
circle_y = []

square_x = []
square_y = []

i = 1
while i <= N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= 1:
        circle_x.append(x)
        circle_y.append(y)
    else:
        square_x.append(x)
        square_y.append(y)
    i+=1

pi = 4 * len(circle_x)/float(N)

print(f"Pi is approximately: {pi}")
print(f"Pi actually is: {np.pi}")

plt.plot(circle_x, circle_y, 'b.')
plt.plot(square_x, square_y, 'g.')
plt.grid()   
plt.show()
