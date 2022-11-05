def result(a:bool, p:int):
  if a == True:
    print('Pode viajar.')
    print(f'R$: {p}')
  else:
    print('Nao pode viajar.')

lista = input().split(' ')
d, r, l, p, g = int(lista[0]), int(lista[1]), int(lista[2]), int(lista[3]), int(lista[4])  
capacidadeCarro = l*10
distPostos = d/(p+1)  
distRestante = d - capacidadeCarro
postosUltrapassados = capacidadeCarro // distPostos  
gastoAbastecimento = (distRestante/10)*g 
if capacidadeCarro >= d: 
  result(True, r)
else:
  if gastoAbastecimento > r or distPostos > capacidadeCarro:  
    result(False, 0)
  else:
    result(True, int(r - gastoAbastecimento)) 