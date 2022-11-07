tv = 0.0
l = ''
lista = 0
while l != 'FIM':
  l = input()
  if l != 'FIM': lista += len(list(l.split()))
  for c in l:
    if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U') and l != 'FIM': tv += 1
if lista == 0: print('texto vazio')
else: print('%.2f'%(tv/lista))