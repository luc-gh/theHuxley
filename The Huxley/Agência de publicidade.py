soma = 0.0
for i in range(7):
    x = input()
    if x == "R�dio":
        if input() == "AM": soma += 300
        else: soma += 500
    elif x == "TV":
        if int(input()) > 20: soma += 2000
        else: soma += 1200
    elif x == "Revista": soma += 750
    else: soma += 1500
print(f'{soma:.2f}')