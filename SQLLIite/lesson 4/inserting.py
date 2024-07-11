import sqlite3

conn = sqlite3.connect('mars.db')

cursor = conn.cursor()

evos = [
    (1, 28, 'original lavash', 'http://cc.oqtepalavash.uz/api/image/0b6f0370-57c9-484f-87e3-141ba1d72a5b.jpg',
     'yumshoq non,pomidor,qizil sous va boshqa narsalar'),
    (2, 23, 'original lavash mini', 'http://cc.oqtepalavash.uz/api/image/3f6efb6f-1659-4899-abd2-70d61fe34560.jpg',
     'yumshoq non,pomidor,qizil sous va boshqa narsalar'),
    (3, 31, 'pishloqli lavash', 'http://cc.oqtepalavash.uz/api/image/483107e9-8235-4ba2-ad5d-44bd23de9ae5.jpg',
     'yumshoq non,pomidor,qizil sous, pishloq va boshqa narsalar'),
    (5, 26, 'pishloqli lavash mini',
     'http://cc.oqtepalavash.uz/api/image/33efc0af-c5d0-4c42-9310-5d329db484e2.jpg',
     'yumshoq non,pomidor,qizil sous, pishloq va boshqa narsalar'),
    (6, 29, 'tandir lavash', 'http://cc.oqtepalavash.uz/api/image/9fc53311-aaca-423d-9076-a05f39a86132.jpg',
     'yumshoq non,pomidor,qizil sous, pishloq, tandirda tayorlanadi va boshqa narsalar'),
    (7, 32, 'tandir lavash', 'http://cc.oqtepalavash.uz/api/image/448aa104-01be-4262-8547-a55cd81fcc1f.jpg',
     'yumshoq non,pomidor,qizil sous, pishloq, tandirda tayorlanadi va boshqa narsalar'),
    (8, 95, 'pizza asorti', 'http://cc.oqtepalavash.uz/api/image/4d97afb5-7301-49d2-9856-7e6cbe41d2be.jpg',
     'peperoni,pishloq,oq sous va boshqa narsalar'),
]

cursor.executemany("""
INSERT INTO evos VALUES(?,?,?,?,?)
""", evos)

conn.commit()
conn.close()
