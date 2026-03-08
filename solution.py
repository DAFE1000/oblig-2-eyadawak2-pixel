import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(x):
    return np.exp(-x/4) * np.arctan(x)

def g(x):
    return np.arctan(x) - 4/(x**2 + 1)

x0 = 1.5
x_topp = fsolve(g, x0)[0]
y_topp = f(x_topp)

print("Toppunkt x:", x_topp)
print("Toppunkt y:", y_topp)

x = np.linspace(-5,10,500)
y = f(x)

plt.plot(x,y)
plt.scatter(x_topp,y_topp,color='red')
plt.title("Function plot with maximum point")
plt.show()
