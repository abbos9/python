# num=1
# def true_or_false()
# lib = [1, 2, 4, 5, 3, 3]
# if len(lib) == len(set(lib)):
#     print(True)
# else:
#     print(False)

# num = 2

# nums = [1, 2, 4, 105, 3, 99]
#
# max_num = max(nums)
# min_num = min(nums)
#
# max_index = nums.index(max_num)
# min_index = nums.index(min_num)
#
# nums[max_index] = min_num
# nums[min_index] = max_num
#
# print(nums)

# num = 3

# names = ['salom', "O'zbekiston", 'qaleysan']
#
# longest_name = max(names, key=len)
# # print(longest_name)
# for i in names:
#     if longest_name == i:
#         print(i,',', names.index(i))

# UYGA VAZIFA
# def check_email(email: str):
#     if len(email) > 5:
#         if '@gmail.com' in email and not ' ':
#             print(email)
#     else:
#         print('invalid')
#
#
# email = input('enter your email: ')
#
# print(check_email(email=email))

# ai
# def emailni_tekshirish(email):
#     # email oxiri @gmail.com bilan tugashi va @ 1 marta qatnashgan bo'lishi kk
#     if not email.endswith("@gmail.com") or email.count("@") != 1:
#         return False
#
#     # email ichida bo'sh joy bo'lmasligi kerak
#     if " " in email:
#         return False
#
#     # @gmail.com gacha bo'lgan qismining uzunligi 5 dan katta bo'lishi kk
#     if len(email.split("@")[0]) <= 5:
#         return False
#
#     return True
#
#
# print(emailni_tekshirish("example@gmail.com"))  # True chiqadi
# print(emailni_tekshirish("exa@gmail.com"))  # False chiqadi
