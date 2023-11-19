from sympy.abc import x, y
from sympy import plot_implicit as pt, Eq

pt(Eq((x-1)**2+(y-2)**3, 4), (x, -6, 6), (y, -2, 4))