import json
from pymongo import MongoClient
from bson.json_util import dumps

from notify import *

client = MongoClient('mongodb://bae:bae@34.228.79.24:27017/bae_chat')
db = client.bae_chat

cur = db.kp_paid_tickets.find({'order_status': 'Success'},{'billing_email': 1})

email_list = json.loads(dumps(cur))
# email_list = email_list.split(',')

print len(email_list)

counter = 0

for x in email_list:
	promoEmail(x['billing_email'])
	print counter
	counter = counter + 1