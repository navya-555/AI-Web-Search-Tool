import pandas as pd
from duckduckgo_search import DDGS

def scrape(query):
    results = DDGS().text(
        keywords=query,
        region="in-en",
        safesearch="off",
        backend="api",
        max_results=4
    )
    results_df=pd.DataFrame(results)
    return results_df

search_query = input()
res=scrape(search_query)
print(res)