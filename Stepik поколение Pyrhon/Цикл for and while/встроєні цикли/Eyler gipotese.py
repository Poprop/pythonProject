# for n in range(1,14):
#     for k in range(1, 13):
#         for m in range(1, 12):
#             if 28*n+30*k+31*m==365:
#                 print(f"n={n},k={k},m={m} ")

# for b in range (1,11):
#     for k in range(1,21):
#         for m_k in range(1,201):
#             if 10*b+5*k+0.5*m_k==100 and b+k+m_k==100:
#                 print(f"b={b} , k={k}, m_k={m_k}")

for a in range(1,151):
    for b in range(1,151):
        for c in range(1,151):
            for d in range(1,151):
                 sum = a**5+b**5+c**5+d**5
                 e=int(sum**(1/5))
                 if sum==e**5:
                     print(a,b,c,d,e)
                     print(a+b+c+d+e)
                     break



