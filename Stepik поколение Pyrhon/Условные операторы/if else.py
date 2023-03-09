# x,y=input(),input()
# print("Пароль принят" if x==y else '«Пароль не принят')
#
#
#
# x=list(map(int,input()))
# sum_14=(x[0]+x[3])
# sum_23=(x[1]-x[2])
# if sum_23==sum_14:
#     print("ДА")
# else:
#     print("НЕТ")
# x,y,b= int(input()),int(input()),int(input())
# print("YES" if y-x==b-y  else "NO")
#
# a,b,c,d=int(input()),int(input()),int(input()),int(input())
# print(min(a,b,c,d))

# x=int(input())
# if x<=13:
#     print("детство")
# if 14<=x<=24:
#     print("молодость")
# if 25<=x<=59:
#     print("зрелость")
# if x>=60:
#     print("старость")
# x,y,d=int(input()),int(input()),int(input())
# list=[]
# if x>0 :
#     list.append(x)
# if y>0:
#     list.append(y)
# if d>0:
#     list.append(d)
# print(sum(list))

# a = int(input())
# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5
# p = (a + b) * (a + b)
# print(p)

# x=int(input())
# print("YES" if 1000<=x<=9999 and x%7==0 or x%17==0 else "NO")
# a,b,c=int(input()),int(input()),int(input())
# print("YES" if c<a+b and a<c+b and b<a+c else "NO")

x=int(input())
print("YES" if (x%4==0 and (not x%100==0)) or x%400==0 else "NO")