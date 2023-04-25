# lambda
# map
# filter

# def daraja(a,b):
#     return a**2

# print(daraja(4))

# daraja = lambda a: a ** 2
# print(daraja(4))

# yigindi = lambda a,b: a + b
# print(yigindi(2,3))


# from math import pi

# s = lambda r: pi*(r**2)
# print(s(2))

# def yuza(r):
#     return pi*(r**2)

# l = list(range(10))
# sum(l)
# def Sum(l):
#     s = 0
#     for i in l:
#         s += i
#     return s

# def daraja(x):
#     return x**2

# h = list(range(1,10))

# k = list(map(daraja,[1,2,3,4,5,6,7,8,9]))
# k3 = list(map(lambda x:x**2,[1,2,3,4,5,6,7,8,9]))
# print(k, k3)

# k2 = []
# for i in [1,2,3,4,5,6,7,8,9]:
#     k2.append(daraja(i))
# print(k2)

l1 = list(range(2,5)) # [2, 3, 4]
l2 = list(range(5,9)) # [5, 6, 7, 8]
# res = [7, 9, 11]

# for i, j in enumerate(res):
#     print(i, j)

# res = []
# for i in range(3):
#     res.append(l1[i] + l2[i])
# print(res)

# res = [ l1[i] + l2[i] for i in range(3) ]

# def qoshish(x,y):
#     return x + y

# res = list(map(lambda x,y: x+y, l1, l2))
# print(res)

mevalar = ['apple', 'banana', 'cherry']
# res = list(map(lambda x: x.upper(), mevalar))
# print(res)

# import random
# l = list(range(200,1000))
# k = random.sample(l, 10)
# print(k)


# summa = lambda toplam: sum(toplam)
# print(summa(l))

# d = lambda x: '4' in x
# print(d('banana'))

# t = list(filter(lambda x: 'a' in x, mevalar))
# print(t)
# t2 = []
# for i in mevalar:
#     if 'a' in i:
#         t2.append(i)


# l = [
#     ['*','*','*','*'],
#     ['*','*','*','*'],
#     ['*','*','*','*'],
#     ['*','*','*','*'],
#     ]
# for i,j in enumerate(l):
#     for m,n in enumerate(l[i]):
#         if i==m:
#             print(' '*i + l[i][m], end=' ')
#     print()
    

# i = 0
# while i < 10:
#     i += 1
#     if i%2!=0:
#         continue
#     else:
#         print(i)