n = int(input())
reg = []
for i in range(2*n):
  s = input().split()
  for i in range(len(s)): s[i] = int(s[i])
  reg.append(s)
l1 = [] 
l2 = []
met = int(len(reg)/2)
for i,c in enumerate(reg[0:met:1]): l1.append(c)
for i,c in enumerate(reg[met:len(reg):1]): l2.append(c)
for i in range(n):
  ch = ''
  for j in range(n):
    ch += f'{l1[i][j] + l2[i][j]} '
  if i == n-1: ch = ch[:-1]
  print(ch)