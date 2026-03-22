import sqlite3
import os

# The file path where our SQLite database will be saved
db_path = os.path.join("..", "..", "data", "maintenance_logs.db")

def create_db():
    # Connect to the database file (creates the file if it doesn't exist yet)
    db_conn = sqlite3.connect(db_path)

    # A cursor lets us send SQL commands to the database
    cursor = db_conn.cursor()

    # Create the maintenance_logs table if it isn't already there.
    # Each row represents one maintenance event logged by a technician.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS maintenance_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT, -- unique number for each log entry
            machine_id TEXT NOT NULL,             -- which machine had the problem
            error_code TEXT NOT NULL,             -- the error code shown on the machine
            fault_description TEXT NOT NULL,      -- plain description of what went wrong
            root_cause TEXT NOT NULL,             -- why it went wrong
            repair_action TEXT NOT NULL,          -- what was done to fix it
            technician TEXT NOT NULL,             -- who did the repair
            date TEXT NOT NULL,                   -- when the repair happened
            downtime_minutes INTEGER NOT NULL     -- how long the machine was offline
        )
    """)

    # Save the changes and close the connection cleanly
    db_conn.commit()
    db_conn.close()

if __name__ == "__main__":
    # checking if folder exists before running
    os.makedirs("data", exist_ok=True)
    create_db()
    print(f"Database created successfully in {db_path}")
