import sqlite3

conn = sqlite3.connect('mars.db')

cursor = conn.cursor()

classmates = [
    (1, 'Muhammad', 14.5, "17T yoli", "+998 94 866 75 16"),
    (2, 'MIrshohid', 14.3, "17T yoli", "+998 94 866 75 16"),
    (3, 'dovron', 14.6, "17T yoli", "+998 94 866 75 16"),
    (4, 'Muhammdamin', 14.2, "17T yoli", "+998 94 866 75 16"),
    (5, 'egamberdi', 14.65, "17T yoli", "+998 94 866 75 16"),
    (6, 'said', 14.7, "17T yoli", "+998 94 866 75 16"),
    (7, 'saidalo', 14.8, "17T yoli", "+998 94 866 75 16"),
    (8, 'abdulloh', 14.9, "17T yoli", "+998 94 866 75 16"),
    (9, 'fazil', 14.4, "17T yoli", "+998 94 866 75 16"),
    (10, 'usmon', 14.1, "17T yoli", "+998 94 866 75 16"),

]

cursor.executemany("""
INSERT INTO classmates VALUES(?,?,?,?,?)
""", classmates)
my_IT_class = [
    (1, 'Sanjar ', 14.5, "17T yoli", "+998 94 866 75 16"),
    (2, 'Saidabbos', 14.3, "17T yoli", "+998 94 866 75 16"),
    (3, 'Abdulloh', 14.6, "17T yoli", "+998 94 866 75 16"),
    (4, 'Hasan', 14.2, "17T yoli", "+998 94 866 75 16"),
    (5, 'Bekzod', 14.97, "17T yoli", "+998 94 866 75 16"),
    (6, 'Botir', 14.7, "17T yoli", "+998 94 866 75 16"),
    (7, 'Samadbek', 14.8, "17T yoli", "+998 94 866 75 16"),
    (8, 'Ibrohim 2 ', 14.9, "17T yoli", "+998 94 866 75 16"),
    (9, 'bpshla;r', 14.4, "17T yoli", "+998 94 866 75 16"),
    (10, 'Ibrohim 1', 14.1, "17T yoli", "+998 94 866 75 16"),

]

cursor.executemany("""
INSERT INTO my_IT_class VALUES(?,?,?,?,?)
""", my_IT_class)


conn.commit()
conn.close()