import sqlite3
import json

# Connect to the SQLite database
conn = sqlite3.connect('./localdb/contacts.db')  # Change to your database name
cursor = conn.cursor()

# Your data to insert
zones_data = [
    {
        "name": "Lakshadweep Islands Maritime Surveillance Triangle",
        "type": "Remote Island Chain Monitoring Area",
        "description": "Comprehensive surveillance of Lakshadweep archipelago",
        "coordinates_json": json.dumps([[8.0, 71.0], [8.0, 74.0], [12.0, 74.0], [12.0, 71.0]]),
        "significance_level": 4
    },
    {
        "name": "Gulf of Khambhat Tidal Energy Security Zone",
        "type": "Renewable Energy Infrastructure Protection Area",
        "description": "Security for tidal power projects and related installations",
        "coordinates_json": json.dumps([[21.0, 72.0], [21.0, 73.0], [22.0, 73.0], [22.0, 72.0]]),
        "significance_level": 3
    },
    {
        "name": "Andaman Sea Exclusive Economic Zone Patrol Sector",
        "type": "Extended Maritime Jurisdiction Area",
        "description": "Enforcement of EEZ rights and resource protection",
        "coordinates_json": json.dumps([[6.0, 91.0], [6.0, 95.0], [14.0, 95.0], [14.0, 91.0]]),
        "significance_level": 4
    },
    {
        "name": "Kochi-Mangalore Offshore Wind Farm Security Corridor",
        "type": "Renewable Energy Asset Protection Zone",
        "description": "Security for offshore wind installations along southwest coast",
        "coordinates_json": json.dumps([[9.5, 75.0], [9.5, 76.0], [13.0, 76.0], [13.0, 75.0]]),
        "significance_level": 3
    },
    {
        "name": "Gopalpur-Puri Integrated Coastal Defense Network",
        "type": "Multi-Layer Coastal Security Zone",
        "description": "Coordinated coastal surveillance and defense operations",
        "coordinates_json": json.dumps([[19.0, 84.5], [19.0, 86.5], [20.0, 86.5], [20.0, 84.5]]),
        "significance_level": 4
    },
    {
        "name": "Saurashtra Peninsula Anti-Trafficking Patrol Zone",
        "type": "Counter-Smuggling Operations Area",
        "description": "Prevention of drug trafficking and contraband smuggling",
        "coordinates_json": json.dumps([[20.5, 69.0], [20.5, 72.0], [23.0, 72.0], [23.0, 69.0]]),
        "significance_level": 5
    },
    {
        "name": "Kavatti Island Forward Operating Base",
        "type": "Remote Naval Outpost",
        "description": "Extended range patrols and surveillance in southern Lakshadweep",
        "coordinates_json": json.dumps([[10.5, 72.5], [10.5, 73.0], [11.0, 73.0], [11.0, 72.5]]),
        "significance_level": 3
    },
    {
        "name": "Vizag-Gangavaram Port Complex Security Zone",
        "type": "Multi-Port Maritime Security Area",
        "description": "Integrated security for adjacent major ports",
        "coordinates_json": json.dumps([[17.5, 83.0], [17.5, 83.5], [18.0, 83.5], [18.0, 83.0]]),
        "significance_level": 4
    },
    {
        "name": "Netrani Island Live Fire Exercise Zone",
        "type": "Naval Gunnery Range",
        "description": "Offshore area for naval artillery and missile testing",
        "coordinates_json": json.dumps([[14.0, 74.0], [14.0, 74.5], [14.5, 74.5], [14.5, 74.0]]),
        "significance_level": 3
    },
    {
        "name": "Andaman Nicobar Command Joint Forces Training Area",
        "type": "Tri-Service Exercise Zone",
        "description": "Combined operations training for navy, army, and air force",
        "coordinates_json": json.dumps([[11.5, 92.0], [11.5, 93.0], [13.0, 93.0], [13.0, 92.0]]),
        "significance_level": 4
    },
    {
        "name": "Kanyakumari-Tuticorin Coastal Security Corridor",
        "type": "Integrated Maritime Border Surveillance Zone",
        "description": "Monitoring of southern tip of Indian peninsula",
        "coordinates_json": json.dumps([[8.0, 77.5], [8.0, 78.5], [9.0, 78.5], [9.0, 77.5]]),
        "significance_level": 3
    },
    {
        "name": "Porbandar-Okha Offshore Patrol Vessel Operating Area",
        "type": "Coast Guard Patrol Zone",
        "description": "Regular patrols to combat illegal fishing and smuggling",
        "coordinates_json": json.dumps([[21.5, 68.5], [21.5, 70.0], [23.0, 70.0], [23.0, 68.5]]),
        "significance_level": 5
    },
    {
        "name": "Kavaratti Underwater Domain Awareness Center",
        "type": "Submarine Detection and Tracking Zone",
        "description": "Monitoring subsurface activities in central Arabian Sea",
        "coordinates_json": json.dumps([[9.5, 71.5], [9.5, 73.0], [11.0, 73.0], [11.0, 71.5]]),
        "significance_level": 4
    },
    {
        "name": "Paradip-Haldia Offshore Security Zone",
        "type": "Critical Maritime Infrastructure Protection Area",
        "description": "Security for offshore oil rigs and pipelines",
        "coordinates_json": json.dumps([[20.5, 87.0], [20.5, 88.5], [22.0, 88.5], [22.0, 87.0]]),
        "significance_level": 5
    },
    {
        "name": "Little Andaman Island Forward Operating Base",
        "type": "Southern Naval Outpost",
        "description": "Extended range operations in southern Bay of Bengal",
        "coordinates_json": json.dumps([[10.0, 92.0], [10.0, 93.0], [11.0, 93.0], [11.0, 92.0]]),
        "significance_level": 3
    },
    {
        "name": "Sundarbans Riverine Patrol Network",
        "type": "Mangrove Forest Maritime Security Zone",
        "description": "Anti-smuggling and environmental protection operations",
        "coordinates_json": json.dumps([[21.5, 88.5], [21.5, 89.5], [22.5, 89.5], [22.5, 88.5]]),
        "significance_level": 4
    },
    {
        "name": "Karwar Underwater Ranges and Measurement Facility",
        "type": "Submarine and Torpedo Testing Area",
        "description": "Calibration and performance testing of submarine systems",
        "coordinates_json": json.dumps([[14.5, 73.5], [14.5, 74.0], [15.0, 74.0], [15.0, 73.5]]),
        "significance_level": 4
    },
    {
        "name": "Kalpeni-Minicoy Islands Maritime Patrol Sector",
        "type": "Inter-Island Security Corridor",
        "description": "Monitoring of sea lanes between southern Lakshadweep islands",
        "coordinates_json": json.dumps([[8.0, 72.5], [8.0, 74.0], [10.0, 74.0], [10.0, 72.5]]),
        "significance_level": 4
    },
    {
        "name": "Chilika Lake Naval Test Facility",
        "type": "Naval Systems Evaluation Zone",
        "description": "Testing of naval equipment in brackish water conditions",
        "coordinates_json": json.dumps([[19.5, 85.0], [19.5, 85.5], [20.0, 85.5], [20.0, 85.0]]),
        "significance_level": 3
    },
    {
        "name": "Lakshadweep Sea Extended Anti-Piracy Patrol Zone",
        "type": "Far Sea Counter-Piracy Operations Area",
        "description": "Anti-piracy measures in high-risk maritime areas",
        "coordinates_json": json.dumps([[9.0, 70.0], [9.0, 73.0], [11.0, 73.0], [11.0, 70.0]]),
        "significance_level": 5
    },
    {
        "name": "Kochi Naval Base Security Operations Zone",
        "type": "Military Asset Protection Area",
        "description": "Security operations around major naval installations",
        "coordinates_json": json.dumps([[9.9, 76.2], [9.9, 76.5], [10.1, 76.5], [10.1, 76.2]]),
        "significance_level": 5
    },
    {
        "name": "Cape Comorin Environmental Protection Zone",
        "type": "Coastal and Marine Ecosystem Security Area",
        "description": "Protection of sensitive coastal and marine ecosystems",
        "coordinates_json": json.dumps([[8.0, 77.0], [8.0, 78.0], [9.0, 78.0], [9.0, 77.0]]),
        "significance_level": 4
    },
    {
        "name": "Rameswaram-Lanka Maritime Border Security Area",
        "type": "Cross-Border Surveillance Zone",
        "description": "Monitoring of maritime borders with Sri Lanka",
        "coordinates_json": json.dumps([[9.0, 79.0], [9.0, 80.0], [10.0, 80.0], [10.0, 79.0]]),
        "significance_level": 5
    },
    {
        "name": "Coromandel Coast Monitoring Area",
        "type": "Maritime Safety and Security Zone",
        "description": "Surveillance and safety operations along Coromandel Coast",
        "coordinates_json": json.dumps([[12.0, 80.0], [12.0, 81.0], [14.0, 81.0], [14.0, 80.0]]),
        "significance_level": 4
    }
]

# Insert data into the zones_basic table
for zone in zones_data:
    cursor.execute('''
        INSERT INTO zones_basic (name, type, description, coordinates_json, significance_level)
        VALUES (?, ?, ?, ?, ?)
    ''', (zone['name'], zone['type'], zone['description'], zone['coordinates_json'], zone['significance_level']))

# Commit the changes and close the connection
conn.commit()
conn.close()
