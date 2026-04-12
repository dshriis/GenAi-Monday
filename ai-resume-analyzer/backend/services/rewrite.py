from openai import OpenAI
client = OpenAI()

def rewrite_resume(resume, job):
    prompt = f"Rewrite resume for job:\n{resume}\n{job}"
    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )
    return res.choices[0].message.content
