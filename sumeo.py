def sum_eo(n,t):
    if t == 'e':
        sum = 0
        for v in range(0,n):
            if v%2 == 0:
                sum += v
                print(sum)
        print(sum)        
        return sum
    elif t == 'o':
        sum = 0
        for v in range(0,n):
            if v%2 != 0:
                sum =+ v
        return sum
    else:
        return -1


sum_eo(10,'e')