def imp(m:float):
  if m < 110.0: print('Glicose Normal')
  elif m >= 200.0: print('Glicose Muito Alta')
  else: print('Glicose Alterada')

x = 1
l = []
while x != 0:
  e = float(input())
  if e != 0: l.append(e)
  else: x = 0

soma = 0.0
for i in l:
  soma += i 

imp(soma/(len(l)))