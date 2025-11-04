def f(x):
    return x**3 - x - 2       
def f_prime(x):
    return 3*x**2 - 1       
def newton_raphson(x0, tol=1e-6, max_iter=20):
    print("Newton-Raphson Method Iterations:")
    print(f"{'Iter':>4} | {'x':>10} | {'f(x)':>12}")
    for i in range(1, max_iter + 1):
        fx = f(x0)
        fpx = f_prime(x0)
        if fpx == 0:
            print("Derivative is zero. Stopping iteration.")
            return None
        x1 = x0 - fx / fpx
        print(f"{i:4d} | {x1:10.6f} | {fx:12.6f}")

        if abs(x1 - x0) < tol:
            print(f"\nRoot found: {x1:.6f} (after {i} iterations)")
            return x1
        x0 = x1
    print("\nDid not converge within maximum iterations.")
    return None
initial_guess = 1.5
root = newton_raphson(initial_guess)
if root is not None:
    print(f"\nApproximate Root = {root:.6f}")
