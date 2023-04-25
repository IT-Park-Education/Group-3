# 1-misol
# class Sonlar:
#     a = 35
#     b = 7
# s = Sonlar()
# print(s.a+s.b, s.a*s.b, s.a-s.b, s.a/s.b)

# 2-misol
# from math import sqrt
# class Uchb:
#     a = 3
#     b = 4
#     c = None

# u = Uchb()
# c = sqrt(u.a**2 + u.b**2)
# print('P', u.a + u.b + c)
# print('S', u.a*u.b/2)

# 7-misol

# class Hisobla():
#     s = 0

#     def count(self, n):
        # 1-usul
        # for i in range(1, n+1):
        #     self.s += i*(n+1-i)
        #     print(i,n+1-i)

        # 2-usul
        # sonlar = list(range(1, n+1))
        # for i,j in enumerate(sonlar):
        #     self.s += j*(n-i)
        # return self.s

        # 3-usul
#         sonlar = list(range(1, n+1))
#         self.s = sum(list(map(lambda x: x*(n+1-x), sonlar)))
#         return self.s

# obj = Hisobla()
# print(obj.count(5))

# 8-misol
# class Fib():
#     fibs = [1,1]

#     def summa(self, n):
#         for _ in range(n-2):
#             self.fibs.append(self.fibs[-1]+self.fibs[-2])

#         return self.fibs


# f = Fib()
# print(f.summa(10))


