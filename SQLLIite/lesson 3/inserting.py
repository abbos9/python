import sqlite3

conn = sqlite3.connect('mars.db')

cursor = conn.cursor()

products = [
    (1, 'smart watch', 30,
     'https://olcha.uz/image/266x266/products/PorjBw0lqeB4L4Bjs8TkcbvNsYyP4zsh3bCdeQ8gKRjj6QpWaE3rWnYe7v6y.jpg',
     20),
    (2, 'apple', 20,
     'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-9kAUcxvGwBFNhxm3wXaK_zn7rGP2ROf6Ow&usqp=CAU',
     20),
    (3, 'rug', 10,
     'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg83RhhvoWFqQ3w2Xi0P6GhpWfrSA1w19ai_uu4ANz&s',
     20),
    (4, 'mouse ', 800,
     'https://i.rtings.com/assets/products/1htouLNw/amazonbasics-3-button-usb-wired-mouse/design-medium.jpg',
     20),
    (5, 'keyboard', 100, 'https://www.computerhope.com/cdn/keyboard/keyboard.jpg',
     20),
    (6, "jacket", 30,
     'https://hips.hearstapps.com/hmg-prod/images/tentree-cloud-shell-puffer-jacket-020-1675265725.jpg',
     20),
    (7, 'jeans', 20,
     'https://static.zara.net/photos///2023/I/0/1/p/8062/475/406/2/w/469/8062475406_1_1_1.jpg?ts=1689683399181',
     20),
    (8, 'pillow', 10,
     'https://cdn.thewirecutter.com/wp-content/media/2023/01/bedpillows-2048px-9999.jpg',
     20),
    (9, 'people', 800,
     'https://img.freepik.com/free-photo/people-taking-selfie-together-registration-day_23-2149096795.jpg',
     20),
    (10, 'ipad', 100,
     'https://kattabozor.s3.eu-central-1.amazonaws.com/ri/32c0cf55b2735b9f41414dd69e4736a7b4e365ebfc7bf57aa09a40859a57a2d0_nm5ERe_640l.jpg',
     20)

]

cursor.executemany("""
INSERT INTO shop VALUES(?,?,?,?,?)
""", products)

conn.commit()
conn.close()
