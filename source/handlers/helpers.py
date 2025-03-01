import re



def count_words(text: str):
    words = text.split()
    return len(words)


def check_link(text):
    url_pattern = r'^http[s]?://\S+$'
    return re.match(url_pattern, text, re.IGNORECASE) is not None