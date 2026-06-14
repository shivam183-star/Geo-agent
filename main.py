from news.fetcher import fetch_articles
from news.scorer import score_article
from ai.duplicate_checker import is_duplicate


MINIMUM_SCORE = 5


def run_news_pipeline():

    print("\nFetching latest articles...\n")

    articles = fetch_articles()

    print(f"Found {len(articles)} articles\n")

    important_count = 0

    for i, article in enumerate(articles[:15]):

        print("=" * 60)
        print(f"Processing Article {i+1}")

        title = article["title"]
        summary = article["summary"]

        score = score_article(title, summary)

        print(f"Title: {title}")
        print(f"Score: {score}")

        if score >= MINIMUM_SCORE:

            duplicate =  is_duplicate(title, summary)

            if duplicate:
                continue


            important_count += 1

            print("\nIMPORTANT ARTICLE DETECTED\n")

            print("Headline:")
            print(title)

            print("\nSummary:")
            print(summary)

            print("\n")

    print("=" * 60)
    print(f"\nImportant Articles Found: {important_count}")


if __name__ == "__main__":
    run_news_pipeline()