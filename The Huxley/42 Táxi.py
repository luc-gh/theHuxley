def primo(n):
    cond = True
    for i in range(2,n,1):
        if n % i == 0: cond = False
    return cond
    
for i in range(int(input())):
    l = [float(i) for i in input().split()]
    if primo(int(l[0] * l[1])): print(f'{(l[0] * l[1] - l[0] * l[1] * 42 / 100):.2f}')
    else: print(f'{(l[0] * l[1]):.2f}')