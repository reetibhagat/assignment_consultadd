x=[1,1,2,4,6,8,9,1,2,3,1,2,1,5]
mu=3


def cusum(x,mu):
    out=[0]
    for i in range(len(x)):
        out.append(max(0,+out[i]+(x[i]-mu)))
    return out
x =[1,1,2,4,6,8,9,1,2,3,1,2,1,5]
mu = 3
print(cusum(x,mu))
# assert cusum(x,mu) ==[0,0,0,0,1,0,1,4,9,15,13,12,12,10,9,7,9]