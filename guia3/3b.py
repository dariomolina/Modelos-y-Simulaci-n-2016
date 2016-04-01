import random

def function(rnd):
    var=(1/rnd)-1
    res=(var*(1+var**(2))**(-2))/(rnd**2)
    return res

def integral(n):
    g=0
    for _ in range(n):
        rnd=random.random()
        g+=function(rnd)
    res=g/n
    return res

def main():
    n=raw_input("ingrese un valor n\n")
    n=int(n)
    value=integral(n)
    print(value)
    return 0        
    
if __name__=='__main__':
    main()
