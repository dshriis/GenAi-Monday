import json
def load_skills():
    return json.load(open("data/skills.json"))
def extract_skills(text):
    return [s for s in load_skills() if s.lower() in text]
