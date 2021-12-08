import sqlite3
import pandas as pd
import os
from mega import Mega
from datetime import datetime

def to_mega():
    email = os.environ.get('MEGA_USER')
    password = os.environ.get('MEGA_PASSWORD')
    mega = Mega()
    m = mega.login(email, password)
    db = sqlite3.connect('./development.sqlite3')
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table_name in tables:
        table_name = table_name[0]
        dest_filename = table_name + '_' + str(datetime.utcnow())
        mfile = m.upload('./' + table_name + '.csv', dest_filename=dest_filename)
        print(m.get_upload_link(mfile))
    cursor.close()
    db.close()

def to_csv():
    db = sqlite3.connect('./development.sqlite3')
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table_name in tables:
        table_name = table_name[0]
        table = pd.read_sql_query("SELECT * from %s" % table_name, db)
        table.to_csv(table_name + '.csv', index_label='index')
    cursor.close()
    db.close()

to_csv()
to_mega()
