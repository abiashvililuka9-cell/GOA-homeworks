def stringg(integerr):
    list = ['!','@','$','%','^','&','*','(',')','+','#']
    for i in range(0, len(integerr), 1):
        if integerr[i] in list:
            return 'ivalid input'
        else:
            return int(integerr)


print(stringg('!123'))




