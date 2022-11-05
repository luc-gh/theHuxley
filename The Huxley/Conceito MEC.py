def cond(l:int,a:int):
  x = float(a/l)
  if x > 18:
    print('D')
  elif x >= 13 and x <= 18:
    print('C')
  elif x >= 9 and x <= 12:
    print('B')
  else:
    print('A')

liv = int(input())
alu = int(input())
cond(liv,alu)