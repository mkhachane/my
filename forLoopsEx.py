
num = 2
for i in range(1,10+1):
    print num,"*",i,"=",num*i




for num in range(1,30):
    if num > 1:
        for i in range(2,num):
            if (num%i) == 0:
                break
        else:
            print num

