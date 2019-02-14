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
            characterName TEXT COLLATE NOCASE,
            dungeonID INT NOT NULL,
            level INT NOT NULL,
            PRIMARY KEY (userID, characterName)
            );
            '''
            self.create_table(create_table_sql)
        except Error as e:
            print(e)

    def create_table(self, create_table_sql):
        """Creates a table within the current connection"""
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

    def get_keystones_single(self, user_id):
        """

        Gets the keystones for a single user

        A user can be associated with multiple keystones if they
        have multiple characters
        :param user_id: (str) the id for a user
        :return: list of tuples containing character name (str),
        dungeon id (integer), and level (integer)
        """
        id_tuple = (user_id,)  # Needs to be passed as a tuple
        sql_statement = '''
        SELECT characterName, dungeonID, level
        FROM Keystones
        WHERE userID=?;
        '''
        cur = self.conn.cursor()
        cur.execute(sql_statement, id_tuple)
        return cur.fetchall()

    def get_keystones_many(self, user_ids):
        """

        Gets the keystones for multiple users

        A user can be associated with multiple keystones if they
        have multiple characters
        :param user_ids: (list of str) the user ids to get keys of
        :return: dictionary mapping user ids (str) to a list of tuples
        containing character name (str), dungeon id (integer), and
        level (integer)
        """
        query_result = {}
        sql_statement = '''
        SELECT characterName, dungeonID, level
        FROM Keystones
        WHERE userID=?;
        '''
        cur = self.conn.cursor()
        for user_id in user_ids:
            id_tuple = (user_id,)
            cur.execute(sql_statement, id_tuple)
            query_result[user_id] = cur.fetchall()
        return query_result

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
    # db_manager.delete_all_keystones()
    db_manager.add_keystone(('123456', 'hovsep', 35, 10))
    db_manager.add_keystone(('123456', 'hop', 890, 1))
    db_manager.add_keystone(('123456', 'hosep', 5, 180))
    db_manager.add_keystone(('567', 'jon', 7, 100))
    db_manager.add_keystone(('567', '', 7, 100))
    db_manager.add_keystone(('567', 'jak', 7, 100))
    db_manager.add_keystone(('567', 'jaK', 8, 99))
    print(db_manager.get_keystones_many(['123456', '567']))


if __name__ == '__main__':
    main()
