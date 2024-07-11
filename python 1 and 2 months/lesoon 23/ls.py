# def name_upper(name1: str):
#     for alp in 'aioue':
#         if alp in 'aioue':
#             name1.replace(alp, '@')
#     return alp
#
#
# name = input("entyer your name: ")
# res = name_upper(name)z
# print(res)
# 1
# def pluser(names: list):
#     namer = ""
#     for nam in names:
#         namer += nam
#
#     return namer
#
#
# name = ['alu', 'gani', 'bani', 'gali', 'ali', 'abbos']
# res = pluser(name)
# print(res)


# homework

# 1. Odamdan ismini kitishini so'rang va uni ismini return qiladigan funksiya yozing.


# user1 = input('enter your name: ')
#
#
# def name_returner(user_name):
#     name = user_name
#     return name
#
#
# res = name_returner(user1)
# print(res)


# 2. Odamdan ikkita son sorang va ularni qoshib beradigan funksiya yozib bering


# def pluser(num1: int, num2: int):
#     total = num1 + num2
#     return total
#
#
# user1 = int(input('enter your number1: '))
# user2 = int(input('enter your number2: '))
# res = pluser(user1, user2)
# print(res)


# 3. Odamdan ikkita son sorang va ularni kopaytirib beradigan funksiya yozing.

# def pluser(num1: int, num2: int):
#     total = num1 * num2
#     return total
#
#
# user1 = int(input('enter your number1: '))
# user2 = int(input('enter your number2: '))
# res = pluser(user1, user2)
# print(res)


# 4. Odamdan ismini sorang va uni ichida nechta harf borligini topib beradigan funksiya yozing.
# user = input('enter your name: ')
#
#
# def counter_alp(name: str):
#     count = len(name)
#     return count
#
#
# res = counter_alp(user)
# print(res)
# 5. Oila azolarizni ismlarini list ichida saqlang va odamdan kimmni chopish kerakligini sorang
#    va odam kiritgan ism listni ichida bor bolsa chopib tashlang. Agar yoq bolsa bunday ism
#    yoq desin


try:
    family_name = ['Saidabbos', 'Egamberdi', 'Hojarkar', 'Nigora', 'Hotam']
    deleter = input('enter the name which you want delete: ')
    for name in family_name:
        if deleter in family_name:
            family_name.remove(deleter)
            print(family_name)
except ValueError:
    print('kiritilgan  ism mavjud emas')
# except IndexError:
#     print('kiritilgan  ism mavjud emas')
