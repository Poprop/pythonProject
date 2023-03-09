# x=int(input())
# text="Even" if x%2==0 else "Odd"
# print(text)
#---------------------------------------------------------------
# x,y=int(input()) , int(input())
# minimum=x if x<y else y
# print(minimum,end=" ")
# maximum=x if x>y else y
# print(maximum,end=" ")
# або ---------------------------------------------------------------------------------------------
# print(minimum := n if (n := int(input())) < (m := int(input())) else m, maximum := n if m < n else m)


# x=input()
# sentence="Вопросительное" if (x[-1]=="?") else "Обычное"
# print(sentence)
# або--------------------------
# print(('Обычное', 'Вопросительное')[input()[-1] == '?'])

# -----------------------------------------------------
# n=input()
# y=input()
# experiment=("Отталкиваются") if n==y else ("Притягиваются")
# print(experiment)

print(("Притягиваются","Отталкиваются")[input()==input()])