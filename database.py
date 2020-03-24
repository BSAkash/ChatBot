#!/bin/python3

import sqlite3
from time import time

class Database:
    conn = None
    cur = None

    def initDB(self):
        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS bot_vars(name TEXT, value INT);''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS user_session(query TEXT, response TEXT, time INT);''')
        self.conn.commit()


    def addToDB(self, query, response):
        self.cur.execute('''INSERT INTO user_session values (?, ?, ?);''', [query, response, int(time())])
        self.conn.commit()