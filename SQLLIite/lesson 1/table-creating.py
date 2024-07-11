import sqlite3

conn = sqlite3.connect('mars.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER,
    full_name TEXT,
    phone_num TEXT,
    age INTEGER

)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS shop (

    id INTEGER,
    name TEXt,
    cost INTEGER,
    photo TEXT,
    count INTEGER    

)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS name(

    id INTEGER,
    name TEXT,
    photo TEXT,
    gender TEXT,
    languages TEXT  

)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS course_regist(
    id INTEGER,
    full_name TEXT,
    reason TEXT,
    branch TEXT,
    age INTEGER,
    gender TEXT    
)
""")
