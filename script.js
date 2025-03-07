document.addEventListener("DOMContentLoaded", function () {
    const dateElement = document.getElementById("current-date");
    const today = new Date();
    dateElement.textContent = today.toDateString();

    fetch("data/news.json")
        .then(response => response.json())
        .then(data => {
            const newsContainer = document.getElementById("news-container");
            newsContainer.innerHTML = "";

            data.articles.slice(0, 7).forEach(article => {
                const newsItem = document.createElement("article");
                newsItem.innerHTML = `
                    <img src="${article.image}" alt="News Image">
                    <h2>${article.title}</h2>
                    <p>${article.description}</p>
                    <a href="${article.url}" target="_blank">Read More</a>
                `;
                newsContainer.appendChild(newsItem);
            });
        })
        .catch(error => console.error("Error fetching news:", error));
});
