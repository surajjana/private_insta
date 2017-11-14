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

def promoEmail(email):
	# message = 'Hello'
	header  = 'From: Krispypapad<orders@krispypapad.com>\n'
	header += 'To: ' + email + '\n'
	header += 'MIME-Version: 1.0\n'
	header += 'Content-type: text/html\n'
	header += 'Subject: [Learn-ups] Arduino, Data Science & more...\n\n'

	message = '<!DOCTYPE html><html lang=en xmlns=http://www.w3.org/1999/xhtml xmlns:o=urn:schemas-microsoft-com:office:office xmlns:v=urn:schemas-microsoft-com:vml><meta charset=utf-8><meta content="width=device-width"name=viewport><meta content="IE=edge"http-equiv=X-UA-Compatible><meta name=x-apple-disable-message-reformatting><title></title><!--[if mso]><style>*{font-family:sans-serif!important}</style><![endif]--><!--[if !mso]><!--><!--<![endif]--><style>body,html{margin:0 auto!important;padding:0!important;height:100%!important;width:100%!important}*{-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}div[style*="margin: 16px 0"]{margin:0!important}table,td{mso-table-lspace:0!important;mso-table-rspace:0!important}table{border-spacing:0!important;border-collapse:collapse!important;table-layout:fixed!important;margin:0 auto!important}table table table{table-layout:auto}img{-ms-interpolation-mode:bicubic}.aBn,.x-gmail-data-detectors,.x-gmail-data-detectors *,[x-apple-data-detectors]{border-bottom:0!important;cursor:default!important;color:inherit!important;text-decoration:none!important;font-size:inherit!important;font-family:inherit!important;font-weight:inherit!important;line-height:inherit!important}.a6S{display:none!important;opacity:.01!important}img.g-img+div{display:none!important}.button-link{text-decoration:none!important}@media only screen and (min-device-width:375px) and (max-device-width:413px){.email-container{min-width:375px!important}}@media screen and (max-width:480px){u~div .email-container{min-width:100vw;width:100%!important}}</style><style>.button-a,.button-td{transition:all .1s ease-in}.button-a:hover,.button-td:hover{background:#555!important;border-color:#555!important}@media screen and (max-width:600px){.email-container{width:100%!important;margin:auto!important}.fluid{max-width:100%!important;height:auto!important;margin-left:auto!important;margin-right:auto!important}.stack-column,.stack-column-center{display:block!important;width:100%!important;max-width:100%!important;direction:ltr!important}.stack-column-center{text-align:center!important}.center-on-narrow{text-align:center!important;display:block!important;margin-left:auto!important;margin-right:auto!important;float:none!important}table.center-on-narrow{display:inline-block!important}.email-container p{font-size:17px!important}}</style><!--[if gte mso 9]><xml><o:officedocumentsettings><o:allowpng><o:pixelsperinch>96</o:pixelsperinch></o:officedocumentsettings></xml><![endif]--><body bgcolor=#222222 style=margin:0;mso-line-height-rule:exactly width=100%><center style=width:100%;background:#222;text-align:left><div style=display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;font-family:sans-serif>Join us coming Sunday, i.e., 19th Nov, 2017 from 9 A.M to 12 P.M for ths informative learn-up by Krispy Papad in association with Opencube Labs and enter into the exciting world of electronics.</div><table border=0 cellpadding=0 cellspacing=0 role=presentation align=center width=600 style=margin:auto class=email-container><tr><td style="padding:20px 0;text-align:center"><img alt=alt_text border=0 height=50 src=https://www.krispypapad.com/img/kp-logo.png style=height:auto;background:#ddd;font-family:sans-serif;font-size:15px;line-height:140%;color:#555 width=200></table><table border=0 cellpadding=0 cellspacing=0 role=presentation align=center width=600 style=margin:auto class=email-container><tr><td bgcolor=#ffffff align=center><img alt=alt_text border=0 height=""src=https://www.krispypapad.com/img/events/arduino-new.jpg style=width:100%;max-width:600px;height:auto;background:#ddd;font-family:sans-serif;font-size:15px;line-height:140%;color:#555;margin:auto width=600 class=g-img align=center><tr><td style="padding:40px 40px 20px;text-align:center"bgcolor=#ffffff><h1 style=margin:0;font-family:sans-serif;font-size:24px;line-height:125%;color:#333;font-weight:400>"Getting started with Arduino"</h1><tr><td style="padding:0 40px 40px;font-family:sans-serif;font-size:15px;line-height:140%;color:#555;text-align:center"bgcolor=#ffffff><p style=margin:0>Join us coming Sunday, i.e., 19th Nov, 2017 from 9 A.M to 12 P.M for ths informative learn-up by Krispy Papad in association with Opencube Labs and enter into the exciting world of electronics.<p>Now book your seat at flat 50% off! Just 199 INR onwards<tr><td style="padding:0 40px 40px;font-family:sans-serif;font-size:15px;line-height:140%;color:#555"bgcolor=#ffffff><table border=0 cellpadding=0 cellspacing=0 role=presentation align=center style=margin:auto><tr><td style=border-radius:3px;background:#222;text-align:center class=button-td><a href=https://www.krispypapad.com/event/ocl-arduino class=button-a style="background:#222;border:15px solid #222;font-family:sans-serif;font-size:13px;line-height:110%;text-align:center;text-decoration:none;display:block;border-radius:3px;font-weight:700">    <span style=color:#fff>Register Now</span>    </a></table><tr><td style=padding:10px dir=rtl valign=top align=center bgcolor=#ffffff width=100%><table border=0 cellpadding=0 cellspacing=0 role=presentation align=center width=100%><tr><td class=stack-column-center width=33.33%><table border=0 cellpadding=0 cellspacing=0 role=presentation align=center width=100%><tr><td style="padding:0 10px"dir=ltr valign=top><img alt=alt_text border=0 height=170 src=https://www.krispypapad.com/img/events/odh.png style=height:auto;background:#ddd;font-family:sans-serif;font-size:15px;line-height:140%;color:#555 width=170 class=center-on-narrow></table><td class=stack-column-center width=66.66%><table border=0 cellpadding=0 cellspacing=0 role=presentation align=center width=100%><tr><td style=font-family:sans-serif;font-size:15px;line-height:140%;color:#555;padding:10px;text-align:left class=center-on-narrow dir=ltr valign=top><h2 style="margin:0 0 10px 0;font-family:sans-serif;font-size:18px;line-height:125%;color:#333;font-weight:700">Introduction to Open Data & Data Science</h2><p style="margin:0 0 10px 0">19th Nov, 2017 | 2 P.M - 4 P.M<table border=0 cellpadding=0 cellspacing=0 role=presentation class=center-on-narrow style=float:left><tr><td style=border-radius:3px;background:#222;text-align:center class=button-td><a href=https://www.krispypapad.com/event/odh-data-science class=button-a style="background:#222;border:15px solid #222;font-family:sans-serif;font-size:13px;line-height:110%;text-align:center;text-decoration:none;display:block;border-radius:3px;font-weight:700"><span style=color:#fff class=button-link>    Register Now    </span></a></table></table></table><tr><td style=padding:10px dir=ltr valign=top align=center bgcolor=#ffffff width=100%><table border=0 cellpadding=0 cellspacing=0 role=presentation align=center width=100%><tr><td class=stack-column-center width=33.33%><table border=0 cellpadding=0 cellspacing=0 role=presentation align=center width=100%><tr><td style="padding:0 10px"dir=ltr valign=top><img alt=alt_text border=0 height=170 src=https://www.krispypapad.com/img/events/ocl-cdp.png style=height:auto;background:#ddd;font-family:sans-serif;font-size:15px;line-height:140%;color:#555 width=170 class=center-on-narrow></table><td class=stack-column-center width=66.66%><table border=0 cellpadding=0 cellspacing=0 role=presentation align=center width=100%><tr><td style=font-family:sans-serif;font-size:15px;line-height:140%;color:#555;padding:10px;text-align:left class=center-on-narrow dir=ltr valign=top><h2 style="margin:0 0 10px 0;font-family:sans-serif;font-size:18px;line-height:125%;color:#333;font-weight:700">CanSat Development Program</h2><p style="margin:0 0 10px 0">26th Nov, 2017 | 10 A.M - 4 P.M<table border=0 cellpadding=0 cellspacing=0 role=presentation class=center-on-narrow style=float:left><tr><td style=border-radius:3px;background:#222;text-align:center class=button-td><a href=https://www.krispypapad.com/event/ocl-cansat-development-program class=button-a style="background:#222;border:15px solid #222;font-family:sans-serif;font-size:13px;line-height:110%;text-align:center;text-decoration:none;display:block;border-radius:3px;font-weight:700"><span style=color:#fff class=button-link>    Register Now    </span></a></table></table></table><tr><td style=font-size:0;line-height:0 aria-hidden=true height=40> <tr><td bgcolor=#ffffff><table border=0 cellpadding=0 cellspacing=0 role=presentation width=100%><tr><td style=padding:40px;font-family:sans-serif;font-size:15px;line-height:140%;color:#555><center><p>info@krispypapad.com<p><a href=//fb.com/krispypapad>fb.com/krispypapad</a></center></table></table><table border=0 cellpadding=0 cellspacing=0 role=presentation align=center width=100% style=max-width:680px;font-family:sans-serif;color:#888;font-size:12px;line-height:140%><tr><td style="padding:40px 10px;width:100%;font-family:sans-serif;font-size:12px;line-height:140%;text-align:center;color:#888"class=x-gmail-data-detectors><br><br>Hello Krispypapad LLP<br>#15, Bhuvi, 8th Cross, Bhubaneshwari Nagar, Dasarahalli Main Road, Kempapura, Hebbal, Bangalore-24<br>+91-7975769651<br><br></table></center>'

	message = header + message

	server = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', 587)
	server.starttls()
	server.login('AKIAIAHQ56UJBIHV75BA','AjTar1h/T5omIVYopVvb+IpvVuVBv+nAiTmKhzoEFcFb')
	
	problems = server.sendmail('orders@krispypapad.com', email, message)
	print('Email sent')
	
	server.quit()

email_list = "kk.bindumalini@gmail.com,javednisar.shaikh@gmail.com,er.ektaagrawal@gmail.com,vtu5107@veltechuniv.edu.in,rnramkumar@gmail.com"
email_list = email_list.split(',')

print len(email_list)

counter = 0

for x in email_list:
	promoEmail(x)
	print counter
	counter = counter + 1