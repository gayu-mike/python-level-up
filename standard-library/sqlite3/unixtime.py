import datetime
import sqlite3
import time


def adapt_datetime(ts):
    return time.mktime(ts.timetuple())


sqlite3.register_adapter(datetime.datetime, adapt_datetime)

conn = sqlite3.connect(':memory:')
cur = conn.cursor()

now = datetime.datetime.now()
cur.execute('SELECT ?', (now,))
print(cur.fetchone()[0])
