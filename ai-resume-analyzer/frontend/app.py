import streamlit as st, requests

st.title("🔥 AI Resume Analyzer FULL")

resume = st.file_uploader("Resume PDF")
job = st.file_uploader("Job PDF")

if st.button("Analyze"):
    r1 = requests.post("http://127.0.0.1:8000/upload", files={"file":resume})
    r2 = requests.post("http://127.0.0.1:8000/upload", files={"file":job})

    res = requests.post("http://127.0.0.1:8000/analyze",
        json={"resume":r1.json()["text"],"job":r2.json()["text"]})

    data = res.json()

    st.write("Match:",data["match"])
    st.write("Skills:",data["skills"])
    st.write("Missing:",data["missing"])
    st.write("Score:",data["score"])

    st.subheader("AI Suggestions")
    st.write(data["suggestions"])

    st.subheader("Rewritten Resume")
    st.text_area("",data["rewritten_resume"],height=300)

    st.subheader("Diff")
    st.markdown(data["diff"],unsafe_allow_html=True)
