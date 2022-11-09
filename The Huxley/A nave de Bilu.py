nave = [int(i) for i in input().split()]
base = [int(i) for i in input().split()]
if nave[0] <= base[0] and nave[0] <= base[1] and nave[1] <= base[0] and nave[1] <= base[1]: print("Pousa, bilu")
else: print("Procura outro lugar, bilu")