import feedparser

RSS_FEEDS = [
    "https://feeds.bbci.co.uk/news/world/rss.xml",
    "https://www.aljazeera.com/xml/rss/all.xml",
    "https://www.reutersagency.com/feed/?best-topics=world&post_type=best"
]

def fetch_articles():
    articles = []

    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries:
            article = {
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "published": entry.get("published", ""),
                "summary": entry.get("summary", "")
            }

            articles.append(article)

    return articles


if __name__ == "__main__":
    articles = fetch_articles()

    for article in articles[:5]:
        print("\n")
        print(article["title"])
        print(article["link"])