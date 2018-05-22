

# Complete the function below.
import re

def find_phone_number(text):
    allFound = re.findall(r'[0-9]{3}-[0-9]{3}-[0-9]{4}|\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}', text)

    if (allFound):
        return allFound[0]
    else:
        return "NONE"
