



def even_fib_sum(n):
    # You may assume that maximum > 0
    fiblist=[0,1]
    for i in range(2,n+1):
        fiblist.append(fiblist[i-1]+fiblist[i-2])
    print(fiblist)
    fibevensum = 0
    fibevensum=fibevensum+ sum([even for even in  if even % 2 == 0])
    return fibevensum

print(even_fib_sum(100))