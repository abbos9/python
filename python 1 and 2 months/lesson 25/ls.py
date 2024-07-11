# def separate(*args: str):
#     numbers = set()
#     small_alp = set()
#     big_alp = set()
#     for num in args:
#         for word in num:
#             if word.islower():
#                 small_alp.add(word)
#             elif word.isupper():
#                 big_alp.add(word)
#             else:
#                 numbers.add(word)
#     return numbers, small_alp, big_alp
#
#
# res = separate('1Ab2ASGxsa', 'SU12an', 'aSDcm34', 'ds4NKl32')
# print(res)
# 1
# def dictioner(**kwargs):
#     for key, value in kwargs.items():
#         return key, value
#
#
# res = dict(a=23, b=34, c=342)
# print(res)
# def daraja(**kwargs):
#     for values, key in kwargs.items():
#         kwargs[key] = values ** 2
#     return kwargs
#
#
# res = daraja(a=23)
# print(res)
# 3
# my
# def I_do_not_know(**kwargs):
#     d = dict()
#     for key, val in kwargs.items():
#         for harf in key, val:
#             if harf in 'aoeui':
#                 kwargs[key] = kwargs.values()
#
#     return
# techer's
# def test(**kwargs: int):
#     new_dict = dict()
#     for key in kwargs.keys():
#         unli = ""
#         undosh = ""
#         for letter in key:
#             if letter in "aioueAIOUE":
#                 unli += letter
#             else:
#                 undosh += letter
#
#         new_dict[undosh] = unli
#
#     return new_dict
#
#
# res = test(olma=10, behi=20, cocacola=30)
# print(res)
# 4
# def upp(**kwargs):
#     count = 0
#     for key, val in kwargs.items():
#         for letter in key:
#             if letter not in "aioueAIOUE":
#                 count += 1
#             kwargs[key] = count * val
#     return kwargs


# res = upp(Saidabbos=150, Ismoil=200, Ibrohim=400)
# print(res)

# homework

# 1. kwargs qabul qiladigan funksiya yozing va ularni hamma valuelarini listga solib qaytaring.
# def a(**kwargs):
#     values = list()
#     for key, value in kwargs.items():
#         # if value in kwargs:
#         values.append(value)
#     return values
#
#
# res = a(a=23, b=3232, c=42)
# print(res)


# 2. kwargs qabul qiladigan funksiya yozing va hamma valuelarini yigindisini toping.
# def counter(**kwargs):
#     count = 0
#
#     for key, value in kwargs.items():
#         if kwargs.values():
#             count += value
#
#     return count
#
#
# res = counter(a=323, b=3424, c=34)
# print(res)
# 3. kwargs qabul qiladigan funksiya yozing va hamma keylarni listga qoshib qaytaring.

# def abc(**kwargs):
#     keys = []
#     for key, value in kwargs.items():
#         if kwargs.keys():
#             keys.append(key)
#     return keys
#
#
# res = abc(a=332, b=332, c=4324)
# print(res)
