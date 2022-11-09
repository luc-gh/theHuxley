def verificar(x):
  valor = 0
  for i,c in enumerate(str(x)[::-1]):  # enumera a string reversa
    if c == '1':
      valor += 2**int(i)
  quant = 0
  for i in range(valor):
    if not i == 0 and not (i & (i - 1)) and not (i & 0xAAAAAAAA): quant += 1  # verifica se ? pot?ncia de 4
  if quant != 0 and x[0] != '0': print(quant)
  else: print("Numero Invalido")

verificar(input())