# ---------------------------------
# WARNING: This file will delete the contents
# of the Keystones table in keystones/db/keystones.db
#
# This should be run through a cron job before every reset
# Resets occur on Tuesdays at 15:00 UTC for American servers
#
# The crontab command should be:
# 0 15 * * 2 <path to python> <path to this file>
# ---------------------------------


import sqlite3
from sqlite3 import Error


def main():
    try:
        conn = sqlite3.connect('db/keystones.db')
        cur = conn.cursor()
        cur.execute('DELETE FROM Keystones;')
        conn.commit()
        print('Weekly reset complete. Entries deleted from Keystones table.')
    except Error as e:
        print(e)


if __name__ == '__main__':
    main()

