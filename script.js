document.addEventListener("DOMContentLoaded", async () => {
    document.getElementById("date").textContent = new Date().toDateString();
    
    const response = await fetch("data/news.json");
    const newsData = await response.json();
    
    const newsContainer = document.getElementById("news-container");
    newsContainer.innerHTML = "";
    
    newsData.forEach(news => {
        const newsItem = document.createElement("div");
        newsItem.className = "news-item";
        newsItem.innerHTML = `<h3>${news.title}</h3><p>${news.description}</p><a href="${news.url}" target="_blank">Read more</a>`;
        newsContainer.appendChild(newsItem);
    });
});
