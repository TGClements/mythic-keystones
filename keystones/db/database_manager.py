import sqlite3
from sqlite3 import Error


class DatabaseManager:
    def __init__(self):
        """

        Initializes the DatabaseManager with a connection
        and Keystones table
        """
        try:
            self.conn = sqlite3.connect('.\keystones.db')
            create_table_sql = '''
            CREATE TABLE IF NOT EXISTS Keystones (
            userID TEXT,
            characterName TEXT,
            dungeonID INT NOT NULL,
            level INT NOT NULL,
            PRIMARY KEY (userID, characterName)
            );
            '''
            self.create_table(create_table_sql)
        except Error as e:
            print(e)

    def create_table(self, create_table_sql):
        """

        Creates a table within the current connection
        :param create_table_sql: The SQL command to be executed
        :return: (None)
        """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def add_keystone(self, insert_values):
        """

        Inserts or updates a row in the Keystones table

        This method insert a row into the Keystones table. If a row
        already exists with the passed userID and characterName, then
        that row will be updated instead.
        :param insert_values: (tuple) a tuple containing the userID,
        characterName, dungeonID, and level to be added (in that order)
        :return: (None)
        """
        sql_statement = '''
        INSERT OR REPLACE INTO Keystones(userID, characterName, dungeonID, 
        level)
        VALUES (?, ?, ?, ?);
        '''
        try:
            cur = self.conn.cursor()
            cur.execute(sql_statement, insert_values)
            self.conn.commit()
        except Error as e:
            print(e)

    def delete_all_keystones(self):
        """

        Deletes all rows from the Keystones table

        Needless to say, but calling this when you don't want to
        is very problematic and will lose all data in the table.
        This is meant for the weekly resets.
        :return: (None)
        """
        sql_statement = '''DELETE FROM Keystones;'''
        try:
            cur = self.conn.cursor()
            cur.execute(sql_statement)
            self.conn.commit()
        except Error as e:
            print(e)

    def close_connection(self):
        """

        Closes the database connection

        This method should only be used after being completely finished
        using the database (ie the program has stopped running).
        :return: (None)
        """
        self.conn.close()


def main():
    db_manager = DatabaseManager()
    db_manager.add_key(('123456', 'hovsep', 35, 10))


if __name__ == '__main__':
    main()
