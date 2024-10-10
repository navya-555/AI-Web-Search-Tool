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
