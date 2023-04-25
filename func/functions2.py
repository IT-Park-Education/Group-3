# *args - argumentlar
# **kwargs - key-value argumetlar

# def test(a, *args):
#     print(a,args)
# test(4,5, 6,'asdas')

# def test(ism, **kwargs):
#     print(ism, kwargs.get('age'))

# test('Baxtiyor', age=25, nationality='Uzbek')

# def make_dict(**kwargs):
#     return kwargs

# def ask_question(k):
#     ism = input(k[0].title() + ' : ')
#     yosh = input(k[1].title() + ' : ')
#     fam = input(k[2].title() + ' : ')
#     return make_dict(ism=ism, yosh=yosh, familiya=fam)

# k = ['ism', 'yosh', 'familiya']

# print(ask_question(k))

# def Print(a, summa):
#     summa+=a
#     # print(summa)
#     if summa==10:
#         print(summa)
#         return summa
#     Print(a, summa)

# k = Print(1, 0)
# print(Print(1, 0))


# def Calculate(a, b, op):
#     if op == 1:
#         return a-b
#     elif op == 2:
#         return a*b
#     elif op == 3 and b!= 0:
#         return a/b
#     return a+b

# print(Calculate(6,3,2))

# import math

# def IsSquare(k):
#     print(math.sqrt(k))
#     return 

# l = list(range(1,5))
# q = 0
# for i in l:
#     if IsSquare(i):
#         q += 1

# a = 7557
# 15

# l = [1, 2, 3, 4, 5, 6, 7]
# print(l[::-1])

#123321
# def Ispalindron(k):
#     k = str(k)
#     l = len(str(k))//2
#     for i in range(l):
#         if k[i]!= k[-i-1]:
#             return
#     print(True)

# Ispalindron(1239321)
    
    
# def Fibonacci(n):
#     fibs = [1, 1]
#     for i in range(n-2):
#         fibs.append(fibs[-1]+fibs[-2])
#     return fibs[n-1]

# f = Fibonacci(7)
# print(f)

# def Digit_Count(k):
#     return len(str(k))

# print(Digit_Count(15))