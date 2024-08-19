import sqlite3
import os
import shutil
import sys

def clear_chrome_history():
    # Path to Chrome's history file
    user_data_path = os.path.expanduser("~") + "/AppData/Local/Google/Chrome/User Data"
    history_path = user_data_path + "/Default/History"

    # Backup the history file before modification
    backup_path = history_path + ".bak"
    shutil.copy2(history_path, backup_path)
    
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(history_path)
        cursor = conn.cursor()
        
        # Delete all entries from the history table
        cursor.execute("DELETE FROM urls;")
        conn.commit()
        
        print("Browsing history cleared successfully.")
    
    except sqlite3.OperationalError as e:
        print(f"Error: {e}")
        print("Chrome might be running. Please close Chrome and try again.")
    
    finally:
        # Close the database connection
        if conn:
            conn.close()
        
        # Optionally, you can delete the backup file if everything is fine
        # os.remove(backup_path)

if __name__ == "__main__":
    clear_chrome_history()
