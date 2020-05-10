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
        self.cur.execute("CREATE TABLE IF NOT EXISTS bot_vars(name TEXT, value INT);")
        self.cur.execute("CREATE TABLE IF NOT EXISTS user_session(query TEXT, response TEXT, time INT);")
        self.conn.commit()
        # connect to corpus database
        if not os.path.exists('databases/corpus.db'):
            print("ERROR: Missing file: databases/corpus.db")
        self.conn2 = sqlite3.connect('databases/corpus.db')
        self.cur2 = self.conn2.cursor()


    def addInteraction(self, query, response):
        self.cur.execute("INSERT INTO user_session values (?, ?, ?);", [query, response, int(time())])
        self.conn.commit()
    
    
    def listPopular(self):
        popular = ['Cloud Computing - Domain: Computer Science', 'Artificial Intelligence - Domain: Computer Science', 'Machine Learning - Domain: Computer Science', 'Biotechnology - Domain: Biology', 'Internet of Things - Domain: Phoenix']
        return '\n'.join(popular) + '\n'

    def getProfs(self, domain=None, course=None):
        if domain: domain = domain.lower().title()
        if course: course = course.lower().title()
        cur2 = self.cur2
        if domain is None and course is None:
            cur2.execute("SELECT DISTINCT professor FROM corpus;")
        elif domain is None and course is not None:
            cur2.execute("SELECT DISTINCT professor FROM corpus WHERE course=?;", [course])
        elif domain is not None and course is None:
            cur2.execute("SELECT DISTINCT professor FROM corpus WHERE domain=?;", [domain])
        else: # both are given
            cur2.execute("SELECT DISTINCT professor FROM corpus WHERE domain=? and course=?;", [domain, course])
        return list(cur2.fetchall())
    
    def getDomains(self, prof=None, course=None):
        if prof: prof = prof.lower().title()
        if course: course = course.lower().title()
        cur2 = self.cur2
        if prof is None and course is None:
            cur2.execute("SELECT distinct(domain) FROM corpus;")
        elif prof is None and course is not None:
            cur2.execute("SELECT domain FROM corpus WHERE course=?;", [course])
        elif prof is not None and course is None:
            cur2.execute("SELECT domain FROM corpus WHERE professor LIKE '%"+prof+"%';")
        else: # both are given
            cur2.execute("SELECT professor FROM corpus WHERE professor LIKE '%"+prof+"%' and course=?;", [course])
        return list(cur2.fetchall())
    
    def getCourses(self, prof=None, domain=None):
        if prof: prof = prof.lower().title()
        if domain: domain = domain.lower().title()
        cur2 = self.cur2
        if domain is None and prof is None:
            cur2.execute("SELECT course, professor FROM corpus;")
        elif domain is None and prof is not None:
            cur2.execute("SELECT course, professor FROM corpus WHERE professor LIKE '%"+prof+"%';")
        elif domain is not None and prof is None:
            cur2.execute("SELECT course, professor FROM corpus WHERE domain=?;", [domain])
        else: # both are given
            cur2.execute("SELECT course, professor FROM corpus WHERE domain=? and professor LIKE '%"+prof+"%';", [domain])
        return list(cur2.fetchall())
    
    def getAliases(self, domain):
        if domain: domain = domain.lower().title()
        cur2 = self.cur2
        cur2.execute("SELECT alias FROM aliases WHERE domain=?;",[domain])
        return cur2.fetchone()[0].split(',')

    def exists(self, item, value):
        value = value.lower().title()
        cur2 = self.cur2
        if item == 'professor':
            cur2.execute("SELECT professor FROM corpus WHERE professor LIKE'%"+value+"%';")
        else:
            cur2.execute("SELECT "+item+" FROM corpus WHERE "+item+"='"+value+"';")
        x = cur2.fetchall()
        if len(x) > 0: return True
        else: return False