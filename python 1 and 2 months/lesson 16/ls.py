# user = input("Введите свое имя: ")
# user = set(user)
# exe = []
# exe1 = {}
# for i in user:
#     if i in user:
# week = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
# user = input("write day of the week: ")
# w_ind = week.index(week)
# if user in week:
#     if week == "sunday":
#         print("saturday", 'monday')
#     else:
#         print(week[w_ind - 1], week[w_ind + 1])
# else:
#     print("you are stuped")
# month = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august ', 'september', 'october',
#          'november', 'december')
# user = input("write month of the year: ")
#
# if user in month:
#     if month == "december":
#         print("november", 'january')
#     else:
#         m_ind = month.index(month)
#         print(month[m_ind - 1], month[m_ind + 1])
# else:
#     print("you are stuped")
# homework
# 3. Odamdan ismini kitishini so'rang va uning ismidagi har bitta harfni alohida elemnt qilib tuple da saqlang. Va qaysi
#    harf eng ko'p ishlatilganini topib bering.
name = tuple(input("name: "))
name = tuple(name)

more_letter = name.count(name[0])
char = ""
for letter in name:
    count = name.count(letter)
    if count > more_letter:
        more_letter = count
        char = letter
print(char, more_letter)
