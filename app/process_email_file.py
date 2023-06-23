import os
import datetime
from email_obj import Email,filter_email
from extract_msg import Message
from email.utils import parseaddr
from dateutil import parser
import email

class Process:

    def __init__(self, path,filter_values):
        self.path = path
        self.filter_values = filter_values

    def rename_email_file(self,file,lock):
        if(file.endswith(".msg")):
            email_obj = Process.read_msg_file(self,file)
        elif(file.endswith(".eml") ):
            email_obj = Process.read_eml_file(self,file)

        try:
            date_time_obj = datetime.datetime.strptime(str(email_obj.date), '%a, %d %b %Y %H:%M:%S %Z')
        except ValueError:
            date_time_obj = parser.parse(email_obj.date,ignoretz=True)

    
        year = str(date_time_obj.year)[2:]
        month = str(date_time_obj.month).zfill(2)
        day = str(date_time_obj.day).zfill(2)

        sender = filter_email(email_obj.sender_email,email_obj.sender_name,self.filter_values)
        recipient = filter_email(email_obj.recipient_email,email_obj.recipient_name,self.filter_values)

        with lock:
            new_name = f"{year}-{month}-{day} {sender} à {recipient} -{email_obj.extension}"
            new_path = os.path.join(self.path, new_name)

            count = 1
            
            while os.path.exists(new_path):
                new_name = f"{year}-{month}-{day} {sender} à {recipient} - ({count}){email_obj.extension}"
                new_path = os.path.join(self.path, new_name)
                count += 1

            print("Renaming "+ file)
            file_path = os.path.join(self.path, file)
            os.rename(file_path, new_path)

    def read_eml_file(self,file_name):
        file_path = os.path.join(self.path, file_name)

        with open(file_path, 'r') as file:
            message = email.message_from_file(file)

        recipient = message['To']
        recipient_name, recipient_email = parseaddr(recipient)
        sender = message['From']
        sender_name, sender_email = parseaddr(sender)
        date = message['Date']
        return Email(sender_name,sender_email,recipient_name,recipient_email,date,".eml")


    def read_msg_file(self,file_name):
        file_path = os.path.join(self.path, file_name)
        msg = Message(file_path)
        
        date = msg.date
        sender_name, sender_email = parseaddr(msg.sender)
        recipient_name, recipient_email = msg.recipients[0].name,msg.recipients[0].email

        msg.close()

        return Email(sender_name,sender_email,recipient_name,recipient_email,date,".msg")