import pandas as pd
from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup

def scrape(query):
    results = DDGS().text(
        keywords=query,
        region="in-en",
        safesearch="off",
        backend="api",
        max_results=4
    )
    results_df=pd.DataFrame(results)
    contents=[]
    for i in range(len(results_df)):
        url=results_df['href'][i]
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')   
        text_content = soup.get_text(separator='\n', strip=True)
        contents.append(text_content)
    return contents

search_query = input()
res=scrape(search_query)
print(res)