import sqlite3

conn = sqlite3.connect('./localdb/contacts.db')
cursor = conn.cursor()

def get_all_reports():
    all_recs = cursor.execute('SELECT * FROM contacts_basic')
    ret_recs = all_recs.fetchall()
    return ret_recs

def get_all_zones():
    all_zones = cursor.execute('SELECT * FROM zones_basic')
    ret_zones = all_zones.fetchall()
    return ret_zones