a = 1 
for a in range (101):
    if a % 7 == 0:
        pass
    elif a // 10 == 7:
        pass
    elif a % 10 == 7:
        continue
    else:
         print(a)
