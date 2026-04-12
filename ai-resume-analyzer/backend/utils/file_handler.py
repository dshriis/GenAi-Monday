import fitz
async def extract_text(file):
    content = await file.read()
    with open("temp.pdf","wb") as f:
        f.write(content)
    doc = fitz.open("temp.pdf")
    text=""
    for p in doc:
        text+=p.get_text()
    return text
