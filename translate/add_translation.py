import sys, getopt
# read in user item input
try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
except getopt.GetoptError:
    print('check syntax script.py -i <inputfile> -o <outputfile>')
    sys.exit(2)
for opt, arg in opts:
  if opt in ("-i", "--in"):
    input_item = arg
  else:
    print("no item found")

# connect to cluster
import pymongo
client = pymongo.MongoClient("mongodb+srv://stephen:mongo@znaydit.padcu.mongodb.net/zynadit?retryWrites=true&w=majority")
db = client.zynadit
col = db.items
# print(col.find_one({"item.name":"blankets"}))
# print(col.find_one({"_id":"ObjectId('622fb5e0e2501451937c6a75')"}))

import pandas as pd
import googletrans
from googletrans import Translator

# translate
def transl(lang, word):
    if(lang=="en"):
        english = word
        #german = translator.translate(word, src='en', dest='de').text
        polish = translator.translate(word, src='en', dest='pl').text
        russian = translator.translate(word, src='en', dest='ru').text
        ukrainian = translator.translate(word, src='en', dest='uk').text
    elif(lang=="pl"):
        english = translator.translate(word, src='pl', dest='en').text
        # german = translator.translate(word, src='pl', dest='de').text
        polish = word
        russian = translator.translate(word, src='pl', dest='ru').text
        ukrainian = translator.translate(word, src='pl', dest='uk').text
    elif(lang=="ru"):
        english = translator.translate(word, src='ru', dest='en').text
        # german = translator.translate(word, src='ru', dest='de').text
        polish = translator.translate(word, src='ru', dest='pl').text
        russian = word
        ukrainian = translator.translate(word, src='ru', dest='uk').text
    elif(lang=="uk"):
        english = translator.translate(word, src='uk', dest='en').text
        # german = translator.translate(word, src='uk', dest='de').text
        polish = translator.translate(word, src='uk', dest='pl').text
        russian = translator.translate(word, src='uk', dest='ru').text
        ukrainian = word
    else:
        english = word
        # german = word
        polish = word
        russian = word
        ukrainian = word
        # print("language not found")
    #print(f"english:{english}\ngerman:{german}\npolish:{polish}\nrussian:{russian}\nukrainian:{ukrainian}")
    #print(f"english:{english}\tpolish:{polish}\trussian:{russian}\tukrainian:{ukrainian}")
    return english, polish, russian, ukrainian

# update collection
def update(inpu, engl, poli, russ, ukra):
    result = col.update_many(
        # *** remove .capitalize when coll is updated
            {   "item.name": inpu.capitalize() },
            { 
                "$set": { 
                    "translation.english":engl,
                    "translation.polish":poli,
                    "translation.russian":russ,
                    "translation.ukrainian":ukra 
                    }
            }
            )
    print(f"matches: {result.matched_count}\tmodified: {result.modified_count}")
    if result.modified_count>0:
        print(result.modified_count, "documents updated.")

# find all distinct items
allitems = col.distinct("item.name")
print(allitems)

flag = True
dictionary = {}

import json
# open existing json
filename = "dictionary.json"
with open(filename, 'w') as outfile:
            outfile.write('{"term":"translations"}')

with open(filename) as dict_json:
    dictionary = json.load(dict_json)
    print(dictionary)

while flag:
    docs = col.aggregate([
        {
            "$match":{
                "translated":{"$exists":False}
            }
        }
        ]
    )
    for doc in docs:
        input_item = doc["item"]["name"].lower()
        # if word exists in dictionary, update_many
        if input_item in dictionary:
            values = dictionary[input_item]
            update(input_item, values[0], values[1], values[2], values[3])
        else:
            translator = Translator()
            detected_lang = translator.detect(input_item).lang
            print(input_item + "\t" + detected_lang)
            eng, pol, rus, ukr = transl(detected_lang, input_item)
            print(f"english:{eng}\tpolish:{pol}\trussian:{rus}\tukrainian:{ukr}")
            arr = [eng, pol, rus, ukr]
            dictionary[input_item] = [eng, pol, rus, ukr]
            update(input_item, eng, pol, rus, ukr)
        for key, value in dictionary.items():
            print("###### " + key, ' : ', value)

        with open(filename, 'w') as fp:
            json.dump(dictionary, fp)
        # myquery = {"item.name": {"$eq" : input_item}}
        # new_values = {"$set":{
        #     "translation.english":eng,
        #     "translation.polish":pol,
        #     "translation.russian":rus,
        #     "translation.ukrainian":ukr
        #     }}

        # clear number of fields
        # test = col.update_many(
        # { },
        # {"$set":
        #     {
        #         "translation.english":"null",
        #         "translation.polish":"null",
        #         "translation.russian":"null",
        #         "translation.german":"null",
        #         "translation.ukrainian":"null" 
        #     }
        # })
        # print(test.modified_count)
        
