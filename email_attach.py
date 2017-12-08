import os
import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


SENDER = "Opencube Labs <hello@ocl.space>"


AWS_REGION = "us-east-1"


SUBJECT = "[CERTIFICATE] Arduino : Hands-on Workshop by Opencube Labs on 3rd December, 2017"

def send_cert_attach(email_id, name, file_name):

    RECIPIENT = email_id

    ATTACHMENT = "./ocl_cert/" + file_name + ".pdf"


    BODY_TEXT = "Hello " + name + "!,\r\nThank you for attending Arduino : Hands-on Workshop by Opencube Labs on 3rd December, 2017. Please find attached your certificate.\n\nFollow us on Twitter(twitter.com/opencubelabs), like us on Facebook(fb.com/opencubelabs) to get updated about our future events.\n\nThank you,\n\nRegards,\nSuraj Kumar Jana\nFounder & CEO, Opencube Labs\nhttp://ocl.space"

    BODY_HTML = """\
    <html>
    <head></head>
    <body>
    <h1>Hello """ + name + """!</h1>
    <p>Thank you for attending Arduino : Hands-on Workshop by Opencube Labs on 3rd December, 2017. Please find attached your certificate.</p>
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


names = ['Abdul Rehman Iftekhar','Mohit Kumar','Preeti N Kini','Vinutha MR','Manjunath .P','Amruth Raj S.A','Deekshith Gowda H.P']
email_ids = ['abdria26@gmail.com','m_kumar@students.iitmandi.ac.in','preetikini653@gmail.com','vinutharpkv@gmail.com','manjup93@gmail.com','amruthrajsagara@yahoo.com','deekshith2211@gmail.com']
file_names = ['AR031217001', 'AR031217002', 'AR031217003', 'AR031217004', 'AR031217005', 'AR031217006', 'AR031217007']

for i in range(0, len(names)):
    print i+1
    send_cert_attach(email_ids[i], names[i], file_names[i])


# send_cert_attach('surajjana2@gmail.com', 'Suraj', 'AR031217001')