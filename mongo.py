import pymongo
client = pymongo.MongoClient("mongodb+srv://gurpreet:gurpreet@cluster0.zc1iw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db  = client["mydatabase"]
mycol = db["customers"]
mydict = {"first": "gurpret", "last" : "dhaliwal"}
mycol.insert_one(mydict)
