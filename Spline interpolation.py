import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

def cubic_spline(x, y, x_new):
    n = len(x)
    a = y.copy()
    
    h = np.diff(x)
    

    A = np.zeros((n, n))
    b = np.zeros(n)
    

    for i in range(1, n - 1):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]
        b[i] = 3 * ((a[i + 1] - a[i]) / h[i] - (a[i] - a[i - 1]) / h[i - 1])
    
    
    A[0, 0] = 1
    A[n - 1, n - 1] = 1
    
    
    c = np.linalg.solve(A, b)
    
    
    b = np.zeros(n - 1)
    d = np.zeros(n - 1)
    
    for i in range(n - 1):
        b[i] = (a[i + 1] - a[i]) / h[i] - h[i] * (2 * c[i] + c[i + 1]) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])
    

    y_new = np.zeros_like(x_new)
    
    for j, x_val in enumerate(x_new):
        
        for i in range(n - 1):
            if x[i] <= x_val <= x[i + 1]:
                dx = x_val - x[i]
                y_new[j] = a[i] + b[i] * dx + c[i] * dx**2 + d[i] * dx**3
                break
                
    return y_new

x_new = np.linspace(1, 5, 100)
y_new = cubic_spline(x, y, x_new)


plt.figure(figsize=(10, 5))
plt.scatter(x, y, color='blue', label='Original Data')
plt.plot(x_new, y_new, color='red', label='Cubic Spline Interpolation')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cubic Spline Interpolation Example')
plt.legend()
plt.show()

