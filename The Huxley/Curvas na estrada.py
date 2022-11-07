v = esquerda = direita = incorretas = 0
while v == 0:
  ent = input()
  if ent == '*':
    v = 1
  else:
    if ent.lower() == 'd' or ent.lower() == 'dir' or ent.lower() == 'direita':
      direita += 1
    elif ent.lower() == 'esquerda' or ent.lower() == 'esq' or ent.lower() == 'e':
      esquerda += 1
    else:
      incorretas += 1

print('Esquerda: %i'%esquerda)
print('Direita: %i'%direita)
print('Incorretas: %i'%incorretas)