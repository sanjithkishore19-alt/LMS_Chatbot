import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import requests
from bs4 import BeautifulSoup

# Create the FastAPI application
app = FastAPI()

# Mount the frontend directory to serve static files
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Web Scraping Logic
def scrape_website(url):
    """
    Fetches a webpage and extracts its title and a summary of content.
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Get the title
        title = soup.title.string if soup.title else "No Title Found"
        
        # Get the first few paragraphs for a summary
        paragraphs = [p.get_text() for p in soup.find_all('p')[:3]]
        summary = "\n".join(paragraphs).strip()
        
        if not summary:
            # If no paragraphs, try to find text from the body
            text_content = soup.get_text().strip()
            summary = text_content[:500] + "..." if len(text_content) > 500 else text_content
            
        return f"Scraped from {url}:\n\nTitle: {title}\n\nSummary:\n{summary}"

    except requests.exceptions.RequestException as e:
        return f"Error: Could not access the website. Please check the URL and your internet connection. ({e})"

# API Endpoints
@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    with open("frontend/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    user_message = data.get("message", "").lower()

    # Simple, rule-based logic to decide what to do
    response_text = "I'm sorry, I can only provide information from a specific website. Try asking me about 'news' or 'tech'."
    
    # Example: If the user asks about 'news', scrape a news website
    if "news" in user_message:
        url = "https://www.bbc.com/news"
        response_text = scrape_website(url)
    elif "tech" in user_message:
        url = "https://www.theverge.com"
        response_text = scrape_website(url)
    elif "hello" in user_message or "hi" in user_message:
        response_text = "Hello! I am a simple web scraping chatbot. Try asking me about 'news' or 'tech'."
        
    return {"response": response_text}
