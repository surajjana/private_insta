import os
import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


SENDER = "Open Data Hack <hi@opendatahack.org>"


AWS_REGION = "us-east-1"


SUBJECT = "[Certificate] Introduction to Open Data & Data Science Learn-up by Open Data Hack on 19th November, 2017"

def send_cert_attach(email_id, name, file_name):

    RECIPIENT = email_id

    ATTACHMENT = "./odh_cert/" + file_name + ".pdf"

    BODY_TEXT = "Hello " + name + "!,\r\nThank you for attending Introduction to Open Data & Data Science Learn-up by Open Data Hack on 19th November, 2017. Please find attached your certificate.\n\nFollow us on Twitter(twitter.com/_opendatahack), like us on Facebook(fb.com/opendatahack) to get updated about our future events.\n\nThank you,\n\nRegards,\nSuraj Kumar Jana\nGlobal community coordinator\nhttps://www.opendatahack.org"

    BODY_HTML = """\
    <html>
    <head></head>
    <body>
    <h1>Hello """ + name + """!</h1>
    <p>Thank you for attending Introduction to Open Data & Data Science Learn-up by Open Data Hack on 19th November, 2017. Please find attached your certificate.</p>
    <p>Follow us on Twitter(twitter.com/_opendatahack), like us on Facebook(fb.com/opendatahack) to get updated about our future events.</p>
    <br>
    <p>Thank you,</p>
    <br>
    <p>Regards,</p>
    <p>Suraj Kumar Jana</p>
    <p>Global community coordinator</p>
    <p>https://www.opendatahack.org</p>
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


names = ['Ali Raza','Abu Bakr','VR Krishna Prasad Sajja','Somnath Mahato','Nithyashree K','Salman Shariff','Rohith Kumar P']
email_ids = ['sanadi.raza@gmail.com','abuhaider2011@gmail.com','rankyp@gmail.com','somnathmahato723@gmail.com','nithyavishwakarma.gkm@gmail.com','salmanshariff.salman@gmail.com','rohithkumar31@gmail.com']
file_names = ['DS191117001','DS191117002','DS191117003','DS191117004','DS191117005','DS191117006','DS191117007']

for i in range(0, len(names)):
    print i+1
    send_cert_attach(email_ids[i], names[i], file_names[i])