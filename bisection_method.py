def bisection (func,a,b,tol=1e-6,max_iter=100):
    """
    Bisection method with iteration
    """
    if func(a)*func(b)>=0:
        raise ValueError("f(a) and f(b) must have opposite signs.")
    print(f"{'iter' :<5}{'a':<12}{'b':<12}{'mid':<12}{'f(mid)':<12} ")
    print("-" * 55)
    for i in range (1,max_iter + 1):
        mid= (a+b)/2.0
        f_mid=func(mid)
        print(f"{i:<5}{a:<12.6f}{mid:<12.6f}{f_mid:<12.6f} ")
        if abs(f_mid)< tol or (b-a)/2 <tol:
            print("\n Converged! ")
            return mid
        if func(a)* f_mid<0:
            b=mid
        else:
            a=mid
    print("\n Reached maximumm iterations.")
    return (a+b)/2.0
if __name__ =="__main__":
    def f(x):
        return x**3-x-2
    root= bisection(f,a=1,b=2,tol=1e-6)
    print(f"\n Approximate root: {root:.6f}")