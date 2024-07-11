# with open('mahsulotlar.txt', 'r') as reader:
#     data = reader.read()
#
# with open('mahsulotlar.txt', 'w') as writer:
#     writer = writer.read()

# with open('mahsulotlar.txt', 'a') as appender:
#     appender = appender.read()

# 1

# import os
#
# if not os.path.exists('juft.txt'):
#     with open('juft.txt', 'x') as create:
#         create = create.read()
# if not os.path.exists('toq.txt'):
#     with open('toq.txt', 'x') as create1:
#         create1 = create1.read()
#
#
# c = 1
#
# while c < 10:
#     c += 1
#     user = int(input('num: '))
#     if user % 2 == 0:
#         with open('juft.txt', 'a') as appender:
#             appender = appender.write(str(f'{user}\n'))
#     else:
#         with open('toq.txt', 'a') as appender:
#             appender = appender.write(str(f'{user}\n'))

# 2
# while True:
#     try:
#         index = int(input("Index: "))
#
#         names = ['ali', 'vali', 'gani']
#         name = names[index]
#         print(name)
#
#     except IndexError:
#         print("Bunday ism yo'q")

# 3
# while True:
#     try:
#         user1 = int(input("num1: "))
#         user2 = int(input("num2: "))
#         print(user1 / user2)
#     except ZeroDivisionError:
#         print("bunka bololmaysiz")

# homework
# 1. Odamdan ismini kiritishi so'rang. Va uning ismini ichida nechta a harfi borligini topib beradigan funksiya yozing.
#    Xatolarni oldini ham oling. Masalarn ismini emas raqam kiritib yuborishi mumkin


# while True:
#
#     try:
#         user = input('enter your name: ')
#
#
#         def lener(name):
#             name.isalpha()
#             name = len(name)
#             return name
#             res = lener(user)
#             print(res)
#     except ValueError :
#         if user.isalnum():
#             print('you write number')

# 2. Odamdan ismini kiritishini sorang va shu ismi bilan txt fayl ochib beradigan funksiya yozing. Agar bunaqa nomli
#    fayl bor bolsa xato berishi mumkin siz shu xatoni oldini oling.
# import os
#
# try:
#     user = input('enter new file name: ')
#     if not os.path.exists(f'{user}'):
#         new_file = open(user, 'x')
#
# except FileExistError :
#     print('bunaka fayl mavjud')

# 3. O'yinchini ismini key uning balini esa value qilib saqlab ketadigan dict yarating. Odamdan oyinchini ismini
#    kiritishini sorang agar bunaqa ismli oyinchi yoq bolsa key error berishi mumkin siz shuni oldini oling.
d = {
    'ismoil':
        9,
    'egamberdi':
        8,
    'abbos':
        6,
    'saidabbos':
        10,

}
# a = d.values()
user = input("enter player name: ")
while True:
    try:
        for user in d.keys():
            if user in d.keys():
                pass

    except KeyError:
        print('bunaka ism yoq')
