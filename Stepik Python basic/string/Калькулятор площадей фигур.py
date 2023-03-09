# print("Введите фигуру")
# figura = input()
# if 'треугольник' in figura:
#     a = int(input())
#     b = int(input())
#     c = int(input())
#
#     p = (a + b + c) / 2
#     S = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
#     print(S)
# if "прямоугольник" in figura:
#     a = int(input())
#     b = int(input())
#     S = a * b
#     print(S)
# if 'круг' in figura:
#     Pi = 3.14
#     r = int(input())
#     S = Pi * r ** 2
#     print(S)

#________________________Словари
# figura = {'треугольник': [3, lambda a, b, c: ((a+b+c)/2*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c))**0.5],
#           'прямоугольник': [2, lambda a, b: a*b],
#           'круг': [1, lambda r: 3.14*r**2]}
# f = input()
# print(figura[f][1](*(float(input()) for _ in range(figura[f][0]))))

# ---------------------------------------------------------------------
# s = {1: lambda r: 3.14  * r**2, 2: lambda a, b: a * b, 3: lambda a, b, c: ((a+b+c)/2*(b+c-a)/2*(a+c-b)/2*(a+b-c)/2)**0.5}
# f = {'круг': 1, 'прямоугольник': 2, 'треугольник': 3}
# args = [float(input()) for _ in range(f[input()])]
# print(s[len(args)](*args))