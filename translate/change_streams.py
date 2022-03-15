#!/usr/bin/env python3

import asyncio
import time
from python_settings import settings
import sys
import os
from pymongo import MongoClient
from threading import Thread
import pandas as pd
import googletrans
from googletrans import Translator


####
# Start script
####
print("==========================================")
print("    Change Stream Listener                ")
print("Resume functionality is a separate thread ")
print("==========================================")


####
# Main start function
# Start each individual thread for each event
# Sleep momentarily after starting each thread
####
def main():
    print('Starting Change Stream Listener.\n')

    # Create the insert thread
    insert_loop = asyncio.new_event_loop()
    insert_loop.call_soon_threadsafe(insert_change_stream)
    t = Thread(target=start_loop, args=(insert_loop,))
    t.start()
    time.sleep(0.25)


    # Create the resume example thread
    resume_loop = asyncio.new_event_loop()
    resume_loop.call_soon_threadsafe(resume_change_stream)
    t = Thread(target=start_loop, args=(resume_loop,))
    t.start()
    time.sleep(0.25)


####
# Make sure the loop continues
####
def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


####
# Insert Change Stream
####
def insert_change_stream():
    print("Insert listener thread started.")
    mongo_client = MongoClient(MONGODB_ATLAS_URL)
    db = mongo_client[DATABASE]
    coll = db[COLLECTION]

    # Change stream pipeline
    pipeline = [
        {'$match': {'operationType': 'insert'}}
    ]
#hackathon.py ###
    try:
    	for document in coll.watch(pipeline=pipeline, full_document='updateLookup'):
    		result = "=== INSERT EVENT ===\n"
    		print(result)

#################
    except KeyboardInterrupt:
        keyboard_shutdown()

####
# Resume capability implemented
####
def resume_change_stream():
    print("Resume listener thread started.")
    mongo_client = MongoClient(MONGODB_ATLAS_URL)
    db = mongo_client[DATABASE]
    accounts_collection = db[COLLECTION]

    pipeline = [
        {'$match': {'operationType': 'update'}},
        {'$match': {'fullDocument.accounts.type': 'checking'}},
        {'$match': {'fullDocument.accounts.balance': {'$gt': 100}}},
        {'$match': {'fullDocument.resumeCounter': {'$exists': True}}}
    ]

    # cursor to watch for specific updates
    cursor = accounts_collection.watch(pipeline=pipeline, full_document='updateLookup')
    # variable to indicate when to close change stream
    resume_counter = 0

    # loop thru docs in cursor
    try:
        for document in cursor:

            resume_token = document['_id']
            resume_counter = resume_counter + 1
            # check that the resumecounter field has been updated in document
            fulldoc_resume_counter_value = document['fullDocument']['resumeCounter']

            result = "\n=== RESUME EXAMPLE ===\n"
            result = result + "Resume token: " + str(resume_token) + "\n"
            result = result + "Counter value: " + str(fulldoc_resume_counter_value) + "\n"
            print(result)

            # once the resume_counter is greater than specified integer, sleep, close change stream, restart
            if resume_counter > 4:
                print("Resume Counter: " + str(resume_counter))
                print("Simulate failure for 10 seconds...")
                time.sleep(10)
                cursor.close
                print("Resume Change Stream closed.")
                print("Restart Change Stream with resume token: " + str(resume_token))
                # reset the cursor with resume token
                cursor = accounts_collection.watch(pipeline=pipeline,
                                                   full_document='updateLookup', resume_after=resume_token)
                # reset variables
                resume_counter = 0
                continue

    except KeyboardInterrupt:
        keyboard_shutdown()


###
# "Gracefully" consume output via ctrl-c
###
def keyboard_shutdown():
    print('Interrupted\n')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)


####
# Constants loaded from .env file
####
MONGODB_ATLAS_URL = "mongodb+srv://stephen:mongo@znaydit.padcu.mongodb.net/zynadit?retryWrites=true&w=majority"
DATABASE = "znaydit"
COLLECTION = "znaydit_data"

####
# Main
####
if __name__ == '__main__':
    main()
