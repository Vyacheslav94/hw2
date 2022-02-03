x = int(1) # искомое кол-во яиц
while True:
    if x % 2 == 1 and x % 3 == 1 and x % 4 == 1 and x % 5 == 1 and x % 6 == 1 and x % 7 == 0:
        print(x)
        break
    else:
        x += 1
