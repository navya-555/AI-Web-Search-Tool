# AI-Web-Search-Tool
The AI Web Search Tool is a smart search companion that utilizes web scraping and generative AI to analyze and summarize content from various sources based on user queries. It combines results from multiple websites to provide a concise output.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    streamlit run application.py
    ```

## Usage

1. Set Up Your Google API Key: Make sure you have a valid Google API key to access the generative AI model.

2. Enter your Google API key.
     
3. Input your search query.

4. Click the "Search" button to get analyzed results.

## Features
- Web scraping from DuckDuckGo to gather content from the top search results.
- Analysis of the gathered content using a generative AI model (Google Gemini).
- User-friendly interface built with Streamlit for easy interaction.

## Workflow

1. **User Input**
   - The user enters a search query and their Google API key into the Streamlit interface.

2. **API Key Validation**
   - The application checks if the provided Google API key is valid. If the key is valid, it configures the generative AI model for use.

3. **Web Scraping**
   - Upon clicking the "Search" button, the `process_query` function is triggered.
   - This function calls the `scrape_text` function from `utils/scrape.py`.
   - The `scrape_text` function uses the DuckDuckGo Search API to perform a search with the user’s query.
   - For each result, it makes an HTTP request to fetch the webpage content and uses BeautifulSoup to extract the text from the HTML.

4. **Content Analysis**
   - The scraped text content is passed to the `analyze_reviews_with_gemini` function in `utils/search.py`.
   - This function creates a prompt combining the query and the content from the different websites.
   - It then uses the generative AI model to analyze and summarize the gathered content.
  
5. **User Interface**
  - Built using Streamlit, providing an interactive interface for users to input their queries and view results.
  - Handles API key input securely and manages error handling.

## Link
https://questai.streamlit.app/
