import sqlite3
import os

# The file path where our SQLite database will be saved
db_path = os.path.join("..", "..", "data", "maintenance_logs.db")

def display_db():
    # Connect to the database file (creates the file if it doesn't exist yet)
    db_conn = sqlite3.connect(db_path)

    cursor = db_conn.cursor()

    cursor.execute("SELECT * FROM maintenance_logs")
    
    rows = cursor.fetchall() 
    print([description[0] for description in cursor.description])    
    for display in rows:
        print(display)
    # Print column headers from the cursor description
    print([description[0] for description in cursor.description])

    # Save the changes and close the connection cleanly
    db_conn.close()

if __name__ == "__main__":
    # checking if folder exists before running
    #os.makedirs("data", exist_ok=True)
    display_db()
    
# python display_db.py