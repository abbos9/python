import requests


def get_data_nbu():
    link = 'https://nbu.uz/uz/exchange-rates/json/'
    nbu = requests.get(link).json()
    text = ''
    for cur in nbu:
        text += f"{cur['title']}| {cur['code']} | {cur['cb_price']}\n"
    return text


def get_one_cur(code: str):
    link = "https://nbu.uz/uz/exchange-rates/json/"
    nbu = requests.get(link).json()
    text = "Siz bergan code bo'yicha hech narsa topilmadi"
    for cur in nbu:
        if code == cur['code']:
            text = f"{cur['title']} | {cur['code']} | {cur['cb_price']}\n"
            break
    return text


def get_kop_cur(code: str,price:float):
    link = "https://nbu.uz/uz/exchange-rates/json/"
    nbu = requests.get(link).json()
    data = "Siz bergan code bo'yicha hech narsa topilmadi"
    for cur in nbu:
        if code == cur['code']:
            text = float(cur['cb_price'])
            money = cur['code']
            res = text * price
            data = f"{money} | {res}"
            break
    return data
