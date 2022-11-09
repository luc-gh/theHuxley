def cond(lista):
  cond = None
  a = lista.copy()
  b = lista.copy()
  a.sort()
  b.sort(reverse=True)
  if lista == a: print('C')
  elif lista == b: print('D')
  else: print('N')

l = input().split()
for i in range(len(l)): l[i] = int(l[i])
cond(l)