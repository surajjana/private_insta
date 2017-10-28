#!/usr/bin/python

from ccavutil import encrypt,decrypt
from string import Template
from pymongo import MongoClient
from bson.json_util import dumps
import json
import pymongo
from notify import sendClientEmail, sendMerEmail


# client = MongoClient('mongodb://su:su@52.37.155.102:27017/kp_events')
# # client = MongoClient()
# db = client.kp_events


def res_test(encResp):
	'''
	Please put in the 32 bit alphanumeric key in quotes provided by CCAvenues.
	'''	 
	# workingKey = '7D9D1B56365DC282F2F83E8B1C9D4A04'
	workingKey = 'DEDE391379CF9113C0DE2ADF7DA7C235'
	decResp = decrypt(encResp,workingKey)

	data = decResp.split('&')

	mer_name = 'UVCE'
	mer_email = 'inspiron2k17@campusuvce.in'

	res = {}

	for x in data:
		d = x.split('=')
		res.update({d[0]: d[1]})

	# cur = db.event_tickets.find({'res.0.order_status': 'Success'}).sort('_id',pymongo.DESCENDING).limit(1)
	# cur_data = json.loads(dumps(cur))

	# bib_s = cur_data[0]['bib']['end'] + 1
	# bib_e = bib_s + int(res['merchant_param3']) - 1

	# cur = db.event_tickets.update({'order_id': res['order_id']}, {'$set': { 'res.0': res}})

	if res['order_status'] == 'Success':
		order_id = res['order_id']
		event_id = str(res['merchant_param1'])
		name = res['billing_name']
		email = res['billing_email']
		amount = res['mer_amount']
		
		sendClientEmail(name, order_id, event_id, amount, email)
		sendMerEmail(mer_name, name, order_id, event_id, amount, mer_email)
		

	return {'name': res['billing_name'], 'order_id': res['order_id'], 'event_id': res['merchant_param1'], 'amount': res['mer_amount'], 'order_status': res['order_status']}

def res(encResp):
	'''
	Please put in the 32 bit alphanumeric key in quotes provided by CCAvenues.
	'''	 
	workingKey = '7D9D1B56365DC282F2F83E8B1C9D4A04'
	# workingKey = 'DEDE391379CF9113C0DE2ADF7DA7C235'
	decResp = decrypt(encResp,workingKey)

	mer_name = 'UVCE'
	mer_email = 'surajjana2@gmail.com'

	data = decResp.split('&')

	res = {}

	for x in data:
		d = x.split('=')
		res.update({d[0]: d[1]})

	if res['order_status'] == 'Success':
		order_id = res['order_id']
		event_id = str(res['merchant_param1'])
		name = res['billing_name']
		email = res['billing_email']
		amount = res['mer_amount']
		
		sendClientEmail(name, order_id, event_id, amount, email)
		sendMerEmail(mer_name, name, order_id, event_id, amount, mer_email)

	return {'name': res['billing_name'], 'order_id': res['order_id'], 'event_id': res['merchant_param1'], 'amount': res['mer_amount'], 'order_status': res['order_status']}