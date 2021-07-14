import re

email_regex = "^[\w\.\+\-\\]+\@[\w]+\.[a-z]{2,6}$"

def validate_email(mail: str) -> bool:
    if len(mail) == 0:
        return False

    if not re.match(email_regex, mail):
        return False
    else:
        return True