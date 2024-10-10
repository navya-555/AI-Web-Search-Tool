
def analyze_reviews_with_gemini(query,text1,text2,text3,text4,model):
    prompt = f"""
    {query} this is my query and i want an output from you after analyzing, summarizing and combining the relative answer to the query from 4 different websites.
     First website gave {text1}, second website gave {text2}, third website gave {text3}, fourth website gave {text4}.
    """
    
    response = model.generate_content([prompt,query,text1,text2,text3,text4])
    output = response.text.strip()
    return output

