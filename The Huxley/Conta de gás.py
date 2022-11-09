def conta(n:int) -> int:
    soma = 5
    for i in range(11,n+1,1):
        if i < 51: soma += 1
        elif i >= 51 and i < 81: soma += 2
        else: soma += 3
    return soma
    
x = int(input())
print(conta(x))