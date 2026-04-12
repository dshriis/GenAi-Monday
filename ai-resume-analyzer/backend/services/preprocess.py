import re
def clean_text(t):
    return re.sub(r'\W+',' ',t.lower())
