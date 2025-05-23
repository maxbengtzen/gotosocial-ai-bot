import re

URL_REGEX = re.compile(r'https?://\S+')

def extract_url(content):
    match = URL_REGEX.search(content)
    return match.group(0) if match else None