from openai import OpenAI
client = OpenAI()

def get_suggestions(resume, job):
    prompt = f"Give improvement tips for this resume vs job:\n{resume}\n{job}"
    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )
    return res.choices[0].message.content
