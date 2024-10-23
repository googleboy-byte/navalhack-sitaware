import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('./localdb/contacts.db')
cursor = conn.cursor()

# SQL query to insert data
insert_query = '''
INSERT INTO contacts_basic (contact_type, contact_designator, contact_current_location,
                            contact_heading, contact_last_report_time, contact_speed,
                            contact_history, contact_meta, contact_status)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
'''


data = [
    # Previous entries (1-10)
    {
        "contact_type": "Patrol Vessel",
        "contact_designator": "PATROL VESSEL ALPHA",
        "contact_current_location": "13.250000, -71.500000",
        "contact_heading": "045°",
        "contact_last_report_time": "2024-10-20 14:30:00",
        "contact_speed": "12 knots",
        "contact_meta": "No suspicious activity.",
        "contact_status": "routine"
    },
    {
        "contact_type": "Coastal Station",
        "contact_designator": "COASTAL STATION BRAVO",
        "contact_current_location": "12.833333, -70.250000",
        "contact_heading": None,
        "contact_last_report_time": "2024-10-21 08:45:00",
        "contact_speed": None,
        "contact_meta": "Stationary.",
        "contact_status": "routine"
    },
    {
        "contact_type": "Aerial Patrol",
        "contact_designator": "AERIAL PATROL CHARLIE",
        "contact_current_location": "13.083333, -71.166667",
        "contact_heading": "270°",
        "contact_last_report_time": "2024-10-22 22:15:00",
        "contact_speed": "35 knots",
        "contact_meta": "Unidentified fast-moving craft.",
        "contact_status": "urgent"
    },
    {
        "contact_type": "Submarine",
        "contact_designator": "SUBMARINE DELTA",
        "contact_current_location": "12.666667, -70.916667",
        "contact_heading": None,
        "contact_last_report_time": "2024-10-23 11:00:00",
        "contact_speed": None,
        "contact_meta": "Large underwater contact detected.",
        "contact_status": "confidential"
    },
    {
        "contact_type": "Patrol Vessel",
        "contact_designator": "PATROL VESSEL ECHO",
        "contact_current_location": "13.500000, -71.750000",
        "contact_heading": None,
        "contact_last_report_time": "2024-10-24 16:20:00",
        "contact_speed": None,
        "contact_meta": "Advised to change course.",
        "contact_status": "routine"
    },
    {
        "contact_type": "Radar Station",
        "contact_designator": "RADAR STATION FOXTROT",
        "contact_current_location": None,
        "contact_heading": None,
        "contact_last_report_time": "2024-10-25 03:10:00",
        "contact_speed": None,
        "contact_meta": "Possible fishing fleet.",
        "contact_status": "routine"
    },
    {
        "contact_type": "Patrol Vessel",
        "contact_designator": "PATROL VESSEL GOLF",
        "contact_current_location": "12.500000, -70.666667",
        "contact_heading": "180°",
        "contact_last_report_time": "2024-10-26 19:55:00",
        "contact_speed": "8 knots",
        "contact_meta": "Routine transit.",
        "contact_status": "routine"
    },
    {
        "contact_type": "Coastal Station",
        "contact_designator": "COASTAL STATION HOTEL",
        "contact_current_location": None,
        "contact_heading": None,
        "contact_last_report_time": "2024-10-27 07:30:00",
        "contact_speed": None,
        "contact_meta": "No irregularities observed.",
        "contact_status": "routine"
    },
    {
        "contact_type": "Aerial Patrol",
        "contact_designator": "AERIAL PATROL INDIA",
        "contact_current_location": "13.333333, -71.250000",
        "contact_heading": None,
        "contact_last_report_time": "2024-10-28 13:40:00",
        "contact_speed": None,
        "contact_meta": "Oil slick detected.",
        "contact_status": "urgent"
    },
    {
        "contact_type": "Patrol Vessel",
        "contact_designator": "PATROL VESSEL JULIET",
        "contact_current_location": "12.916667, -70.500000",
        "contact_heading": "090°",
        "contact_last_report_time": "2024-10-29 05:05:00",
        "contact_speed": "6 knots",
        "contact_meta": "Investigating further.",
        "contact_status": "routine"
    },
    # New entries (11-20)
    {
        "contact_type": "Patrol",
        "contact_designator": "PATROL BOAT BRAVO",
        "contact_current_location": "13.750000, -71.383333",
        "contact_heading": "270°",
        "contact_last_report_time": "2024-10-24 16:45:00",
        "contact_speed": None,
        "contact_meta": "Request immediate air support for area search.",
        "contact_status": "urgent"
    },
    {
        "contact_type": "Coastal Station",
        "contact_designator": "COASTAL STATION ALPHA",
        "contact_current_location": "13.000000, -71.000000",
        "contact_heading": None,
        "contact_last_report_time": "2024-10-24 10:30:00",
        "contact_speed": None,
        "contact_meta": "Weather advisory: tropical storm approaching.",
        "contact_status": "routine"
    },
    {
        "contact_type": "Air Patrol",
        "contact_designator": "AIR PATROL CHARLIE",
        "contact_current_location": "12.500000, -70.750000",
        "contact_heading": "315°",
        "contact_last_report_time": "2024-10-24 15:45:00",
        "contact_speed": "20 knots",
        "contact_meta": "Spotted vessel matching description of wanted smuggling ship.",
        "contact_status": "immediate"
    },
    {
        "contact_type": "Submarine",
        "contact_designator": "SUBMARINE DELTA",
        "contact_current_location": "13.166667, -71.083333",
        "contact_heading": None,
        "contact_last_report_time": "2024-10-24 12:00:00",
        "contact_speed": None,
        "contact_meta": "Discovered uncharted seamount.",
        "contact_status": "confidential"
    },
    {
        "contact_type": "Port Authority",
        "contact_designator": "PORT AUTHORITY XAVIER",
        "contact_current_location": None,
        "contact_heading": None,
        "contact_last_report_time": "2024-10-24 14:00:00",
        "contact_speed": None,
        "contact_meta": "Port closure due to maintenance.",
        "contact_status": "routine"
    },
    {
        "contact_type": "Rescue Coordination",
        "contact_designator": "RESCUE COORDINATION CENTER",
        "contact_current_location": "12.916667, -70.666667",
        "contact_heading": None,
        "contact_last_report_time": "2024-10-24 18:30:00",
        "contact_speed": None,
        "contact_meta": "Distress call received from yacht.",
        "contact_status": "urgent"
    },
    {
        "contact_type": "Environmental Protection",
        "contact_designator": "ENVIRONMENTAL PROTECTION UNIT",
        "contact_current_location": "13.416667, -71.333333",
        "contact_heading": None,
        "contact_last_report_time": "2024-10-24 10:45:00",
        "contact_speed": None,
        "contact_meta": "Oil spill detected.",
        "contact_status": "immediate"
    },
    {
        "contact_type": "Fisheries Patrol",
        "contact_designator": "FISHERIES PATROL ECHO",
        "contact_current_location": "12.666667, -70.500000",
        "contact_heading": "045°",
        "contact_last_report_time": "2024-10-24 08:30:00",
        "contact_speed": "25 knots",
        "contact_meta": "Intercepted fishing vessel.",
        "contact_status": "urgent"
    },
    {
        "contact_type": "Naval Intelligence",
        "contact_designator": "NAVAL INTELLIGENCE FOXTROT",
        "contact_current_location": None,
        "contact_heading": None,
        "contact_last_report_time": "2024-10-24 12:00:00",
        "contact_speed": None,
        "contact_meta": "Possible hostile submarine activity.",
        "contact_status": "secret"
    },
    {
        "contact_type": "Lighthouse",
        "contact_designator": "LIGHTHOUSE KEEPER GULF",
        "contact_current_location": "13.083333, -70.333333",
        "contact_heading": None,
        "contact_last_report_time": "2024-10-24 16:00:00",
        "contact_speed": None,
        "contact_meta": "Lighthouse undergoing repairs.",
        "contact_status": "routine"
    },
]



# Insert each record into the database
for record in data:
    cursor.execute(insert_query, (
        record["contact_type"],
        record["contact_designator"],
        record["contact_current_location"],
        record["contact_heading"],
        record["contact_last_report_time"],
        record["contact_speed"],
        None,  # Assuming contact_history is not provided
        record["contact_meta"],
        record["contact_status"]
    ))

# Commit the changes and close the connection
conn.commit()
conn.close()
