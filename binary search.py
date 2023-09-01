# There we start making the binary screach program
a=[-1,0,3,5,9,12,15]
target = 9
len= len(a)
len = int(len/2)
if a[len] == target:
    print(len)
elif a[len] < target:
    while(1):
        len = len +1
        if a[len] == target:
            print(len)
            exit()
if len > target:
    while(1):
        len = len -1
        if a[len] == target:
            print(len)
            exit()
else:
    print(-1)
