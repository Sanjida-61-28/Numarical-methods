# False Position Method (Regula Falsi)
def f(x):
# Example function: change this as needed
    return x**3 - 4*x - 9
def false_position(a, b, tol=1e-6, max_iter=15):
    if f(a) * f(b) >= 0:
        print("Invalid initial guesses. f(a) and f(b) must have opposite signs.")

        return None
    print("Iter\t a\t\t b\t\t c\t\t f(c)")
    for i in range(max_iter):
# Compute the point using Regula Falsi formula
        c = b - (f(b) * (a - b)) / (f(a) - f(b))
        print(f"{i+1}\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f(c):.6f}")
# Check if result is close enough to zero
    if abs(f(c)) < tol:
        print("\nRoot found at x =", round(c, 6))
        return c
# Update interval
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

    print("\nDid not converge within the given iterations.")
    return None

# Example usage
false_position(a=2, b=3)
