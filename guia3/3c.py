import random
import math

def function(rnd):
    var=(1/rnd)-1
    res=(math.exp(-(var**2)))/(rnd**2)
    return res

##integral entre 0 e infinito, luego la multiplicamos por 2 para que sea inf y -inf
def integral(n):
    g=0
    for _ in range(n):
        rnd=random.random()
        g+=function(rnd)
    prom=2*(g/n)
    return prom

def main():
    n=raw_input("ingrese un valor n\n")
    res=integral(int(n))
    print(res)
    return 0

if __name__=='__main__':
    main()
