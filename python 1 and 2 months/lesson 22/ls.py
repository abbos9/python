# for numbers in range(0, 10 + 1):
#     pass
#
# import os
#
# if not os.path.exists('nums'):
#     with open('nums', 'x') as new_file:
#         pass
# with open('nums', 'a') as appender:
#     appender.write(str(numbers))
# while True:
#     try:
#         user = int(input('enter your age: '))
#         age = (2023 - user)
#         print(age)
#     except ValueError:
#         print('hato')
# sinif ishi
# 1
# def bolish():
#     b = user1 / user2

# d = {
#     "ali": 14,
#     "gani": 25,
#     "vali": 34,
# }
#
# while True:
#     try:
#         user = input("Enter your key: ")
#         print(d[user])
#         if user.isdigit():
#             print('raqam hato')
#     except KeyError:
#         print('bunaka kety yoq')
# homework
# 1. Ikkita son qabul qiladigan funksiya yozing. U funksiyani vazifasi qaysi biri katta bo'lsa ushani qaytarish.
# Odamdan ikkita son so'rang va usha sonlarni funksiyaga berib yuboring. Odam raqam emas harf kiritganda xato
# chiqishini oldini oling.

# def pluser(num1: int, num2: int):
#     while True:
#         try:
#             if num1 > num2:
#                 return num1
#             else:
#                 return num2
#         except Exception:
#             return 'ra qam kiriting'
#
#
# use1 = input('num1: ')
# use2 = input('num2: ')
# res = pluser(use1, use2)
# print(res)

# 2. Ichida 5 ism bor list yarating. Va odamdan qaysi index dagi ismni olmoqchi ekanligini so'rang.
# Agar odam listni ichida mavjud bo'lmagan index ni kiritsa xato chiqadi. Siz shu xatoni oldini oling.
# names = ['gani', 'ali', 'bani', 'Egamberdi', 'Sanjarbek']
# while True:
#     try:
#         user = int(input("enter your name's index: "))
#         print(names[user])
#     except IndexError:
#         print('mavjud bolmagan index kiritingiz')
# 3. ism:yosh holatida dict yarating. Ichida kamida 5 ism bor bo'lsin. Odamdan qaysi ismni olish kerakligni
# so'rang. Agar dict ni ichida yo'q bo'lgan ismni kiritsa xato chiqadi. Siz shu xatoni oldini oling.
dic = {
    'Egamberdi': 14,
    'saidalo': 14,
    'Saidabbos': 14,
    'Sanjarber': 24,
    'ilon': 68  # sinif rahbarim

}
while True:
    try:
        user = input("enter your prople name: ")
        print(dic[user])
    except  KeyError:
        print('bunaka ism mavjud emas!!!')
