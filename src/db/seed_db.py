import sqlite3
import os

db_path = os.path.join("data","maintenance_logs.db")
# Function to populate db with sample maintenance records with new db
def seed_data():
    db_conn = sqlite3.connect(db_path)

    cursor = db_conn.cursor()
# check teh data columns first to see how to populate the db
    sample_logs = [
        ("M-01", "E-47", "Injection pressure drop", "Worn hydraulic seal", "Replaced hydraulic seal on unit 3", "J.Smith", "2024-01-15", 90),
        ("M-02", "E-12", "Barrel temperature instability", "Faulty thermocouple", "Replaced thermocouple on zone 2", "A.Jones", "2024-01-22", 45),
        ("M-03", "E-33", "Mould not closing fully", "Debris in tie bar", "Cleaned tie bars and re-lubricated", "T.Brown", "2024-02-18", 60),
        ("M-04", "E-19", "Screw not rotating", "Burnt drive motor", "Replaced screw drive motor", "A.Jones", "2024-03-05", 200),
        ("M-05", "E-55", "Short shot defect", "Material viscosity too high", "Adjusted melt temperature and injection speed", "J.Smith", "2024-03-12", 75),
        ("M-01", "E-21", "Flash on moulded part", "Excessive injection pressure", "Reduced injection pressure and checked clamp force", "T.Brown", "2024-03-20", 30),
        ("M-02", "E-09", "Hopper dryer alarm", "Blocked air filter", "Cleaned and replaced hopper dryer filter", "A.Jones", "2024-04-02", 25),
        ("M-03", "E-61", "Ejector pin stuck", "Bent ejector pin", "Replaced ejector pin and realigned plate", "J.Smith", "2024-04-15", 80),
        ("M-04", "E-38", "Oil temperature warning", "Cooling fan failure on hydraulic unit", "Replaced hydraulic unit cooling fan", "T.Brown", "2024-04-28", 110),
        ("M-05", "E-14", "Nozzle drool detected", "Nozzle temperature too high", "Reduced nozzle temp and adjusted decompression", "A.Jones", "2024-05-10", 35),
    ]
    # Insert all sample records into the maintenance_logs table with placeholders
    cursor.executemany("""
        INSERT INTO maintenance_logs (
            machine_id, error_code, fault_description,
            root_cause, repair_action, technician,
            date, downtime_minutes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?) 
    """, sample_logs)
    db_conn.commit()
    db_conn.close()
    print("Data successfully added!")

if __name__ == "__main__":
    seed_data()

