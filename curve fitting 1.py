import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
x_data = np.linspace(0, 10, 50)
y_data = 2 * x_data**2 + 3 * x_data + 1 + np.random.normal(0, 10, size=x_data.size)

coefficients = np.polyfit(x_data, y_data, 2)

polynomial = np.poly1d(coefficients)
x_fit = np.linspace(0, 10, 100)
y_fit = polynomial(x_fit)
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, label='Data', color='blue')
plt.plot(x_fit, y_fit, label='Fitted Curve', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Curve Fitting Example')
plt.legend()
plt.grid()
plt.show()
