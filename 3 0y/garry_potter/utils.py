import requests


def get_all_name():
    link = 'https://hp-api.onrender.com/api/characters'
    data = requests.get(link).json()
    text = ''
    for person in data[:20]:
        text += person['name'] + '\n'
    return text


def get_all_house():
    link = 'https://hp-api.onrender.com/api/characters'
    data = requests.get(link).json()
    houses = ''
    for house in data[:20]:
        houses += house['house'] + '\n'
    return houses


def random_inf():
    import random
    link = 'https://hp-api.onrender.com/api/characters'
    data = requests.get(link).json()
    rand = random.choice(data)
    text = f"""
-{rand['name']}
-{rand['alternate_names']}
-{rand['house']}
-{rand['gender']}
    """
    return text
