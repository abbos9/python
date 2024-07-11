import sqlite3

conn = sqlite3.connect('new.db')
cursor = conn.cursor()

pizzas1 = cursor.execute("SELECT *, MAX(price) FROM pizza").fetchone()
print(pizzas1)

pizzas0 = cursor.execute("SELECT * FROM pizza WHERE id= 4").fetchone()
print(pizzas0)

pizzas6 = cursor.execute("SELECT id,name FROM pizza").fetchall()
print(pizzas6)

pizzas2 = cursor.execute("SELECT *, MIN(price) FROM pizza").fetchone()
print(pizzas2)

pizzas = cursor.execute("SELECT  SUM(price) FROM pizza").fetchone()
print(pizzas)
