
import sympy

x, y = sympy.symbols('x y')

eq1 = sympy.Eq(x + y, 8)
eq2 = sympy.Eq(x - y, 6)

solution = sympy.solve((eq1, eq2), (x, y))
print(solution)