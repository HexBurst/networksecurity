
from pymongo import MongoClient

uri = "mongodb+srv://anirudhsingh972005_db_user:Alpha1236@cluster0.1k2hqza.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)