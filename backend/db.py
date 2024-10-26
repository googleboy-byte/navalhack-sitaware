# database.py

import sqlite3

def create_database():
    """Create the SQLite database and necessary tables."""
    conn = sqlite3.connect('contact_data.db')

    conn.execute('''
    CREATE TABLE IF NOT EXISTS contacts_basic (
        contact_id INTEGER NOT NULL UNIQUE,
        contact_type TEXT,
        contact_designator TEXT,
        contact_current_location TEXT,
        contact_heading TEXT,
        contact_last_report_time TEXT,
        contact_speed TEXT,
        contact_history TEXT,
        contact_meta TEXT,
        contact_status TEXT,
        PRIMARY KEY(contact_id AUTOINCREMENT)
    )''')

    conn.execute('''
    CREATE TABLE IF NOT EXISTS zones_basic (
        zone_id INTEGER NOT NULL UNIQUE,
        name TEXT,
        type TEXT,
        description TEXT,
        coordinates_json TEXT,
        significance_level TEXT,
        PRIMARY KEY(zone_id AUTOINCREMENT)
    )''')

    conn.commit()
    conn.close()

def insert_into_contacts(conn, report):
    """Insert parsed report data into the contacts_basic table."""
    if report.get('alert') == 1:
        meta_str = "ALERT"
        
    contact_data = {
        'contact_type': report.get('location'),
        'contact_designator': report.get('vessel_name'),
        'contact_current_location': f"{report['coordinates']['latitude']}, {report['coordinates']['longitude']}",
        'contact_heading': report.get('heading'),
        'contact_last_report_time': report.get('time'),
        'contact_speed': report.get('speed'),
        'contact_history': 'None',  
        'contact_meta': f"{meta_str} {report.get('additional_info')}", 
        'contact_status': report.get("priority"),
    }
    # Check if the vessel name already exists in the database
    existing_record = conn.execute('''
        SELECT contact_current_location, contact_last_report_time 
        FROM contacts_basic 
        WHERE contact_designator = :contact_designator
    ''', {'contact_designator': contact_data['contact_designator']}).fetchone()

    # If a record exists, update the contact_history
    if existing_record:
        current_location, last_report_time = existing_record
        contact_data['contact_history'] = (current_location, last_report_time)
    else:
        contact_data['contact_history'] = 'None'

    # Insert the new record into the contacts_basic table
    conn.execute('''
    INSERT INTO contacts_basic (contact_type, contact_designator, contact_current_location,
                                contact_heading, contact_last_report_time, contact_speed, 
                                contact_history, contact_meta, contact_status)
    VALUES (:contact_type, :contact_designator, :contact_current_location, :contact_heading,
            :contact_last_report_time, :contact_speed, :contact_history, :contact_meta, :contact_status)
    ''', contact_data)

    # Commit the transaction
    conn.commit()