# def Hi(name, words):
#     text = words + ' ' + name
#     return text
#
#
# my_n = 'Saidabbos'
# word = "Asalomu Aleykum"
# r = Hi(my_n, word)
# print(r)
# 2
# print("1. lower")
# print("2. upper")
# print("3. strip")
# print("4. rstrip")
# print("5. lstrip")
# print("6. split")
# print("7. islower")
# print("8. isupper")
# print("9. isalpha")
# print("10. count")
#
#
# def lower(word: str):
#     new_word = word.lower()
#     return new_word
#
#
# def upper(word: str):
#     n_w = word.upper()
#     return n_w
#
#
# def strip(word: str):
#     n_w1 = word.strip()
#     return n_w1
#
#
# def rstrip(word: str):
#     n_w2 = word.rstrip()
#     return n_w2
#
#
# def lstrip(word: str):
#     n_w3 = word.lstrip()
#     return n_w3
#
#
# def split(word: str):
#     spl = word.split()
#     return spl
#
#
# def islow(word: str):
#     lw = word.islower()
#     return lw
#
#
# def isupper(word: str):
#     upp = word.islower()
#     return upp
#
#
# def isalp(word: str):
#     alp = word.islower()
#     return alp
#
#
# def count(word: str, wht: str):
#     cnt = word.count(wht)
#     return cnt
#
#
# text = input("Text kiriting: ")
# option = int(input("Enter option: "))
#
# if option == 1:
#     res = lower(text)
#     print(res)
# elif option == 2:
#     res1 = upper(text)
#     print(res1)
# elif option == 3:
#     res2 = strip(text)
#     print(res2)
# elif option == 4:
#     res3 = rstrip(text)
#     print(res3)
# elif option == 5:
#     res4 = lstrip(text)
#     print(res4)
# elif option == 6:
#     res5 = split(text)
#     print(res5)
# elif option == 7:
#     res6 = islow(text)
#     print(res6)
# elif option == 8:
#     res8 = isupper(text)
#     print(res8)
# elif option == 9:
#     res9 = isalp(text)
#     print(res9)
# elif option == 10:
#     what = input("count: ")
#     res10 = count(text)
#     print(res10)
# else:
#     print("bunaka soz yoq")
# 3


# def unli(users: str):
#     count = 0
#     for alp in users.lower():
#         if users == "а" or users == "о" or users == "у" or users == "э" or users == "и":
#             count = + 1
#
#
# user = input("text: ")
# r = unli(user)
#
# print(r)

# homework
# 1. ism qabul qilish va undagi hamma unli harflarni katta qilib qaytarish, shunday funksiya yozing
#    Masalan: sanjarebk => sAnjArbEk
# def upper(upp):
#     for letter in upp.lower():
#         if letter in "aioue":
#             upp.upper()
#     return letter
#
#
# user = input("name: ")
# r = upper(user)
# print(r)


# 2. text qabul qilish va uni ichida nechta so'z borligini topib qaytarish, shunday funksiya yozing
# def lens(user: str):
#     len(user)
#
#
# user1 = input("text: ")
# res = lens(user1)
# print(res)
# 3. string formatda ikkita son qabul qilish va ularni inegerga o'tkazib bir biriga qo'shish, shunday funksiya yozing

user = input('num: ')
user2 = input('num: ')


def plus(user: int, user2: int):
    result = user + user2
    return result


res = plus(user, user2)
print(res)
