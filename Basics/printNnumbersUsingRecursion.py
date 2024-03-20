def recursion(n):
    if(n==0):
        print(0)
    else:
        print(n)
        return recursion(n-1)
    return 0

recursion(5)