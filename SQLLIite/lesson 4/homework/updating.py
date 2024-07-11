import sqlite3

conn = sqlite3.connect('mars.db')

cursor = conn.cursor()
cursor.execute("""
UPDATE my_IT_class SET name=Sanjar WHERE id=1;
""")

conn.commit()
conn.close()