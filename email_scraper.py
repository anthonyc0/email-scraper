import re
import requests

def extract_emails_from_url(url):
    response = requests.get(url)
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", response.text)
    return set(emails)

# Exemple d’utilisation
url = "https://example.com"
emails = extract_emails_from_url(url)
for email in emails:
    print(email)
