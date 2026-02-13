import re

def validate_url(url):
    # simple regex to check URL
    pattern = r'^(http|https)://'
    return re.match(pattern, url) is not None
