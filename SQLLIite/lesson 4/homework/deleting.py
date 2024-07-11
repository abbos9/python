import sqlite3

conn = sqlite3.connect('mars.db')

cursor = conn.cursor()

cursor.execute("DELETE FROM classmates WHERE id=9;")

conn.commit()
conn.close()
