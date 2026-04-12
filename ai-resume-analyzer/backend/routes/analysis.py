from fastapi import APIRouter
from services import preprocess, extractor, skill_gap, scorer, ai_suggestions, advanced_ai, rewrite, diff
from utils.embeddings import similarity

router = APIRouter()

@router.post("/analyze")
def analyze(data: dict):
    resume = data["resume"]
    job = data["job"]

    clean = preprocess.clean_text(resume)
    skills = extractor.extract_skills(clean)

    match = similarity(clean, job)

    required = ["python", "ml", "sql"]
    missing = skill_gap.missing_skills(skills, required)

    score_val = scorer.score(skills)

    ai_data = advanced_ai.advanced_analysis(resume, job)
    suggestions = ai_suggestions.get_suggestions(resume, job)
    rewritten = rewrite.rewrite_resume(resume, job)
    diff_html = diff.get_diff(resume, rewritten)

    return {
        "match": match,
        "skills": skills,
        "missing": missing,
        "score": score_val,
        "ai_analysis": ai_data,
        "suggestions": suggestions,
        "rewritten_resume": rewritten,
        "diff": diff_html
    }
