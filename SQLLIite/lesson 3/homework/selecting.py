import sqlite3

conn = sqlite3.connect('mars.db')

cursor = conn.cursor()

cost = cursor.execute("""
 SELECT MAX(price),name FROM evos;
 """).fetchone()[1]
costs = cursor.execute("""
SELECT MIN(price),name FROM evos;
""").fetchone()[1]
cost1 = cursor.execute("""
SELECT SUM(price),name FROM shop;
""").fetchone()[0]

print(cost1, cost, costs)
keyboard = cursor.execute("""
SELECT * FROM shop WHERE name="hot-dog mini";
""").fetchone()

name = input('enter you product name: ')

products = cursor.execute(f"""
SELECT * FROM shop WHERE name LIKE '%{name}%';
""").fetchall()

for product in products:
    print(product)
