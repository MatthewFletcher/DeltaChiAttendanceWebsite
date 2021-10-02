import sqlite
import time
import re 
import logging

MASTER_DB = "MASTER.DB"

class AttendanceWizard:
    #TODO Make this a singleton
    _instance = None

    def __init__(self,DB_FILENAME):
        #Regex to strip all non-text data
        self.regex = re.compile('[^a-zA-Z]')
        self.TABLE_NAME = 'ATTENDEES'

        self.con =   sqlite3.connect(DB_FILENAME)
        self.cur = con.cursor()
        cur.execute(f'''CREATE TABLE {self.TABLE_NAME}(
        ID INT PRIMARY KEY NOT NULL,
        INT TIMESTAMP NOT NULL,
        SECRET TEXT NOT NULL,
        );'''
        )

    def sanitizeName(self,last,first):
        '''
        Strips all non-alphabetical characters from names
        Returns a tuple (lastname:str, firstname:str)
        '''
        return (regex.sub('',name).title() for name in (last,first)) 

    def prepAndAddStatement(self, identifier, secret):
        #Get unix timestamp of login time
        timestamp = int(time.time())
        toInsert = f"INSERT INTO {self.TABLE_NAME} VALUES('{identifier}, {timestamp}, {secret}')" 
        logging.debug(f"Command value: >{toInsert}<")
        self.cur.execute(toInsert) 

