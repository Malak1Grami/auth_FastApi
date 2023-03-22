
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

async def send_email(subject:str, recipient:str, message:str):
    mailer = smtplib.SMTP(host='smtp.gmail.com', port=587)
    mailer .starttls()
    mailer.login("email@gmail.com", "password")
    mailer.ehlo()
    #email body
    msg = MIMEMultipart()
    msg['From']="Name"
    msg['To']=recipient
    msg['Subject']=subject
    msg.attach( MIMEText(message,'html'))
    mailer.send_message(msg)