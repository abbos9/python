# def k():
#     a = 10
#     b = 20
#     result = a * b
#     return result
#
#
# res = k()
# print(res)
# def kop(num1, num2):
#     result = num1 + num2
#
#     return result
#
#
# def iyir(num1, num2):
#     result = num1 - num2
#     return result
#
#
# def k(num1, num2):
#     result = num1 * num2
#     return result
#
#
# def ayir(num1, num2):
#     result = num1 / num2
#     return result
#
#
# def o(num1, num2):
#     result = num1 // num2
#     return result
#
#
# def n(num1, num2):
#     result = num1 ** num2
#     return result
#
#
# def x(num1, num2):
#     result = num1 % num2
#     return result


# numbers1 = int(input("number1: "))
# numbers2 = int(input("number2: "))
# sign = input("sign: ")
# if sign == "*":
#     res = k(numbers1, numbers2)
#     print(res)
# elif sign == "/":
#     res2 = ayir(numbers1, numbers2)
#     print(res2)
# elif sign == "+":
#     res3 = kop(numbers1, numbers2)
#     print(res3)
# elif sign == "-":
#     res4 = iyir(numbers1, numbers2)
#     print(res4)
# elif sign == "//":
#     res5 = o(numbers1, numbers2)
#     print(res5)
# elif sign == "**":
#     res6 = n(numbers1, numbers2)
#     print(res6)
# elif sign == "%":
#     res7 = x(numbers1, numbers2)
#     print(res7)
# else:
#     print("bunaqa operator yoq")

# homework

# 1. for va range orqali 3 va 5 ga bo'linadigan sonalarni yangi list ochib ushanga qo'shib boradiagn funksiya yozing
# a = []
#
#
# def listener():
#     for num in range(1, 100):
#         if num % 3 == 0 and num % 5 == 0:
#             a.append(num)
#     return a
#
#
# b = listener()
# print(b)
# 2. ichida 5 ta meva nomi bor list yarating va o'zingiz yoqtirmagan mevani uni ichidan olib tashlaydigan funksiya yozing
# a = ['olma', 'nok', 'tarvuz', 'qovun', 'olhori']
#
# b = input("fruit: ")
#
#
# def user():
#     if b in a:
#         a.remove(b)
#     return a
#
#
# r = user()
# print(r)
# 3. ichida 10 ta son bor list yarating va o'zingiz yoqtirgan sonning indexini topib beradigan funksiya yozing
# num = [13, 4, 5, 6, 7, 8, 20, 89, 534, 53, 5, 3, 90]
# print(num)
#
#
# def find_num_index(nums):
#     index = num.index(nums)
#     return index
#
#
# numbers = int(input("Num: "))
# r = find_num_index(numbers)
# print(r)
# 4. ichida 5 ta ism bor list yarating va 0-indexga o'zingizni ismingizni qo'shib beradigan funksiya yarating
# names = ['saidabbos', 'egamberdi', 'sanjar', 'ismoil', 'ibrohim']
# user = input("name: ")
#
#
# def add_name():
#     names.insert(0, user)
#     return names
#
#
# r = add_name()
# print(r)
# 5. ichida 10 son bor list yarating va eng kichkina va eng katta sonni o'rnini almashtirib beragigan funksiya yozingй
# num = [0.1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 8, ]
# max_num = max(num)
# min_num = min(num)
#
#
# def replace_num(nums):
#     num.insert(max_num, min_num)
#     num.insert(min_num, max_num)
#     num.remove(max_num)
#     num.remove(min_num)
#     return num
#
#
#  res = replace_num()
# print(res)
