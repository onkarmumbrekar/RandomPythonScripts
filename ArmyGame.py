
def eo(x):
    if x%2==0:
        return x/2
    else:
        return ((x-1)/2)+1
n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
if n<=1000 and m<=1000 and n>0 and m>0:
    np = int(eo(n))
    mp = int(eo(m))
    min_package = np*mp
    print(min_package)