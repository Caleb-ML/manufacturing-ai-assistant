import sqlite3
import os

# The file path where our SQLite database will be saved
db_path = os.path.join(os.path.dirname(__file__), "..", "..", "data", "maintenance_logs.db")

def query_by_machine_id(machine_id):
    # Connect to the database file (creates the file if it doesn't exist yet)
    db_conn = sqlite3.connect(db_path)

    cursor = db_conn.cursor()

    cursor.execute("SELECT * FROM maintenance_logs WHERE machine_id = ?" ,(machine_id,))
    
    rows = cursor.fetchall() 
    
   
    

    # Save the changes and close the connection cleanly
    return rows
    db_conn.close()

    # Need 3 different fucntiosn mainly based on the input the user will type in either by machine id, error code or description
def query_by_error_code(error_code):
    # Connect to the database file (creates the file if it doesn't exist yet)
    db_conn = sqlite3.connect(db_path)

    cursor = db_conn.cursor()

    cursor.execute("SELECT * FROM maintenance_logs WHERE error_code = ?" ,(error_code,))
    
    rows = cursor.fetchall() 
       

    # query by fault descr. provided by user
    return rows
    db_conn.close()

def query_by_fault_descr(fault_descr):
    # Connect to the database file (creates the file if it doesn't exist yet)
    db_conn = sqlite3.connect(db_path)

    cursor = db_conn.cursor()

    cursor.execute("SELECT * FROM maintenance_logs WHERE fault_description LIKE ?" ,(f'%{fault_descr}%',))
    
    rows = cursor.fetchall() 
    
    
    
    # Save the changes and close the connection cleanly
    return rows
    db_conn.close()
if __name__ == "__main__":
    # checking if folder exists before running
    #os.makedirs("data", exist_ok=True)
    query_by_machine_id("M-03")

    query_by_error_code("E-14")
    query_by_fault_descr("pressure")


    
# python  query_db.py