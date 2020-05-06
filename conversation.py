#!/bin/python3

import os
import re
import aiml
from apis import quotes
from apis import dictionary
from database import Database

k = None
d = None
domain = None
prof = None

def initBrain():
    if 'conversation.py' not in os.listdir():
        os.chdir("/home/rikilg/mysite/")
    if not os.path.exists('brain_files'):
        os.mkdir('brain_files')
    brain_file = "brain_files/brain.dump"

    global k
    k = aiml.Kernel()

    # if os.path.exists(brain_file):
    #     print("Loading brain file: " + brain_file)
    #     k.loadBrain(brain_file)
    #     return
    # else:
    k.bootstrap(learnFiles="learningFileList.aiml", commands="LEARN AIML")
    print("Saving brain file: " + brain_file)
    k.saveBrain(brain_file)


def suggestCourse(query):
    global prof
    global domain
    if len(query) > 2:
        query[1] = ' '.join(query[1:])
    if query[0] == 'professor':
        query[1] = query[1].replace('.', ' ')
        if not d.exists(query[0], query[1]):
            return "NO PROF IN DB"
        prof = query[1]
        return "PROF IN DB"
    elif query[0] == 'domain':
        if not d.exists(query[0], query[1]):
            return "NO DOMAIN IN DB" # will be taken care by AIML
        domain = query[1]
        return ""
    elif query[0] == 'done':
        if prof is not None or domain is not None:
            course = d.getCourses(prof, domain)
            return course[0][0] + ". "
    elif query[0] == 'list-courses-domain':
        l = d.getCourses(domain=domain)
        return '- ' + '\n- '.join([ x[0] for x in l ]) + "\n"
    elif query[0] == 'list-courses-prof':
        l = d.getCourses(prof=prof)
        return '- ' + '\n- '.join([ x[0] for x in l ]) + "\n"
    elif query[0] == 'list-all':
        l = d.getCourses()
        return '- ' + '\n- '.join([ x[0] for x in l ]) + "\n"
    elif query[0] == 'list-profs-domain':
        l = d.getProfs(domain=domain)
        return '- ' + '\n- '.join([ x[0] for x in l ]) + "\n"
    elif query[0] == "list-all-domains":
        l = d.getDomains()
        return '- ' + '\n- '.join([ x[0] for x in l ]) + "\n"
    

def botAnswer(query):
    global k
    global d
    if d is None:
        d = Database()
        d.initDB()
    if k is None:
        initBrain()
    response = k.respond(query)
    if response is None or response == "": response = "I'm don't yet understand your query! I am programmed to assist you in your course selection. Type 'help' to know more." # custom response
    d.addInteraction(query, response)
    m = re.match('/\{(.*)\}(.*)', response)
    if m is None: # no command found
        return response
    # else: # command found
    command = m.groups()[0].strip().split()
    response = m.groups()[1].strip()

    if command[0] == 'define':
        if len(command) < 2: return "Define *what*?"
        return dictionary.define(command[1])
    elif command[0] == 'quote':
        return quotes.getQuote()
    elif command[0] == 'corpus':
        dbResponse = suggestCourse(command[1:])
        if dbResponse == "NO PROF IN DB":
            return botAnswer("TRY PROFESSOR AGAIN")
        elif dbResponse == "PROF IN DB":
            return botAnswer("EVAL INTEREST")
        return dbResponse + response
    elif command[0] == 'popular':
        return d.listPopular() + response

    return "Looks like a command i'm not sure of!"


def main():
    global k
    try:
        while True:
            reply = botAnswer(input("USER > "))
            if 'bye' in reply:
                print('BOT > ', reply)
                return;
            print("BOT > ", reply)
    except KeyboardInterrupt:
        print("\rUser Exit signal encountered. exiting...")


if __name__ == "__main__":
    initBrain()
    main()