from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def similarity(t1,t2):
    e1=model.encode([t1])
    e2=model.encode([t2])
    return float(round(cosine_similarity(e1,e2)[0][0]*100,2))
