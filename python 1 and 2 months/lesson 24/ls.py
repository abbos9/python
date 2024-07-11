# def adder(*args):
#     summa = 0
#     for num in args:
#         summa += num
#     return summa
#
#
# res = adder(1,4,5,67,8,9,67)
# print(res)\
# 1
# def jufter(*args):
#     juft = []
#     for num in args:
#         if num % 2 == 0:
#             juft.append(num)
#     return juft
#
#
# res = jufter(1, 24, 46, 66, 6, 8, 98, 8, 90, 0, 8, 9, 9, 89)
# print(res)
# 2
# def multiplay(*args):
#     plus = 0
#     minus = 0
#     for num in args:
#         if num % 2 == 0:
#             plus += num
#
#         else:
#             minus += num
#
#     result = plus * minus
#
#     return result
#
#
# res = multiplay(12, 67, 8, 9, 90, 98, 978, 76, 566, 7)
# print(res)
# 3
#
#
# def meva(*args):
#     count = 0
#     for mev in args:
#         for i in mev:
#             if i in "aoiue":
#                 count += 1
#
#     return count
#
#
# res = meva('olma', 'piyoz', 'nok')
# print(res)
# Uyga vazifa:

# 1. Nomalum miqdorda args qabul qiling va ularni ichidan eng kichkinasini topib return qiling.

# def small(*args):
#     return min(args)
#
#
# res = small(1324, 35, 232, 32, 44324, 57, 56, 76, 45, 37, 696, 898, 34, )
# print(res)
# 2. args qabul qiladigan funksiya yozing va ularni hammasi son bolsin, sizni vazifangiz ularni ichidan
#    0 dan kichkinalarni alohida, 0 dan kattalarini alohida qilib qaytaring.

# def function(*args):
#     zeroplus = []
#     zerominus = []
#     for num in args:
#         if num <= 0:
#             zerominus.append(num)
#         elif num >= 0:
#             zeroplus.append(num)
#         else:
#             print('hato')
#     return zeroplus, zerominus
#
#
# res = function(12, -332, 43, -566, 4, -6, -543, 4, 46, -3, 5, -6, 6,-5, 65, -345, 443, -6, )
# print(res)
