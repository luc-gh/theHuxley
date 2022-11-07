lista = []
diasMeta = 0
soma = 0.0
for i in range(0,7,1):
  x = float(input())
  soma += x
  lista.append(x)
  if x >= lista[i-1] + 0.5:
    diasMeta += 1
print('R$ %.2f'%soma)
print(diasMeta)