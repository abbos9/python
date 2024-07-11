# numbers = [12, 12, 1, 22, 3, 4, 5, 6, 7, 6, 5, 334, 5, 56]
# index = 0
# for nums in numbers:
#     if nums % 2 == 0:
#         pass
#     while index <= len(numbers):
#         if index % 2 == 1 and nums[index] % 2 == 1:
#             print(index)
#         index += 1
#
# set_example = {'saidabbos', 'abbos', 'said', 'ismoil', 'ibrohim'}
# user = input("name: ")
# if user in set_example:
#     set_example.remove(user)
# else:
#     print("bunaka ism yoq")
#
# print(set_example)
# 1
# class_a = {'saidabbos', 'abbos', 'ibrohim', 'kalishbek', 'sanjarbek'}
# class_b = {'ahmoqhon', 'toronbek', 'ibrohim', 'kalishbek', 'sanjarbek'}
# class_c = class_a.intersection(class_b)
# print(len(class_c))

# user = input('name: ')
# user1 = set()
# for i in user:
#     user1.add(i)
# print(user1)
# homework
# 2. Odamdan ikkita ism sorash va ikkalsida ham bor harflarni rint qilish
# user1 = set(input('name: '))
# user2 = set(input('name: '))
# safe = user1.intersection(user2)
# print(safe)
# 3. IChida 5 ism bor set yaratasiz, odamdan ismini soraysiz agar bunaqa ism
#    bor bolsa bor desin yoq bolsa uni ismini qoshib qoying.
# set_example = {'saidabbos', 'abbos', 'said', 'ismoil', 'ibrohim'}
# user = input("name: ")
# if user in set_example:
#     print("bunaka ism bor")
# else:
#     set_example.add(user)
#     print(set_example)
# 4. Odamdan qaysi davlatda yashashini sorash va uni ichida unli
#  harflarni setga qoshib ketish
# country = input("country: ")
# set1 = set()
# for name in country:
#     if name == 'a' or name == 'u' or name == 'i' or name == 'e' or name == 'o':
#         set1.add(name)
# print(set1)
