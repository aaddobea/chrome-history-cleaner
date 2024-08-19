  ># INTRO
>> I was finding it difficult to clear my chrome browsing history the usual way. I tried on different days yet to no avail. I developed this python code to clear the browsing history and thankfully it worked. You can try this code and see if it works for you too. Remember to comment if it works.
 
# chrome-history-cleaner
This code is a Python script that clears the browsing history from Google Chrome's SQLite database. Here's a summary of the Code:

<details>
    <summary> 1. Imports </summary>
  <p> ⇥ sqlite3: To interact with the SQLite database used by Chrome.</p>
  <p> ⇥ shutil: To perform file operations, specifically for creating backups.</p>
  <p> ⇥ sys: This is imported but not used in this script. </p>
    </details>

<details>
    <summary> 2.  Function Definition </summary>
  <p> ⇥ clear_chrome_history(): The main function that performs the task of clearing the Chrome browsing history.</p>
  </details>
  
  <details>
    <summary> 3.  File Path Setup </summary>
    <p>  ⇥ The script defines the path to Chrome's history file using the os.path.expanduser("~") method to get the user's home directory.</p>
    <p>  ⇥ The full path to the history file is constructed assuming it is located at .../AppData/Local/Google/Chrome/User Data/Default/History.</p>
    </details>  

<details>
    <summary> 4.  Backup:</summary>
  <p> ⇥ clear_chrome_history(): A backup of the history file is created using shutil.copy2(), saving it as history.bak.</p>
  </details>

<details>
    <summary> 5. Database Connection:</summary>
  <p> ⇥ The script connects to the SQLite database located at the history path.</p>
  <p> ⇥ It creates a cursor for executing SQL commands.</p>
    </details>
    

<details>
    <summary> 6. Clearing History </summary>
  <p> ⇥ The script executes an SQL statement to delete all entries from the urls table, effectively clearing the browsing history. It then commits this change.</p>
  </details>

<details>
 <summary> 7. Error Handling </summary>
  <p> ⇥ If an OperationalError occurs (for example, if Chrome is running while this script tries to access the database), a message is printed prompting the user to close Chrome and try again.</p>
  </details>

<details>
    <summary> 8. Cleanup </summary>
  <p> ⇥ The database connection is closed in the finally block, ensuring it runs regardless of whether the operation was successful or encountered an error.</p>
  <p> ⇥  There is a commented-out line that suggests the option to delete the backup file if the operation is successful.</p>
    </details>

<details>
    <summary> 9. Main Execution </summary>
  <p> ⇥ The script runs the clear_chrome_history() function if it is executed as the main program.</p>
  </details>



# Conclusion:
This script automates the process of clearing Google Chrome's browsing history by directly accessing its SQLite database but includes a backup step to prevent data loss. Users should ensure Chrome is closed before execution to avoid operational errors.

