def criterios(lista: list):
  lista.sort()
  a, b, c = lista[0], lista[1], lista[2]
  pontos = 0
  if a+1 == b and b+1 == c:  
    pontos += a
  if a == b and a == c: 
    pontos += a
  if a == b and b < c:   
    pontos += (int(a/2)) 
  if b == c and a < b:  
    pontos += (int(b/2))   
  if a + b + c == 8:         
    pontos += 8              
  return pontos

p = input().split(" ")
w = input().split(" ")
paes = [int(valor) for valor in p]
willy = [int(valor) for valor in w]
pontPaes = criterios(paes)
pontWilly = criterios(willy)
if pontPaes > pontWilly:
  print(1)
elif pontPaes < pontWilly:
  print(2)
else:
  print(0)