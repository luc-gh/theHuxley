categ = input()
value = float(input())
cashb = float(input())
if categ.lower() == "infinity": print(f'{5*value/100:.2f}')
elif categ.lower() == "platinum":
    if cashb <= 2.5*value/100: print(f'{cashb:.2f}')
    else: print(f'{2.5*value/100:.2f}')
elif categ.lower() == "gold":
    if cashb <= value/100: print(f'{cashb:.2f}')
    else: print(f'{value/100:.2f}')