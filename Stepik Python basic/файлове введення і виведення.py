inf = open(r"C:\Users\ILLIA\PycharmProjects\pythonProject\Stepik Python basic\Функції\dataset_3363_3.txt")
s = inf.read().replace('\n', ' ').lower().split()
p=[]
for i in set(s):
    p = []
    p.uppend(i , scount(i)