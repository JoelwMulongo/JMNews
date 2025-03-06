import os
import requests
import json

# Get API Key from environment variables
API_KEY = os.getenv("NEWS_API_KEY")  

KENYA_NEWS_URL = f"https://newsapi.org/v2/top-headlines?country=ke&apiKey={API_KEY}"
WORLD_NEWS_URL = f"https://newsapi.org/v2/top-headlines?language=en&apiKey={API_KEY}"

def fetch_news():
    if not API_KEY:
        print("Error: Missing API key")
        return

    kenya_news = requests.get(KENYA_NEWS_URL).json().get("articles", [])[:2]
    world_news = requests.get(WORLD_NEWS_URL).json().get("articles", [])[:2]

    news_list = []
    for article in kenya_news + world_news:
        news_list.append({
            "title": article["title"],
            "description": article["description"] or "No description available.",
            "url": article["url"]
        })

    # Ensure the "data" folder exists
    os.makedirs("data", exist_ok=True)

    # Save news data
    with open("data/news.json", "w") as file:
        json.dump(news_list, file, indent=4)

if __name__ == "__main__":
    fetch_news()
