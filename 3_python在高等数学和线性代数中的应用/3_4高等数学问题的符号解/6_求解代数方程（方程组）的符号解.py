from sympy import *
x, y=symbols('x y')
print(solve(x**3-1, x))
print(solve((x-2)**2*(x-1)**3, x))
print(roots((x-2)**2*(x-1)**3, x))

s = solve([x**2+y**2-1, x-y], [x, y])
print("方程组的解为", s)