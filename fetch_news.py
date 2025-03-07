import requests
import json
import os

API_KEY = os.getenv("NEWS_API_KEY")  # Use GitHub Secrets for API key
NEWS_URL = "https://newsapi.org/v2/top-headlines?category=technology&language=en&pageSize=6&apiKey=" + API_KEY

def fetch_news():
    response = requests.get(NEWS_URL)
    if response.status_code == 200:
        data = response.json()
        articles = [
            {
                "title": article["title"],
                "description": article["description"] or "No description available.",
                "url": article["url"],
                "image": article.get("urlToImage", "https://via.placeholder.com/300")  # Default image if none
            }
            for article in data.get("articles", [])[:6]  # Ensure only 6 articles
        ]

        os.makedirs("data", exist_ok=True)
        with open("data/news.json", "w") as file:
            json.dump({"articles": articles}, file, indent=4)

fetch_news()
