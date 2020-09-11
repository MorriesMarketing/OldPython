import locale
locale.setlocale(locale.LC_ALL, '')  # empty string for platform's default settings
from pathlib import Path
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

folder = Path('C:/Users/gamer/Documents/')
Walser_Ignite_Specials = folder / 'Walser Ignite Specials.xlsx'
class Email():
    def __init__(self,to,cc,subject,html_body,attachment):
        self.outlook = win32.Dispatch('outlook.application')
        self.mail = self.outlook.CreateItem(0)
        self.mail.To = to
        self.mail.CC = cc
        self.mail.Subject = subject
        self.mail.HTMLBody = html_body
        self.mail.Attachments.Add(attachment)
        self.mail.Send()

def send_email(email_recipient,
               email_subject,
               email_message,
               attachment_location = ''):

    email_sender = 'mmuhlenkort@walser.com'

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_recipient
    msg['Subject'] = email_subject

    msg.attach(MIMEText(email_message, 'plain'))

    if attachment_location != '':
        filename = os.path.basename(attachment_location)
        attachment = open(attachment_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        "attachment; filename= %s" % filename)
        msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.ehlo()
        server.starttls()
        server.login('mmuhlenkort@walser.com', '$quati$RulZ39')
        text = msg.as_string()
        server.sendmail(email_sender, email_recipient, text)
        print('email sent')
        server.quit()
    except:
        print("SMPT server connection error")
    return True

send_email('mmuhlenkort@walser.com',
           'Happy New Year',
           'We love Outlook', 
           'C:/Users/gamer/Documents/Walser Ignite Specials.xlsm')