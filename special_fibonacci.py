def f(n):
    if n==1 or n==0:
        return 1
    else:
        return (f(n-1)*f(n-1) + (n-2)*(n-2))%47
print(f(6))

'''def fibb(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return (fibb((n-1)**2+ (n-2)**2)%47)
print(fibb(6))
'''



