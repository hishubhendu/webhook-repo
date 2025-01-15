from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')     #setting up mongoDB
db = client['mydatabase']                           
