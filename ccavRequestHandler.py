#!/usr/bin/python

from flask import request, redirect, Flask, render_template
from ccavutil import encrypt,decrypt
from ccavResponseHandler import res
from string import Template
app = Flask('ccavRequestHandler') 

'''
Please put in the 32 bit alphanumeric key and Access Code in quotes provided by CCAvenues.
'''

accessCode = 'AVHA69EB15AS94AHSA' 	
workingKey = 'FDCDFB0F903F843FDDA8BF74F37C12B1'

@app.route('/')
def webprint():
    return render_template('dataFrom.htm')

@app.route('/ccavResponseHandler', methods=['GET', 'POST'])
def ccavResponseHandler():
    plainText = res(request.form['encResp'])
    return plainText

@app.route('/ccavRequestHandler', methods=['GET', 'POST'])
def login():
	p_merchant_id = request.form['merchant_id']
	p_order_id = request.form['order_id']
	p_currency = request.form['currency']
	p_amount = request.form['amount']
	p_redirect_url = request.form['redirect_url']
	p_cancel_url = request.form['cancel_url']
	p_language = request.form['language']
	p_customer_identifier = request.form['customer_identifier']
	
	

	merchant_data='merchant_id='+p_merchant_id+'&'+'order_id='+p_order_id + '&' + "currency=" + p_currency + '&' + 'amount=' + p_amount+'&'+'redirect_url='+p_redirect_url+'&'+'cancel_url='+p_cancel_url+'&'+'language='+p_language+'&'+'customer_identifier='+p_customer_identifier+'&'
		
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

#Host Server and Port Number should be configured here.

if __name__ == '__main__':
    #app.run(host = '127.0.0.1', port = 8080)
    app.run()


