for i in range(1000,10000,1):
    if int(i/1000) == int(((i%10)%10)%10) and int((i/100)%10) == int(((i/10)%100)%10):
        print(i)