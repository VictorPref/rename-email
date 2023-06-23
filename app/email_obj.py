from email.header import decode_header


class Email:
    def __init__(self, sender_name, sender_email ,recipient_name, recipient_email ,date ,extension):
        self.sender_name = sender_name
        self.sender_email = sender_email
        self.recipient_name = recipient_name
        self.recipient_email = recipient_email
        self.date = date
        self.extension = extension

def get_name_or_email(name,email):
    if name:
        return decode_header_value(name)
    else:
        return email

def filter_email(email,name,filter_name):
    if email in filter_name:
        return filter_name.get(email)
    else:
         return clean_string_name(get_name_or_email(name, email))
        
def decode_header_value(value):
    decoded_value = []
    for part, encoding in decode_header(value):
        if isinstance(part, bytes):
            decoded_value.append(part.decode(encoding or "utf-8", errors="ignore"))
        else:
            decoded_value.append(part)
    return "".join(decoded_value)
    
def clean_string_name(name):
    return name.replace("'", "")