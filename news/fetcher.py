import requests
from bs4 import BeautifulSoup


RSS_FEEDS = [
    "https://feeds.bbci.co.uk/news/world/rss.xml",
    "https://www.aljazeera.com/xml/rss/all.xml"
]


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0"
    )
}


def fetch_articles():

    articles = []

    for feed_url in RSS_FEEDS:

        try:

            response = requests.get(
                feed_url,
                headers=HEADERS,
                timeout=10
            )

            soup = BeautifulSoup(
                response.content,
                "xml"
            )

            items = soup.find_all("item")

            for item in items:

                title = item.title.text if item.title else ""

                link = item.link.text if item.link else ""

                summary = ""

                if item.description:
                    summary = item.description.text

                article = {
                    "title": title,
                    "link": link,
                    "summary": summary
                }

                articles.append(article)

        except Exception as e:

            print(f"Feed error: {e}")

            continue

    return articles
