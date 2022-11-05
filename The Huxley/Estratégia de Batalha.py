l1 = input().split(" ") 
soldA, tanqA, aviA, lmA = int(l1[0]), int(l1[1]), int(l1[2]), int(l1[3])  
l2 = input().split(" ") 
soldI, tanqI, aviI, lmI = int(l2[0]), int(l2[1]), int(l2[2]), int(l2[3])  
l3 = input().split(" ")  
refSoldI, refTanqI, refAviI, refLmI = int(l3[0]), int(l3[1]), int(l3[2]), int(l3[3])  
sSI, sTI, sAI, sLMI = soldI + refSoldI, tanqI + refTanqI, aviI + refAviI, lmI + refLmI  
lista1 = [soldA, tanqA, aviA, lmA]  
lista2 = [sSI, sTI, sAI, sLMI]      

contAvancar = 0
contRecuar = 0
for i in range(4):
  if lista1[i] > lista2[i]:
    contAvancar += 1
  elif lista1[i] < lista2[i]:
    contRecuar += 1

if contAvancar >= 3:
  print("Avancar")
elif contRecuar >= 3:
  print("Recuar")
else:
  print("Permanecer")