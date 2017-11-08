from bottle import Bottle, run, route, static_file, request, response, template
from pymongo import MongoClient
from bson.json_util import dumps
from string import Template
from ccavutil import encrypt,decrypt
from ccavResponseHandler import *
import json
import pymongo
import requests
import datetime
import time
import urlparse
import hashlib
import os

from notify import *

app = Bottle(__name__)

client = MongoClient('mongodb://bae:bae@34.228.79.24:27017/bae_chat')
# # client = MongoClient()
db = client.bae_chat

@app.route('/')
def root():
	# return template('templates/index.tpl')
	return static_file('index.html', root='templates/')

@app.route('/privacy-policy')
def privacy_policy():
	return static_file('privacy-policy.html', root='templates/')

@app.route('/terms-of-service')
def terms_of_service():
	return static_file('terms-of-service.html', root='templates/')

@app.route('/event/<filename>')
def filename(filename):
	return static_file(filename + '.html', root='templates/')

@app.route('/e/<eid>')
def event(eid):
	# cur = db.event.find({'eid': int(eid)})
	# data = json.loads(dumps(cur))[0]

	#data = {'name': 'Test event name', 'date': '12th Nov, 2017', 'time': '10 A.M - 12 P.M', 'venue': 'Test venue address', 'organiser': 'Sai Krishna, info@krispypapad.com', 'img': 'bitcoin.png', 'description': 'Test description'}
	data = [{'eid':1,'name':'Introduction to Data Science & all about open data','date':'3rd Nov, 2017','time':'2 P.M - 4 P.M','venue':'BMS Institute of Technology & Mgmt., Avalahalli, Bangalore-560064','organiser':'NA','img':'data_science.png','description':'NA','price':'Free','speakers':[{'name':'Suraj Jana','description':'NA','img':'suraj.png'}]},{'eid':2,'name':'Introduction to Bitcoin & other cryptocurrencies','date':'12th Nov, 2017','time':'10 A.M - 12 P.M','venue':'Opencube Labs, Hebbal, Bangalore-560024','organiser':'NA','img':'bitcoin.png','description':'NA','price':'Free','speakers':[{'name':'Suraj Jana','description':'NA','img':'suraj.png'}]},{'eid':3,'name':'Introduction to Python Programming','date':'12th Nov, 2017','time':'2 P.M - 4 P.M','venue':'Opencube Labs, Hebbal, Bangalore-560024','organiser':'NA','img':'python.png','description':'NA','price':'Free','speakers':[{'name':'Suraj Jana','description':'NA','img':'suraj.png'}]},{'eid':4,'name':'Introduction to Open Hardware & Arduino','date':'To be decided','time':'NA','venue':'Opencube Labs, Hebbal, Bangalore-560024','organiser':'NA','img':'arduino.png','description':'NA','price':'Free','speakers':[{'name':'Suraj Jana','description':'NA','img':'suraj.png'}]}]

	return template('templates/event.tpl', data[int(eid) - 1])

@app.post('/reg/free')
def reg():
	event_id = request.forms.get('event_id')
	order_id = hashlib.md5(str(time.time())).hexdigest()
	name = request.forms.get('name')
	email = request.forms.get('email')
	mobile = request.forms.get('mobile')

	data = {'event_id': event_id, 'order_id': order_id, 'name': name, 'email': email, 'mobile': mobile}

	cur = db.kp_event_tickets.insert(data)

	message = 'Dear ' + name + ', \n\n'
	message += 'Thanks for registration :-) You will receive a confirmation email soon.\n\n'
	message += 'Participant name : ' + name + '\n'
	message += 'Order id : ' + order_id + '\n'
	message += 'Event id : ' + event_id + '\n\n'
	message += 'Thank you,\n\n'
	message += 'Regards,\nKrispypapad Team\ninfo@krispypapad.com'

	sendEmail(email, 'Event ticket | ' + event_id, message)

	data = {'event_id': event_id, 'order_id': order_id, 'name': name, 'email': email}

	return template('templates/kp-order-status.tpl', data)

@app.post('/order-status-test')
def ccavResponseHandler():
    data = res_test(request.forms.get('encResp'))
    # data = json.loads(plainText)
    #return data

    return template('templates/order-status.tpl', data)

@app.post('/order-status')
def ccavResponseHandler():
    data = res(request.forms.get('encResp'))
    # data = json.loads(plainText)
    #return data

    return template('templates/order-status.tpl', data)

@app.post('/api/pay/test')
def order_payment():

	accessCode = 'AVPU00EB89BP61UPPB'
	workingKey = 'DEDE391379CF9113C0DE2ADF7DA7C235'

	# accessCode = 'AVHA69EB15AS94AHSA' 	
	# workingKey = '7D9D1B56365DC282F2F83E8B1C9D4A04'

	p_merchant_id = '123840'
	p_currency = 'INR'
	p_redirect_url = 'https://www.krispypapad.com/order-status-test'
	p_cancel_url = 'https://www.krispypapad.com/order-status-test'
	p_language = 'EN'

	# apikey = request.forms.get('apikey')

	p_order_id = request.forms.get('order_id')

	p_amount = request.forms.get('amount')
	p_billing_name = request.forms.get('name')
	p_billing_tel = request.forms.get('mobile')
	p_billing_email = request.forms.get('email')

	event_id = request.forms.get('event_id')

	merchant_data = 'merchant_id='+p_merchant_id+'&'+'order_id='+p_order_id + '&' + "currency=" + p_currency + '&' + 'amount=' + p_amount+'&'+'redirect_url='+p_redirect_url+'&'+'cancel_url='+p_cancel_url+'&'+'language='+p_language+'&'+'billing_name='+p_billing_name+'&'+'billing_tel='+p_billing_tel+'&'+'billing_email='+p_billing_email+'&'+'merchant_param1='+event_id+'&'
		
	encryption = encrypt(merchant_data,workingKey)

	html = '''\
<html>
<head>
	<title>Sub-merchant checkout page</title>
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
</head>
<body>
<form id="nonseamless" method="post" name="redirect" action="https://test.ccavenue.com/transaction/transaction.do?command=initiateTransaction" > 
		<input type="hidden" id="encRequest" name="encRequest" value=$encReq>
		<input type="hidden" name="access_code" id="access_code" value=$xscode>
		<script language='javascript'>document.redirect.submit();</script>
</form>    
</body>
</html>
'''
	fin = Template(html).safe_substitute(encReq=encryption,xscode=accessCode)
			
	return fin

