import json
from pymongo import MongoClient
from bson.json_util import dumps

from notify import *

# client = MongoClient('mongodb://bae:bae@34.228.79.24:27017/bae_chat')
# db = client.bae_chat

# client = MongoClient()
# db = client.test

# cur = db.kp_data.find()

# email_list = json.loads(dumps(cur))
# # email_list = email_list.split(',')

# print len(email_list)

# counter = 20

# s_emails = "madhu1408.bharti@gmail.com,lakshmis1903@gmail.com,sauarbh094@gmail.com,gkamudhu@gmail.com,phanindra.m10@gmail.com ,sahanam64@gmail.com,shreyaskumarts4142@gmail.com,meghananrgowda95@gmail.com,nagashree2195@gmail.com,meghananrgowda95@gmail.com,chiranth1910@gmail.com,brthirumalesh@gmail.com,aranya175@gmail.com,pratheeks1@gmail.com,adityashegde361995@gmail.com,rohithkumar31@gmail,thyagaraj_tanjavur@bmsit.in,bhargavs525@gmail.com,rajaniket10@gmail.com,kediarahul.kedia8@gmail.com,srinidhi738@gmail.com,athuls80@yahoo.com,arunvs9343@gmail.com,Akshreyamalge@gmail.com,vikeshpurbey@gmail.com,deeptireddy1994@gmail.com,uthappa4@gmail.com,dyallappa1@gmail.com,poojashankar@gmail.com,sumanakumar@gmail.com,tejaswinikumar@gmail.com,srikarsr@gmail.com,Abhishekyadav602@gmail.com,surajperfect@rediffmail.com,shivrajakumara1995@gmail.com,shridharcn000@gmail.com,k.s.meghanathan100@gmail.com,akash.jaiswal8406@gmail.com,virukohli143@gmail.com,kanwarjitsingh069@gmail.com ,ravishvmc@gmail.com ,kamaltiwari7394@gmail.com,Saddam6815@gmail.com,msingh88888@gmail.com,rohitanil007@Hotmail.com,Raghukumar7739@gmail.com,aayush.narqyan7@gmail.com,sunilsrinivas19@gmail.com,darshanbharathk@gmail.com,navaneethps1995@gmail.com,vsn.vasu84@gmail.com,akshaynaik7101995@gmail.com,priyeshg123@gmail.com,singh.bidya2@gmail.com,kadallimanjunath@gmail.com,sunaveen06@gmail.com,justtinthecoolguy@gmail.com,namratha.coorg@gmail.com,kirenmoncy@yahoo.co.in,nikilesh122@gmail.com,divya.gombe321@gmail.com,geetha.gayathri8@gmail.com,divya.gombe321@gmail.com,deepith.nayak@gmail.com,Chetanng92@gmail.com,prema5953@gmail.com,RAMYA2561996@gmail.com,rekha8ag@gmail.com,srinandhu687@gmail.com,srinandhu687@gmail.com,prathu496@gmail.com,stive.lf@gmail.com,stive.lf@gmail.com,stive.lf@gmail.com,vaninagliekar@gmail.com,stive.lf@gmail.com,stive.lf@gmail.com,adityakumarraut95@gmail.com ,md.ishteyaque3@gmail.com ,aarpitha2207@gmail.com,mrutyunjaybkalyani1@gmail.com,www.ravik9395@gmail.com,www.ashausha486@gmail.com,megamurthy772@gmail.com,bbpece@gmail.com,megamurthy772@gmail.com,kusuma.rcn@gmail.com,iqbal231192@gmail.com,runthla121@gmail.com,deeksha.shanbhag@gmail.com,madhurikprasad@gmail.com,ashrafmanvswild@gmail.com,skmkk756@gmail.com,shankadhrajesh@gmail.com,18teju96@gmail.com,srinchanaraj@gmail.com"

# s_emails = s_emails.split(',')

# print len(s_emails)

# # print s_emails[0], s_emails[1]

# for x in s_emails:
# 	promoEmail(x)
# 	print counter
	# counter += 1


# for x in range(501, len(email_list)):

# 	try:
# 		if(email_list[x]['temp_details']['email']):
# 			promoEmail(email_list[x]['temp_details']['email'])
# 	except:
# 		print 'Exception'
# 	finally:
# 		print 'Final'
# 	print counter
# 	counter = counter + 1

promoEmail('surajjana2@gmail.com')