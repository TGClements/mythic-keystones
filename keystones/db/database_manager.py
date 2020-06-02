import sqlite3
from sqlite3 import Error


class DatabaseManager:
    def __init__(self, directory='./'):
        """

        Initializes the DatabaseManager with a connection
        and Keystones table
        """
        if directory[-1] != '/':
            directory += '/'
        try:
            self.conn = sqlite3.connect(f'{directory}keystones.db')
            create_table_sql = '''
            CREATE TABLE IF NOT EXISTS Keystones (
            userID TEXT,
            characterName TEXT COLLATE NOCASE,
            dungeonID INT NOT NULL,
            level INT NOT NULL,
            currentTimeperiod INT NOT NULL,
            PRIMARY KEY (userID, characterName, currentTimeperiod)
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
        :return: (bool) True if the transaction was successful
        """
        sql_statement = '''
        INSERT OR REPLACE INTO Keystones(userID, characterName, dungeonID,
        level, currentTimeperiod)
        VALUES (?, ?, ?, ?, ?);
        '''
        try:
            cur = self.conn.cursor()
            cur.execute(sql_statement, insert_values)
            self.conn.commit()
        except Error as e:
            print(e)
            return False
        else:
            return True

    def get_keystones_single(self, user_id, current_timeperiod):
        """

        Gets the keystones for a single user

        A user can be associated with multiple keystones if they
        have multiple characters
        :param user_id: (str) the id for a user
        :return: list of tuples containing character name (str),
        dungeon id (integer), and level (integer)
        """
        where_inserts = (user_id, current_timeperiod)
        sql_statement = '''
        SELECT characterName, dungeonID, level
        FROM Keystones
        WHERE userID=? AND currentTimeperiod=?;
        '''
        try:
            cur = self.conn.cursor()
            cur.execute(sql_statement, where_inserts)
            return cur.fetchall()
        except Error as e:
            print(e)
            return None

    def get_keystones_many(self, user_ids, current_timeperiod):
        """

        Gets the keystones for multiple users

        A user can be associated with multiple keystones if they
        have multiple characters
        :param user_ids: (sequence of str) the user ids to get keys of
        :return: dictionary mapping user ids (str) to a list of tuples
        containing character name (str), dungeon id (integer), and
        level (integer)
        """
        query_result = {}
        sql_statement = '''
        SELECT characterName, dungeonID, level
        FROM Keystones
        WHERE userID=? AND currentTimeperiod=?;
        '''
        try:
            cur = self.conn.cursor()
            for user_id in user_ids:
                where_inserts = (user_id, current_timeperiod)
                cur.execute(sql_statement, where_inserts)
                query_result[user_id] = cur.fetchall()
        except Error as e:
            print(e)
            return None
        else:
            return query_result

    def close_connection(self):
        """

        Closes the database connection

        This method should only be used after being completely finished
        using the database (ie the program has stopped running).
        :return: (None)
        """
        try:
            self.conn.close()
        except Error as e:
            print(e)
