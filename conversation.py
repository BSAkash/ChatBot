#!/bin/python3

import os
import aiml

k = None

def initBrain():
    os.chdir("/home/rikilg/mysite/")
    brain_file = "brain_files/brain.dump"

    global k
    k = aiml.Kernel()

    if os.path.exists(brain_file):
        print("Loading brain file: " + brain_file)
        k.loadBrain(brain_file)
    else:
        k.bootstrap(learnFiles="learningFileList.aiml", commands="LEARN AIML")
        print("Saving brain file: " + brain_file)
        k.saveBrain(brain_file)


def botAnswer(query):
    global k
    if k is None:
        initBrain()
    return k.respond(query)


def main():
    global k
    while True:
        reply = botAnswer(input("BOT > "))
        if reply:
            print("BOT > ", reply)
        else:
            print("BOT > :) ", )


if __name__ == "__main__":
    initBrain()
    main()