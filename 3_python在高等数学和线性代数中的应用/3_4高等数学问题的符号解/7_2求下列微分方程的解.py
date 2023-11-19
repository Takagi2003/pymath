from sympy import *
x = symbols('x ')
y = symbols('y', cls=Function)
eq1 = diff(y(x), x, 2)-5*diff(y(x), x)+6*y(x)
eq2 = diff(y(x), x, 2)-5*diff(y(x), x)+6*y(x)-x*exp(2*x)
y1 = dsolve(eq1, y(x), ics={y(0): 1, diff(y(x), x).subs(x, 0): 0})
y2 = dsolve(eq2, y(x), ics={y(0): 1, y(2): 0})
print(f"初值问题的解为:{y1}")
print(f"边值问题的解为：{y2}")