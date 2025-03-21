import re



def count_words(text: str):
    words = text.split()
    return len(words)


def check_link(text):
    url_pattern = r'https?://[^\s/$.?#].[^\s]*'
    
    match = re.search(url_pattern, text)
    
    if match:
        return match.group(0)
    return None