import sqlite3


conn = sqlite3.connect(':memory:')
conn.row_factory = sqlite3.Row

cur = conn.cursor()
# cur.execute('SELECT "John" as name, 42 as age')
cur.execute('select "john" as name')
for row in cur:
    # print(row[0], '==', row['name'])
    # print(row['name'], '==', row['NaMe'])
    # print(row[1], '==', row['age'])
    print(row['name'])
