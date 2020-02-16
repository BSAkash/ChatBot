#!/usr/bin/env python

import os
import aiml

brain_file = "brain_files/brain.dump"

k = aiml.Kernel()

if os.path.exists(brain_file):
    print(f"Loading brain file: {brain_file}")
    k.loadBrain(brain_file)
else:
    k.bootstrap(learnFiles="learningFileList.aiml", commands="LEARN AIML")
    print("Saving brain file: " + brain_file)
    k.saveBrain(brain_file)
    print()

while True:
    reply = k.respond(input("User > "))
    if reply:
        print("bot > ", reply)
    else:
        print("bot > :) ", )