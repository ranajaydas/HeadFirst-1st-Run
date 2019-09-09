"""The context manager for MySQL DB connections."""
import mysql.connector


class UseSQLDatabase:
    def __init__(self, config: dict) -> None:
        """Initializes using a configuration dictionary."""
        self.configuration = config

    def __enter__(self) -> 'cursor':
        """Connects to the MySQL database and returns a cursor."""
        self.conn = mysql.connector.connect(**self.configuration)  # ** unpacks the dictionary object
        self.cursor = self.conn.cursor()  # Creates a cursor for MySQL. Think of it as mysql>_ in cmd
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Commits any inserts and closes the MySQL connection."""
        self.conn.commit()   # Forcibly commits any inserts to the log
        self.cursor.close()  # Closes the cursor
        self.conn.close()    # Closes the connection to MySQL

