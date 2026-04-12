from openai import OpenAI
import json
client = OpenAI()

def advanced_analysis(resume, job):
    prompt = f"Return JSON score for resume vs job: {resume} {job}"
    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )
    try:
        return json.loads(res.choices[0].message.content)
    except:
        return {"raw": res.choices[0].message.content}
