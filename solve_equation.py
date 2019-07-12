"""
 解下列二元一次方程
  2x-y=3
  3x+y=7
"""
# 导入模块
from sympy import *

# 将变量符号化
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

# 解一元一次方程
expr1 = x*2-4
r1 = solve(expr1, x)
r1_eq = solve(Eq(x*2, 4), x)
print("r1:", r1)
print("r1_eq:", r1_eq)

# 解二元一次方程
expr2 = [2*x-y-3, 3*x+y-7]
r2 = solve(expr2, [x, y])
print("r1:", r2)

# 解三元一次方程
f1 = x+y+z-2
f2 = 2*x-y+z+1
f3 = x+2*y+2*z-3
r3 = solve([f1, f2, f3], [x, y, z])
print("r3:", r3)


"""
    x+y+z-2=0
    2x-y+z+1=0
    x+2y+2z-3=0
"""
from sympy import *


x, y, z = symbols("x y z")

# 默认等式为0的形式
print("======默认等式为0的形式 =======")
eq = [x+y+z-2, 2*x-y+z+1, x+2*y+2*z-3]
result = linsolve(eq, [x, y, z])
print(result)
print(latex(result))

# 矩阵形式
print("======矩阵形式 =======")
eq = Matrix(([1, 1, 1, 2], [2, -1, 1, -1], [1, 2, 2, 3]))
result = linsolve(eq, [x, y, z])
print(result)
print(latex(result))

# 增广矩阵形式
print("======增广矩阵形式 =======")
A = Matrix([[1, 1, 1], [2, -1, 1], [1, 2, 2]])
b = Matrix([[2], [-1], [3]])
system = A, b
result = linsolve(system, x, y, z)
print(result)
print(latex(result))

"""
    x**2+y**2-2=0
    x**3+y**3=0
"""

import sympy as sy
x, y = sy.symbols("x y")

eq = [x**2+y**3-2, x**3+y**3]
result = sy.nonlinsolve(eq, [x, y])
print(result)
print(sy.latex(result))


# 初始化
x = symbols('x')
f = symbols('f', cls=Function)

# 表达式
expr1 = Eq(f(x).diff(x, x) - 2*f(x).diff(x) + f(x), sin(x))

# 求解微分方程
r1 = dsolve(expr1, f(x))

print(r1)
print("原式：", latex(expr1))
print("求解后：", latex(r1))

