def newton_backward_interpolation(x, y, value):
    n = len(x)
    diff_table = [[0 for _ in range(n)] for _ in range(n)]

    # Initialize first column with y values
    for i in range(n):
        diff_table[i][0] = y[i]

    # Construct backward difference table
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            diff_table[i][j] = diff_table[i][j - 1] - diff_table[i - 1][j - 1]

    # Print the backward difference table
    print("\n========== NEWTON BACKWARD INTERPOLATION ==========\n")
    print(f"{'x':>8} | " + " | ".join([f"∇^{i}y".center(12) for i in range(n)]))
    print("-" * (12 * n + 10))

    for i in range(n):
        row = [f"{x[i]:>8.2f}"]
        for j in range(i + 1):
            row.append(f"{diff_table[i][j]:>12.6f}")
        print(" | ".join(row))

    # Apply Newton backward formula
    h = x[1] - x[0]
    p = (value - x[-1]) / h
    result = y[-1]
    fact = 1

    for i in range(1, n):
        fact *= i
        term = diff_table[n - 1][i]
        for j in range(i):
            term *= (p + j)
        result += term / fact

    print("\n--------------------------------------------")
    print(f"Interpolated value at x = {value} is {result:.6f}")
    print("--------------------------------------------\n")
    return result


# Example usage
x = [45, 50, 55, 60]
y = [0.7071, 0.7660, 0.8192, 0.8660]
newton_backward_interpolation(x, y, 58)
