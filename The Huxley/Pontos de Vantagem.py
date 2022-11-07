n = int(input())
dunga = nando = 0
for c in str(n):
  if int(c) % 2 == 0: dunga += int(c)
  else: nando += int(c)

if nando > dunga:
  print('Vencedor: Nando')
  print('%d Pontos de Vantagem'%(nando-dunga))
elif dunga > nando:
  print('Vencedor: Dunga')
  print('%d Pontos de Vantagem'%(dunga-nando))
else: print('Empate')