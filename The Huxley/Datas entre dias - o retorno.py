x = int(input())
l = (input().split())
for i,c in enumerate(l): l[i] = int(l[i])
o = l.copy()
l.sort()
quant = 0
y = 0
a = []
for i in zip(o, l):
  y += 1
  if i[0] == i[1]: 
    quant += 1
    a.append(f'{i[0]} {y}')
print(quant)
for i in a: print(i)