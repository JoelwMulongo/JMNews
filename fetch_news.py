import os
import requests
import json

# Get API Key from GitHub Secrets
API_KEY = os.getenv("NEWS_API_KEY")

TECH_NEWS_URL = f"https://newsapi.org/v2/top-headlines?category=technology&language=en&apiKey={API_KEY}"

def fetch_news():
    if not API_KEY:
        print("Error: Missing API key")
        return

    response = requests.get(TECH_NEWS_URL)
    news_data = response.json().get("articles", [])[:4]  # Get top 4 tech news

    news_list = []
    for article in news_data:
        news_list.append({
            "title": article["title"],
            "description": article["description"] or "No description available.",
            "url": article["url"],
            "image": article["urlToImage"] or "https://via.placeholder.com/600"  # Use placeholder if no image
        })

    os.makedirs("data", exist_ok=True)

    with open("data/news.json", "w") as file:
        json.dump(news_list, file, indent=4)

if __name__ == "__main__":
    fetch_news()
