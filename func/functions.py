def qoshish(a,b):
    return a+b

def ayirish(a,b):
    return a-b

def kopaytirish(a,b):
    return a*b

def bolish(a,b):
    a,b = 5,0
    if b==0:
        return "Bo'luvchi 0 ga teng bo'lmasligi kerak"
    return a/b

def summa(l):
    s = 0
    for i in l:
        if type(i) is not int:
            return f"{i} is not an integer"
        s += i
    return s

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0
#range(5,10)

def RANGE(b,a=0,d=1):
    if b<a:
        b,a = a,b
    l, i = [], a
    while i<b:
        l.append(i)
        i += d
    return l