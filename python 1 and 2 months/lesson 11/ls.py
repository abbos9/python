# 1
# numbers = "8736236237"
#
# nums = 0
# for num in numbers:
#     num = int(num)
#     if num % 2 != 0:
#         nums += num
# print(nums)
# 2
# count = 0
# while count < 100:
#     count += 1
#     if count % 2 == 0:
#         print(count)
# 3
# user = int(input("0 dan kotta raqam kiriting: "))
# count = 0
# while count < user:
#     if user == 0:
#         print("siz 0 yozdis. 0 dan kotta son yozing")
#     elif user > 0:
#         count += 1
#
# print(count)
# homework
# 1. while orqali 1 dan 100 gacha bo'lgan sonlarni print qiling.
# count = 0
# while count < 100:
#     count += 1
#     print(count)
# 2. for va range orqali 1 dan 100 gacha juft sonlarni print qiling.
# num = 0
# for num in range(1, 100 + 1):
#     if num % 2 == 0:
#         print(num)
# 3. while orqali 1 dan 100 gacha 3 ga bo'linadigan sonlar nechta ekanligini toping
# count = 1
# while count < 100:
#     count += 1
#     if count % 3 == 0:
#         print(count)
# 4. for va range orqali 1 dan 100 ga bo'lgan sonlarni yig'indisini toping.
# num = 0
# i = 0
# for son in range(1, 100 + 1):
#     num += son
# print(num)
# 5. odamdan ikkita son sorang. Odam kiritgan 1-sonda 2-songacha bo'lgan sonlarni yig'indisini toping.
num = int(input("Num: "))
num1 = int(input("Num1: "))
summa = 0
for son in range(num, num1):
    summa += son

print(son)
