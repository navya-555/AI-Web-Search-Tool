from utils.scrape import scrape_text
from utils.search import analyze_reviews_with_gemini

def process_query(query,model):
    content=scrape_text(query)
    output=analyze_reviews_with_gemini(query,content[0],content[1],content[2],content[3],model)
    return output
