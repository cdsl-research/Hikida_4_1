from smtplib import SMTP
from email.mime.text import MIMEText
from email.utils import formatdate

TO_ADDRESS = "hkdatadog@gmail.com"
FROM_ADDRESS = "hkdatadog@gmail.com"
FROM_PASSWORD = "tatuki817"

def createMail(text, sub, FROM, TO):

    msg = MIMEText(text, "html")
    msg["Subject"] = sub
    msg["From"] = FROM
    msg["To"] = TO
    msg['Date'] = formatdate()

    return msg