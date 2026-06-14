from newspaper import Article

def extract_article(url):
    try:
        article = Article(url)

        article.download()
        article.parse()

        return {
            "title": article.title,
            "text": article.text,
            "top_image": article.top_image,
            "authors": article.authors
        }

    except Exception as e:
        print(f"Extraction error: {e}")
        return None


if __name__ == "__main__":
    test_url = "https://www.bbc.com/news"

    data = extract_article(test_url)

    print(data)