s = int(input())
li = [[i for i in input().split()]for i in range(s)]

d = dict()

for i in li:
    d.update({i[0]: (i[1], i[2], i[3])})

while True:
    x = input()
    if x == 'FIM':
        break
    t = x.split()
    a = d[t[0]]
    for i in a:
        if i == t[1]:
            print('Uhul! Seu amigo secreto vai adorar')
            break
    else:
        print('Tente Novamente!')