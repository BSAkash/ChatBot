#!/bin/python3

import os
import sqlite3
from time import time

class Database:
    conn = None     # interactions connection
    cur = None
    conn2 = None    # corpus connection
    cur2 = None

    def initDB(self):
        if not os.path.exists('databases'):
            os.mkdir('databases')
        # connect to interactions database
        self.conn = sqlite3.connect('databases/interactions.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS bot_vars(name TEXT, value INT);''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS user_session(query TEXT, response TEXT, time INT);''')
        self.conn.commit()
        # connect to corpus database
        self.conn2 = sqlite3.connect('databases/corpus.db')
        self.cur2 = self.conn2.cursor()


    def addInteraction(self, query, response):
        self.cur.execute('''INSERT INTO user_session values (?, ?, ?);''', [query, response, int(time())])
        self.conn.commit()
    

    def getProfs(domain=None, course=None):
        if domain is None and course is None:
            cur2.execute('''SELECT professor FROM corpus;''')
        elif domain is None and course is not None:
            cur2.execute('''SELECT professor FROM corpus WHERE course=?;''', [course])
        elif domain is not None and course is None:
            cur2.execute('''SELECT professor FROM corpus WHERE domain=?;''', [domain])
        else: # both are given
            cur2.execute('''SELECT professor FROM corpus WHERE domain=? and course=?;''', [domain, course])
        return list(cur2.fetchall())
    
    def getDomains(prof=None, course=None):
        if domain is None and course is None:
            cur2.execute('''SELECT distinct(domain) FROM corpus;''')
        elif domain is None and course is not None:
            cur2.execute('''SELECT domain FROM corpus WHERE course=?;''', [course])
        elif domain is not None and course is None:
            cur2.execute('''SELECT domain FROM corpus WHERE professor=?;''', [prof])
        else: # both are given
            cur2.execute('''SELECT professor FROM corpus WHERE professor=? and course=?;''', [prof, course])
        return list(cur2.fetchall())
    
    def getCourses(prof=None, domain=None):
        if domain is None and course is None:
            cur2.execute('''SELECT course FROM corpus;''')
        elif domain is None and course is not None:
            cur2.execute('''SELECT course FROM corpus WHERE professor=?;''', [prof])
        elif domain is not None and course is None:
            cur2.execute('''SELECT course FROM corpus WHERE domain=?;''', [domain])
        else: # both are given
            cur2.execute('''SELECT professor FROM corpus WHERE domain=? and professor=?;''', [domain, prof])
        return list(cur2.fetchall())