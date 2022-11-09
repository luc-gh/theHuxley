x = dataMaior = dataMenor= None
dados = []
maior = soma = 0
menor = 100
while x != '*':
  x = input()
  if x != '*': dados.append(x)
for v in range(len(dados)): 
  dados[v] = dados[v].replace(",",".")
  dados[v] = dados[v].split()
  if float(dados[v][1]) > maior: 
    maior = float(dados[v][1])
    dataMaior = dados[v][0]
  if float(dados[v][1]) < menor: 
    menor = float(dados[v][1])
    dataMenor = dados[v][0]
  soma += float(dados[v][1])
media = soma/len(dados)
print(f'Menor: {menor:,.2f} ({dataMenor[-2::1]}-{dataMenor[0:4:1]})\nMaior: {maior:,.2f} ({dataMaior[-2::1]}-{dataMaior[0:4:1]})\nMedia: {media:,.2f}')