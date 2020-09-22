from pathlib import Path
import os.path
import win32com.client as win32

class Email():
    def __init__(self,to,cc,subject,html_body,attachment):
        self.outlook = win32.Dispatch('outlook.application')
        self.mail = self.outlook.CreateItem(0)
        self.mail.To = to
        self.mail.CC = cc
        self.mail.Subject = subject
        self.mail.HTMLBody = html_body
        self.mail.Attachments.Add(attachment)
        print('sending email')
        self.mail.Send()