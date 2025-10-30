# Newton-Raphson Method Implementation
import math
def f(x):
    return x**3 - 5*x + 3  
def f_derivative(x):
    return 3*x**2 - 5
def newton_raphson(x0, tol=1e-6, max_iter=100):
    print("\n========== NEWTON-RAPHSON METHOD ==========\n")
    print(f"{'Iter':>5} | {'x':>10} | {'f(x)':>12} | {'f\'(x)':>12} | {'x_next':>12}")
    print("-" * 60)
    for i in range(1, max_iter + 1):
        fx = f(x0)
        fpx = f_derivative(x0)
        if fpx == 0:
            print("Derivative is zero. Stopping iteration.")
            return None
        x1 = x0 - fx / fpx
        print(f"{i:>5} | {x0:>10.6f} | {fx:>12.6f} | {fpx:>12.6f} | {x1:>12.6f}")
        if abs(x1 - x0) < tol:
            print("\n--------------------------------------------")
            print(f"Root found at x = {x1:.6f} after {i} iterations.")
            print("--------------------------------------------\n")
            return x1
        x0 = x1
    print("\nMethod did not converge within the maximum iterations.")
    return None
initial_guess = 1.0
root = newton_raphson(initial_guess)
