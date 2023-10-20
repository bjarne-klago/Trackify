from databaseService import DatabaseService
from trackifyAPI import app
import threading

def run_app():
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("Das App-Thread wurde durch Strg+C beendet.")

def run_database_service(db_file_name):
    try:
        DatabaseService(db_file_name).run()
    except KeyboardInterrupt:
        print("Das Database-Service-Thread wurde durch Strg+C beendet.")

if __name__ == '__main__':
    db_file_name = "trackify_db.sqlite3"
    
    app_thread = threading.Thread(target=run_app)
    db_thread = threading.Thread(target=run_database_service, args=(db_file_name,))

    app_thread.start()
    db_thread.start()

    try:
        app_thread.join()
        db_thread.join()
    except KeyboardInterrupt:
        print("Das Hauptprogramm wurde durch Strg+C beendet.")


# Um Website im netzwerk sichtbar zu machen:
# - zu E:\Trackify\website navigieren
# - python -m http.server ausführen
# - Website ist nun unter http://192.168.2.108:8000 verfügbar