@app.post('/api/pay')
def order_payment():

	# accessCode = 'AVPU00EB89BP61UPPB'
	# workingKey = 'DEDE391379CF9113C0DE2ADF7DA7C235'

	accessCode = 'AVHA69EB15AS94AHSA' 	
	workingKey = '7D9D1B56365DC282F2F83E8B1C9D4A04'

	p_merchant_id = '123840'
	p_currency = 'INR'
	p_redirect_url = 'https://www.krispypapad.com/order-status'
	p_cancel_url = 'https://www.krispypapad.com/order-status'
	p_language = 'EN'

	# apikey = request.forms.get('apikey')

	p_order_id = request.forms.get('order_id')

	p_amount = request.forms.get('amount')
	p_billing_name = request.forms.get('name')
	p_billing_tel = request.forms.get('mobile')
	p_billing_email = request.forms.get('email')

	event_id = request.forms.get('event_id')

	merchant_data = 'merchant_id='+p_merchant_id+'&'+'order_id='+p_order_id + '&' + "currency=" + p_currency + '&' + 'amount=' + p_amount+'&'+'redirect_url='+p_redirect_url+'&'+'cancel_url='+p_cancel_url+'&'+'language='+p_language+'&'+'billing_name='+p_billing_name+'&'+'billing_tel='+p_billing_tel+'&'+'billing_email='+p_billing_email+'&'+'merchant_param1='+event_id+'&'
		
	encryption = encrypt(merchant_data,workingKey)

	html = '''\
<html>
<head>
	<title>Sub-merchant checkout page</title>
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
</head>
<body>
<form id="nonseamless" method="post" name="redirect" action="https://secure.ccavenue.com/transaction/transaction.do?command=initiateTransaction" > 
		<input type="hidden" id="encRequest" name="encRequest" value=$encReq>
		<input type="hidden" name="access_code" id="access_code" value=$xscode>
		<script language='javascript'>document.redirect.submit();</script>
</form>    
</body>
</html>
'''
	fin = Template(html).safe_substitute(encReq=encryption,xscode=accessCode)
			
	return fin

@app.post('/order-info')
def ccavResponseHandlerKP():
    data = res_kp(request.forms.get('encResp'))
    # data = json.loads(plainText)
    #return data

    return template('templates/order-status.tpl', data)

@app.post('/api/pay/kp')
def order_payment_kp():

	accessCode = 'AVPU00EB89BP61UPPB'
	workingKey = 'DEDE391379CF9113C0DE2ADF7DA7C235'

	# accessCode = 'AVHA69EB15AS94AHSA' 	
	# workingKey = '7D9D1B56365DC282F2F83E8B1C9D4A04'

	p_merchant_id = '123840'
	p_currency = 'INR'
	p_redirect_url = 'https://www.krispypapad.com/order-info'
	p_cancel_url = 'https://www.krispypapad.com/order-info'
	p_language = 'EN'

	# apikey = request.forms.get('apikey')

	p_order_id = hashlib.md5(str(time.time())).digest().encode('base64').strip().replace(' ','')

	p_amount = request.forms.get('amount')
	p_billing_name = request.forms.get('name')
	p_billing_tel = request.forms.get('mobile')
	p_billing_email = request.forms.get('email')

	event_id = request.forms.get('event_id')

	merchant_data = 'merchant_id='+p_merchant_id+'&'+'order_id='+p_order_id + '&' + "currency=" + p_currency + '&' + 'amount=' + p_amount+'&'+'redirect_url='+p_redirect_url+'&'+'cancel_url='+p_cancel_url+'&'+'language='+p_language+'&'+'billing_name='+p_billing_name+'&'+'billing_tel='+p_billing_tel+'&'+'billing_email='+p_billing_email+'&'+'merchant_param1='+event_id+'&'
		
	encryption = encrypt(merchant_data,workingKey)

	html = '''\
<html>
<head>
	<title>Sub-merchant checkout page</title>
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
</head>
<body>
<form id="nonseamless" method="post" name="redirect" action="https://test.ccavenue.com/transaction/transaction.do?command=initiateTransaction" > 
		<input type="hidden" id="encRequest" name="encRequest" value=$encReq>
		<input type="hidden" name="access_code" id="access_code" value=$xscode>
		<script language='javascript'>document.redirect.submit();</script>
</form>    
</body>
</html>
'''
	fin = Template(html).safe_substitute(encReq=encryption,xscode=accessCode)
			
	return fin

# Static Routes
@app.route('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.(jpg|png|gif|ico|svg)>')
def images(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static')

@app.hook('after_request')
def enable_cors():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'