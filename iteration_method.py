import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.cos(x) - x
def g(x):
    return np.cos(x) # x = cos(x)
# interval [a, b] where f(a) * f(b) < 0
def find_interval(f, start=-10, end=10, step=0.1):
    x = start
    while x < end:
        if f(x) * f(x + step) < 0:
            return x, x + step
        x += step
    return None, None

def fixed_point_iteration(g, x0, tol=1e-6, max_iter=100):
    print("\n� Fixed Point Iteration:")
    for i in range(max_iter):
        x1 = g(x0)
        print(f"Iteration {i+1:>2}: x = {x1:.10f}")
        if abs(x1 - x0) < tol:
            print(f"\n� Converged to root: {x1:.10f} after {i+1} iterations.")

            return x1
        x0 = x1
    print("� Did not converge.")
    return None

def plot_function(f, a, b, root=None):
    x_vals = np.linspace(a - 1, b + 1, 400)
    y_vals = f(x_vals)
    plt.figure(figsize=(8, 4))
    plt.plot(x_vals, y_vals, label="f(x) = cos(x) - x", color='blue')
    plt.axhline(0, color='black', linestyle='--')

    plt.axvline(a, color='red', linestyle='--', label=f"a = {a:.2f}")
    plt.axvline(b, color='green', linestyle='--', label=f"b = {b:.2f}")
    if root:
        plt.plot(root, f(root), 'ro', label=f"Root ≈ {root:.6f}")
    plt.grid(True)
    plt.legend()
    plt.title("Graph of f(x) and Interval with Root")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()

a, b = find_interval(f, start=0, end=2)
if a is not None:
    print(f"\n� Root likely in interval: [{a:.4f}, {b:.4f}]")
    plot_function(f, a, b)
    x0 = (a + b) / 2
    root = fixed_point_iteration(g, x0)
if root:
    plot_function(f, a, b, root=root)

else:
    print(" No root found in the given range.")