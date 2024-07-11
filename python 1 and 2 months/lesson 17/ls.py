# student = {
#     "Ismoil": {
#         "age": (13,),
#         "grade": 5,
#         "subjects": ["fronted", "pyton", "javascript"],
#         "name": "Ismoil",
#         "study_it": "mars It school "
#     },
#     "Ibrohim_Asqarov": {
#         "age": (13,),
#         "grade": 5,
#         "subjects": ["math", "English", "russian"],
#         "name": "Ibrohim_Asqarov"
#                 "study_it""mars It school "
#     },
#     "Saidabbos": {
#         "age": (14,),
#         "grade": 5,
#         "subjects": ["Math", "English", "pe"],
#         "name": "Saidabbos"
#                 "study_it""mars It school "
#     }
# }
# user = input("name of movie: ")
# movies = {
#     'avatar': 5,
#     'jumanji': 4,
#     'detpul': 3.5,
#     'marvel': 4.5,
# }
#
# if user == 'avatar':
#     print(movies['avatar'])
# elif user == 'jumanji':
#     print(movies['jumanji'])
# elif user == 'detpul':
#     print(movies['detpul'])
# elif user == 'marvel':
#     print(movies['marvel'])
# else:
#     print("bunaka kino yoq")
# num = 0
# while num < 100:
#     num += 1
#     if num == 34:
#         continue
#     elif num == 65:
#         break
#     else:
#         print(num)
# homework
# 1. O'yinchilarni achkolarini hisoblaydigan dict yarating. Key ularni ismi bo'ladi value nechi achkosi borligi.
#    odamdan 10 martta input sifatida ismini soraysiz va usha ismli o'yinchii achkosini birga oshirib qoyasiz, Oxirida
#    dictni print qilib qo'yasiz.
players = {
    'saidabbos': 94,
    'ibrohim': 205,
    'ismoil': 405,
    'egamberdi': 45,
    'behruz': 304,
}

for i in range(10):
    name = input("Enter player's name: ")
    if name in players:
        players[name] += 1
    else:
        players[name] = 1
print(players)

# 2. Oila a'zolarini ismlarnikey qilib ular haqida quyidagi ma'lumotni dict qilib value qilib saqlang
# family = {
#     "Egamverdi": {
#         "bo'y": 165,
#         "ism": "Egamberdi",
#         "familiya": "Azimjonov",
#         "yosh": 13,
#         "qolidan keladigan narsala": ['bekorchi', 'uxalsh', 'telefon oynash', 'boltat qilish']
#     },
#     "Hosiyat": {
#         "bo'y": 135,
#         "ism": "Hosiyat",
#         "familiya": "Athamova",
#         "yosh": 10,
#         "qolidan keladigan narsala": ['bekorchi', 'baqirish', 'telefon oynash', 'odamni asabini bizish']
#     },
#     "Nigora": {
#         "bo'y": 179,
#         'ism': 'Nigora',
#         "familiya": 'Abduhamidova',
#         'yosh': 37,
#         "qolidan keladigan narsala": ['idish yuvish', 'oyim uzistla', 'pul ishlab topish', ]
#     },
#     'Hotam': {
#         "bo'y": 179,
#         'ism': 'Hotam',
#         "familiya": 'Gaziev',
#         'yosh': 42,
#         "qolidan keladigan narsala": ['ogi narsa buyim kotarish', 'baland baqirish', 'pul ishlab topish', ]
#     }
# }
