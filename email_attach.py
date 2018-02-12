import os
import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


SENDER = "Opencube Labs <suraj@ocl.space>"


AWS_REGION = "us-east-1"


SUBJECT = "[CERTIFICATE] Data Science Workshop by Open Data Hack & Opencube Labs on 11th February, 2018"

def send_cert_attach(email_id, name, file_name):

    RECIPIENT = email_id

    ATTACHMENT = "./ocl_cert/" + file_name + ".pdf"


    BODY_TEXT = "Hello " + name + "!,\r\nThank you for attending Data Science Workshop by Open Data Hack & Opencube Labs on 11th February, 2018. Please find attached your certificate.\n\nPresentation URL : https://www.slideshare.net/SurajKumarJana/introduction-to-open-data-and-data-science\n\nCode Notebooks : https://github.com/opencubelabs/notebooks\n\nFollow us on Twitter(twitter.com/opencubelabs), like us on Facebook(fb.com/opencubelabs) to get updated about our future events.\n\nThank you,\n\nRegards,\nSuraj Kumar Jana\nFounder & CEO, Opencube Labs\nhttp://ocl.space"

    BODY_HTML = """\
    <html>
    <head></head>
    <body>
    <h1>Hello """ + name + """!</h1>
    <p>Thank you for attending Data Science Workshop by Open Data Hack & Opencube Labs on 11th February, 2018. Please find attached your certificate.</p>
    <p>Presentation URL : https://www.slideshare.net/SurajKumarJana/introduction-to-open-data-and-data-science</p>
    <p>Code Notebooks : https://github.com/opencubelabs/notebooks</p>
    
    <p>Follow us on Twitter(twitter.com/opencubelabs), like us on Facebook(fb.com/opencubelabs) to get updated about our future events.</p>
    <br>
    <p>Thank you,</p>
    <br>
    <p>Regards,</p>
    <p>Suraj Kumar Jana</p>
    <p>Founder & CEO, Opencube Labs</p>
    <p>http://ocl.space</p>
    </body>
    </html>
    """

    CHARSET = "utf-8"

    client = boto3.client('ses',region_name=AWS_REGION, aws_access_key_id = 'AKIAJHF4Q3ID4XZZ3DZQ', aws_secret_access_key = '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')

    msg = MIMEMultipart('mixed')
    msg['Subject'] = SUBJECT 
    msg['From'] = SENDER 
    msg['To'] = RECIPIENT

    msg_body = MIMEMultipart('alternative')

    textpart = MIMEText(BODY_TEXT.encode(CHARSET), 'plain', CHARSET)
    htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)

    msg_body.attach(textpart)
    msg_body.attach(htmlpart)

    att = MIMEApplication(open(ATTACHMENT, 'rb').read())

    att.add_header('Content-Disposition','attachment',filename=os.path.basename(ATTACHMENT))

    

    msg.attach(msg_body)

    msg.attach(att)

    try:
        response = client.send_raw_email(
            Source=SENDER,
            Destinations=[
                RECIPIENT
            ],
            RawMessage={
                'Data':msg.as_string(),
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['ResponseMetadata']['RequestId'])


import xlrd

book = xlrd.open_workbook('cert-data.xls')
sheet = book.sheet_by_index(0)

# names = ['Rahul Upadhyay','Md. Danish','Revanth Kumar','Venkatesh Sharma','Harshith SV','Sumit Ranjan']
# email_ids = ['rku1327@gmail.com','mddanishazmi152@gmail.com','revanthkumar271@gmail.com','venkateshsharma13@gmail.com','hm990000@gmail.com','ranjan.sumit79@gmail.com']
# file_names = ['MLPY140118001', 'MLPY140118002', 'MLPY140118003', 'MLPY140118004', 'MLPY140118005', 'MLPY140118006']

for i in range(0, sheet.nrows):
    print i+1
    send_cert_attach(str(sheet.cell(i,1).value), str(sheet.cell(i,0).value), str(sheet.cell(i,2).value))


# send_cert_attach('surajjana2@gmail.com', 'Suraj', 'AR031217001')