import sqlite3


# Connection Obj
conn = sqlite3.connect('example.db')

# Cursor Obj
cursor = conn.cursor()

# execute / commit / close
# cursor.execute("""
#     CREATE TABLE
#         stocks(
#             `date`      text,
#             `trans`     text,
#             `symbol`    text,
#             `qty`       real,
#             `price`     real
#         )
# """)
# cursor.execute("""
#     INSERT INTO
#         stocks
#     VALUES
#         ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)
# """)
# conn.commit()
conn.close()

# format
t = ('RHAT')
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute("""
    SELECT
        *
    FROM
        stocks
    WHERE
        symbol = ?
""", (t,))
print(cursor.fetchall())

# A cursor is not refetchable
sql_select = """
    SELECT
        *
    FROM
        stocks
    WHERE
        symbol = ?
"""
cursor.execute(sql_select, (t,))
print(cursor.fetchone())

purchases = [
    ('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
    ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
    ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
]
cursor.executemany('INSERT INTO stocks VALUES (?, ?, ?, ?, ?)', purchases)
conn.commit()

for row in cursor.execute('SELECT * FROM stocks'):
    print(row)

