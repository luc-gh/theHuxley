dic = {}
l = input().split()
for i,c in enumerate(l):
  v = int(l[i])
  dic[i] = v
cont = 0
for valor in dic.values():
  if valor == dic[9]:
    cont += 1
print(f'O numero {dic[9]} apareceu {cont} vezes\n')