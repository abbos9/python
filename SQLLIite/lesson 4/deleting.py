import sqlite3

conn = sqlite3.connect('mars.db')

cursor = conn.cursor()

cursor.execute("DELETE FROM evos WHERE id=8;")

conn.commit()
conn.close()
