import eel
import db_ops

eel.init('../frontend')

@eel.expose
def fetch_all():
    all_recs = db_ops.get_all_reports()
    return all_recs

eel.start('map.html', size=(1200, 900), port=8001)