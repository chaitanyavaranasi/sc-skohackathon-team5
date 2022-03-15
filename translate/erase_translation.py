# connect to cluster
import pymongo
client = pymongo.MongoClient("mongodb+srv://stephen:mongo@znaydit.padcu.mongodb.net/zynadit?retryWrites=true&w=majority")
db = client.zynadit
col = db.items


test = col.update_many(
        { },
        {"$set":
            {
                "translation.english":"null",
                "translation.polish":"null",
                "translation.russian":"null",
                "translation.german":"null",
                "translation.ukrainian":"null" 
            }
        })
print(test.modified_count)
