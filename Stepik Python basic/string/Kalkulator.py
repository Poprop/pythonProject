x = float(input())
y = float(input())
operation = input()

if "+" in operation:
    print(x + y)
elif "-" in operation:
    print(x - y)
elif "/" in operation:
    if y == 0.0:
        print("Деление на 0!")
    if y != 0.0:
        print(x / y)

elif "*" in operation:
    print(x * y)
elif "mod" in operation:
    if y == 0.0:
        print("Деление на 0!")
    if y != 0.0:
        print(x%y)
elif "pow" in operation:
    print(x ** y)
elif "div" in operation:
    if y == 0.0:
        print("Деление на 0!")
    if y != 0.0:
        print(x // y)
# Через словари
#______________________________________

operations = {
      "+": lambda x, y: x + y,
      "-": lambda x, y: x - y,
      "/": lambda x, y: x / y,
      "*": lambda x, y: x * y,
      "mod": lambda x, y: x % y,
      "pow": lambda x, y: x ** y,
      "div": lambda x, y: x // y
}

x, y = float(input()), float(input())
operation = input()

if operation in ["mod", "div", "/"] and y == 0:
    print("Деление на 0!")
else:
    print(operations[operation](x, y))
#Через еlif но изящно
#-------------------------------------------
a = float(input())
b = float(input())
act = input()

if (act=="/" or act=="mod" or act=="div") and b==0:
    c = "Деление на 0!"
elif act=="+":    c = a + b
elif act=="-":    c = a - b
elif act=="/":    c = a / b
elif act=="*":    c = a * b
elif act=="mod":  c = a % b
elif act=="pow":  c = a ** b
elif act=="div":  c = a // b

print (c)

#Через функцию
#------------------------------------------
def calculate(a, b, P):
    if P == '+':
        return a + b
    if P == '-':
        return a - b
    if P == '/':
        return a / b
    if P == '*':
        return a * b
    if P == 'mod':
        return a % b
    if P == 'pow':
        return a ** b
    if P == 'div':
        return a // b


x = float(input())
y = float(input())
operation = input()
if y == 0 and (operation == '/' or operation == 'div' or operation == 'mod'):
    print('Деление на 0!')
else:
    print(calculate(x, y, operation))