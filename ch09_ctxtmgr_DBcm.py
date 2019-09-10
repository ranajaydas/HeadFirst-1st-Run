"""The context manager for MySQL DB connections.

Not only is this code easier to read, we've also decoupled
all MySQL stuff into this file from the main program."""
import mysql.connector


class MySQLConnectionError(Exception):
    """Custom Exception for MySQL connection errors."""
    pass


class CredentialsError(Exception):
    """Custom Exception for MySQL credential errors."""
    pass


class SQLError(Exception):
    """Custom Exception for MySQL Programming errors in exit."""
    pass


class UseSQLDatabase:
    def __init__(self, config: dict) -> None:
        """Initializes using a configuration dictionary."""
        self.configuration = config

    def __enter__(self) -> 'cursor':
        """Connects to the MySQL database and returns a cursor."""
        try:
            self.conn = mysql.connector.connect(**self.configuration)  # ** unpacks the dictionary object
            self.cursor = self.conn.cursor()  # Creates a cursor for MySQL. Think of it as mysql>_ in cmd
            return self.cursor

        except mysql.connector.errors.InterfaceError as err:           # Catches any interface errors
            raise MySQLConnectionError(err)

        except mysql.connector.errors.ProgrammingError as err:         # Catches any credentials errors
            raise CredentialsError(err)

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Commits any inserts and closes the MySQL connection.

        Any error that happens within the 'with' statement, get
        handled in the __exit___ function."""
        self.conn.commit()   # Forcibly commits any inserts to the log
        self.cursor.close()  # Closes the cursor
        self.conn.close()    # Closes the connection to MySQL

        # Any exception handling code should be placed at the end
        if exc_type is mysql.connector.errors.ProgrammingError:
            raise SQLError(exc_val)
        elif exc_type:
            raise exc_type(exc_val)

