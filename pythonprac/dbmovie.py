from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.sis7sux.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

db.moives.update_one({'title':'가버나움'},{'$set':{'star':'0'}})

