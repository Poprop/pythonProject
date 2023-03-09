
try:
    x = 5/2
    x=int(input())

except ZeroDivisionError :
    print("Деление на ноль!")
except ValueError:
    print("Вы ввели не то")
else:
    print("else")
finally:
    print("Finaly")