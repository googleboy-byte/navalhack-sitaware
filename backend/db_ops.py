import sqlite3

conn = sqlite3.connect('./localdb/contacts.db')
cursor = conn.cursor()

def get_all_reports():
    all_recs = cursor.execute('SELECT * FROM contacts_basic')
    ret_recs = all_recs.fetchall()
    return ret_recs