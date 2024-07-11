import sqlite3
from aiogram.types import InputFile

conn = sqlite3.connect('mars.db')

cursor = conn.cursor()

evos = [
    (1, 23.900, 'mol goshtli lavash', 'photo', 'juda mazali'),
    (2, 25.900, 'dieta-set', 'photo', 'juda mazali'),
    (3, 27.900, 'sprite', 'photo', 'juda mazali'),
    (4, 29.900, 'cola', 'photo', 'juda mazali'),
    (5, 21.900, 'ice cream', 'photo', 'juda mazali'),
    (6, 20.900, 'chair', 'photo', 'juda mazali'),
    (7, 19.900, 'straw', 'photo', 'juda tez bizilmaydi'),
    (8, 90.900, 'kabob', 'photo', 'juda mazali'),
    (9, 50.900, 'hot-dog korolevskiy', 'photo', 'juda mazali'),
    (10, 12.900, 'hot-dog mini', 'photo', 'juda mazali'),
]

cursor.executemany("""
INSERT INTO evos VALUES(?,?,?,?,?)
""", evos)

conn.commit()
conn.close()
