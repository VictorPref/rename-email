from random import randint, choice
from datetime import datetime, timedelta
from independentsoft.msg import Message, Recipient
from independentsoft.msg import Message
from independentsoft.msg import Recipient
from independentsoft.msg import ObjectType
from independentsoft.msg import DisplayType
from independentsoft.msg import RecipientType

# List of example names
names = [
    "John Smith",
    "Alice Johnson",
    "Michael Williams",
    "Emma Brown",
    "David Jones",
    "Olivia Taylor",
    "Daniel Davis",
    "Sophia Anderson",
    "William Martinez",
    "Charlotte Wilson",
    "James Davis",
    "Ava Thomas",
    "Joseph Taylor",
    "Mia Martinez",
    "Charles Thompson",
    "Abigail Thomas",
    "Andrew Clark",
    "Emily Lewis",
    "Matthew Turner",
    "Harper Walker",
    "Ethan Hill",
    "Amelia Mitchell",
    "Alexander Moore",
    "Elizabeth Young",
    "Benjamin Scott",
    "Sofia Hernandez",
    "Jacob Green",
    "Ella Perez",
    "Samuel King",
    "Victoria Roberts",
    "Henry Adams"
]


def generate_random_name():
    return choice(names)

def create_fake_msg(subject, sender, recipients, body, date):
    msg = Message()

    # Set the subject, sender, and recipients
    msg.subject = subject
    msg.sender_name = sender
    msg.sender_email_address = sender+"@gmail.com"
    msg.encoding= "utf-8";

    for recipient_name, recipient_email in recipients:
        recipient1 = Recipient()
        recipient1.address_type = "SMTP"
        recipient1.display_type = DisplayType.MAIL_USER
        recipient1.object_type = ObjectType.MAIL_USER
       # recipient1.display_name = generate_random_name()
        recipient1.display_name = "Anthoine Préfontaine"
        recipient1.email_address = "John@domain.com"
        recipient1.recipient_type = RecipientType.TO
        msg.recipients.append(recipient1)

    # Set the body of the message
    msg.plain_text_body = body

    # Set the date of the message
    msg.client_submit_time = date

    # Save the message to a file
    msg.save(f"email/fake_message_{date.strftime('%Y%m%d%H%M%S')}.msg")
    print("Fake message created successfully.")

def generate_random_date(start_date, end_date):
    time_diff = end_date - start_date
    random_days = randint(0, time_diff.days)
    random_seconds = randint(0, 24 * 60 * 60 - 1)
    random_date = start_date + timedelta(days=random_days, seconds=random_seconds)
    return random_date

# Usage example
subject = "Fake Message"
recipients = [("Recipient 1", "recipient1@example.com"), ("Recipient 2", "recipient2@example.com")]
body = "This is a fake message."
start_date = datetime(2023, 5, 28, 9, 0, 0)  # Example start date: May 28, 2023, 9:00 AM
end_date = datetime(2023, 6, 4, 18, 0, 0)  # Example end date: June 4, 2023, 6:00 PM
num_emails = 2  # Number of emails to generate

for i in range(num_emails):
  #  sender = generate_random_name()
    sender ="Anthoine Préfontaine"
    random_date = generate_random_date(start_date, end_date)
    create_fake_msg(subject, sender, recipients, body, random_date)
