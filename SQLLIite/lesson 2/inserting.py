import sqlite3

conn = sqlite3.connect('new.db')
cursor = conn.cursor()

pizzas = [
    (1, "Combo", 89000, 'bu pitsa manga yoqmidi', 'link'),
    (2, "peperoni", 100000, 'bu pitsa manga yoqmidi', 'link'),
    (3, "sosage", 189000, 'bu pitsa manga yoqmidi', 'link'),
    (4, "mushroom", 289000, 'bu pitsa manga yoqmidi', 'link'),
    (5, "meat", 90000, 'bu pitsa manga yoqmidi', 'link')
]

cursor.executemany("""
INSERT INTO pizza(id,name,price,description,photo) VALUES(?,?,?,?,?)
""", pizzas)

conn.commit()
print('code runned')
