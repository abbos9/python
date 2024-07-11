# MY

# def ip_adress_get(ip: str):
#     for i in ip:
#         for c in i:
#             if '.' in c:
#                 replaced = ip.replace("[.]")
#                 return replaced


# a = '112.3.54.23.32'
# result = ip_adress_get(ip=a)
# print(result)

# BETTER THAN MY

# def my_string_replace(args):
#     a = '[.]'
#     b = '.'
#     args = list(args)
#     args = '[.]'.join(args)
#     args = args
#
#     for i in args:
#         if a == i:
#             a = b
#
#     return args
#
#
# print(my_string_replace('112.3.54.23.32'))


# THE BEST
def get_ip_address(text: str):
    letter_A = '.'
    letter_B = '[.]'

    end_text = "".join(letter_B if letter == letter_A else letter for letter in text)
    return end_text


print(get_ip_address(text='112.3.54.23.32'))
