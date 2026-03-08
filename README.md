# Oblig 2 – DAFE1000

Navn: Eyad Amer Alawak  
Student e-post: eyibr1083@oslomet.no



## Analytisk løsning

Vi ser på funksjonen

f(x) = e^(-x/4) * arctan(x)

For å finne toppunktet deriverer vi funksjonen ved bruk av produktregelen.

f'(x) = e^(-x/4) * (1/(x^2 + 1) - 1/4 * arctan(x))

Toppunktet finnes ved å sette den deriverte lik null.

Dette gir ligningen

arctan(x) - 4/(x^2 + 1) = 0


## Numerisk løsning i Python

For å løse ligningen numerisk bruker vi Python og bibliotekene numpy og scipy.


```python
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

print(x_topp, y_topp)

x = np.linspace(-5,10,500)
y = f(x)

plt.plot(x,y)
plt.scatter(x_topp,y_topp,color='red')
plt.show()
```

## Resultat

Ved numerisk løsning får vi

x ≈ 1.4782

f(x) ≈ 0.7166

Dermed er toppunktet omtrent

(1.4782 , 0.7166)
