import smtplib

def sendClientEmail(name, order_id, event_id, amount, billing_email):
	header  = 'From: Krispypapad<orders@krispypapad.com>\n'
	header += 'To: ' + billing_email + '\n'
	header += 'Subject: [Order Notification] Your ticket \n\n'
	
	message = 'Dear ' + name + ', \n\n'
	message += 'Show this email for entry :-)\n\n'
	message += 'Participant name : ' + name + '\n'
	message += 'Order id : ' + order_id + '\n'
	message += 'Event id : ' + event_id + '\n'
	message += 'Amount paid : ' + amount + '\n\n'
	message += 'Thank you,\n\n'
	message += 'Regards,\nKrispypapad Team'

	message = header + message

	server = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', 587)
	server.starttls()
	server.login('AKIAIAHQ56UJBIHV75BA','AjTar1h/T5omIVYopVvb+IpvVuVBv+nAiTmKhzoEFcFb')
	
	problems = server.sendmail('orders@krispypapad.com', billing_email, message)
	print('Email sent')
	
	server.quit()

def sendMerEmail(mer_name, name, order_id, event_id, amount, mer_email):
	header  = 'From: Krispypapad<orders@krispypapad.com>\n'
	header += 'To: ' + mer_email + '\n'
	header += 'Subject: [Order Notification] Ticket purchased \n\n'
	
	message = 'Dear ' + mer_name + ', \n\n'
	message += 'You have got a registration for your event :-)\n\n'
	message += 'Participant name : ' + name + '\n'
	message += 'Order id : ' + order_id + '\n'
	message += 'Event id : ' + event_id + '\n'
	message += 'Amount paid : ' + amount + '\n\n'
	message += 'Thank you,\n\n'
	message += 'Regards,\nKrispypapad Team'

	message = header + message

	server = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', 587)
	server.starttls()
	server.login('AKIAIAHQ56UJBIHV75BA','AjTar1h/T5omIVYopVvb+IpvVuVBv+nAiTmKhzoEFcFb')
	
	problems = server.sendmail('orders@krispypapad.com', mer_email, message)
	print('Email sent')
	
	server.quit()

def sendEmail(to_email, subject, message):
	header  = 'From: Krispypapad<orders@krispypapad.com>\n'
	header += 'To: ' + to_email + '\n'
	header += 'Subject: ' + subject + ' \n\n'

	message = header + message

	server = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', 587)
	server.starttls()
	server.login('AKIAIAHQ56UJBIHV75BA','AjTar1h/T5omIVYopVvb+IpvVuVBv+nAiTmKhzoEFcFb')
	
	problems = server.sendmail('orders@krispypapad.com', to_email, message)
	print('Email sent')
	
	server.quit()

# name = 'Suraj Kumar Jana'
# order_id = '34627836487283478563478'
# event_id = 'Test event name'
# amount = '199'

# message = 'Dear ' + name + ', \n\n'
# message += 'Thanks for registration :-) Here is your ticket...\n\n'
# message += 'Participant name : ' + name + '\n'
# message += 'Order id : ' + order_id + '\n'
# message += 'Event name : ' + event_id + '\n'
# message += 'Amount paid : ' + amount + ' INR\n\n'
# message += 'Thank you,\n\n'
# message += 'Regards,\nKrispypapad Team\ninfo@krispypapad.com'

# sendEmail('surajjana2@gmail.com','Tickets of Test Event', message)