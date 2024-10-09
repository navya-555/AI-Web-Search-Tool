from scrape import scrape_text
from search import analyze_reviews_with_gemini
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API')

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
gemini_model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def process(query,model):
    content=scrape_text(query)
    output=analyze_reviews_with_gemini(query,content[0],content[1],content[2],content[3],model)
    return output

res=process('what is ml',gemini_model)
print(res)