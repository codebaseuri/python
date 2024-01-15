
import sys
import math
sys.set_int_max_str_digits(10000000)
import time
def foo(a,q,p):#a^q modp in fast time

    if q==0:
        return 1
    if q==1:
        return a%p
    if q%2==1:
        return (foo(a,q//2,p)*foo(a,q//2,p)*a)%p
    return (foo(a,q//2,p)*foo(a,q//2,p))%p

def foo2(a,q,p):#a^q modp in slow time
    #sum=1
    #for i in range(q):
        #sum*=a
   # return sum%p
    time.sleep(1)
    return pow(a,q,p)
var1=time.time()
print(foo(71230078989798978687678,94321,11))
var2=time.time()
print(foo2(71230078989798978687678,94321,11))
var3=time.time()
print(var2-var1)
print(var3-var2)

