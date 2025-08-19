import random
import time

def timer(f,x):
    time0=time.perf_counter()
    out=f(x)
    time1=time.perf_counter()
    print(time1-time0)
    return out

def int_log(a,b):
    num=1
    num2=0
    while True:
        if num-0.5>a:
            return num2-1
        num2+=1
        num*=b

def fme(a,b,n):
    out=1
    abu=True
    while abu:
        if b&1==1:
            out=(out*a)%n
        b//=2
        a=(a*a)%n
        if b==0:
            abu=False
    return out

def sd_finder(d):
    abu=True
    s=0
    while abu:
        if d%2==0:
            d//=2
            s+=1
        else:
            abu=False
    return [s,d]

def miller_rabin(to_test):
    if to_test==1:
        return False
    elif to_test==2:
        return True
    elif to_test%2==0:
        return False
    sd=sd_finder(to_test-1)
    s=sd[0]
    d=sd[1]
    for i in range(100):
        abu=True
        while abu:
            a=random.randint(to_test+1,to_test*10-1)
            if not a%to_test==0:
                abu=False
        good=False
        if fme(a,d,to_test)==1:
            good=True
        if not good:
            for r in range(s):
                if fme(a,(2**r)*d,to_test)==to_test-1:
                    good=True
                    break
        if not good:
            return False
    return True

def find_large_prime(digits):
    abu=True
    while abu:
        out=random.randint(10**(digits-1),10**digits)
        if miller_rabin(out):
            abu=False
    return out
