
#pip install pymongo==3.4.0
#python2


import sys
import pymongo
from pymongo import MongoClient
client = MongoClient()

client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://localhost:27017')


db = client.test
#dictionary style
#db = client['pymongo_test']

posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is module',
    'author': 'cns'
}
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))


bills_post = posts.find_one({'author': 'cns'})
print(bills_post)

# exit the program
sys.exit()



------------------

