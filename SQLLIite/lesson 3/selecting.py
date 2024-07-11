import sqlite3

conn = sqlite3.connect('mars.db')

cursor = conn.cursor()

# cost = cursor.execute("""
# # SELECT MAX(cost),name FROM shop;
# # # """).fetchone()[1]
# # costs = cursor.execute("""
# # SELECT MIN(cost),name FROM shop;
# # """).fetchone()[1]
# # cost1 = cursor.execute("""
# # SELECT SUM(cost),name FROM shop;
# # """).fetchone()[0]
# #
# # print(cost1, cost, costs)
# keyboard = cursor.execute("""
# SELECT * FROM shop WHERE name="ipad";
# """).fetchone()

keyboard = cursor.execute(f"""
SELECT * FROM shop WHERE name LIKE %'A'% AND %'e'%;
""").fetchone()

name = input('enter you product name: ')

products = cursor.execute(f"""
SELECT * FROM shop WHERE name LIKE '%{name}%';
""").fetchall()

for product in products:
    print(product)
