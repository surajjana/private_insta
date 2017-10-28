#!/usr/bin/python

from ccavutil import encrypt,decrypt
from string import Template
from pymongo import MongoClient
from bson.json_util import dumps
import json
import pymongo


# client = MongoClient('mongodb://su:su@52.37.155.102:27017/kp_events')
# # client = MongoClient()
# db = client.kp_events


def res(encResp):
	'''
	Please put in the 32 bit alphanumeric key in quotes provided by CCAvenues.
	'''	 
	# workingKey = '7D9D1B56365DC282F2F83E8B1C9D4A04'
	workingKey = 'DEDE391379CF9113C0DE2ADF7DA7C235'
	decResp = decrypt(encResp,workingKey)

	data = decResp.split('&')

	res = {}

	for x in data:
		d = x.split('=')
		res.update({d[0]: d[1]})

	# cur = db.event_tickets.find({'res.0.order_status': 'Success'}).sort('_id',pymongo.DESCENDING).limit(1)
	# cur_data = json.loads(dumps(cur))

	# bib_s = cur_data[0]['bib']['end'] + 1
	# bib_e = bib_s + int(res['merchant_param3']) - 1

	# cur = db.event_tickets.update({'order_id': res['order_id']}, {'$set': { 'res.0': res}})

	# if res['order_status'] == 'Success':
		# order_id = res['order_id']
		# event_name = str(res['merchant_param3'])
		# event_venue = str(res['merchant_param4'])
		# email_header = str(res['merchant_param5'])
		# sub_total = str( 599 * int(res['merchant_param3']))
		# processing_fees = str( float(res['mer_amount']) - float( 599 * int(res['merchant_param3'] ) ) )
		# total = str(res['mer_amount'])
		# billing_email = res['billing_email']

		# sendemail(res['billing_name'], order_id, event_name, billing_email)
		# sendthemail(res['billing_name'], order_id, '1', event_name, event_venue, email_header, billing_email)

	return {'order_id': res['order_id'], 'order_status': res['order_status']}
