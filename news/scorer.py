KEYWORDS = {
    "war": 5,
    "military": 4,
    "missile": 5,
    "china": 3,
    "russia": 3,
    "india": 3,
    "taiwan": 4,
    "sanctions": 4,
    "nato": 4,
    "election": 3,
    "conflict": 5,
    "attack": 5,
    "usa": 5,
    "united states": 5,
    "palestine":4,
    "iran": 5,
    "israel": 5,
}


def score_article(text):
    score = 0

    text = text.lower()

    for keyword, points in KEYWORDS.items():
        if keyword in text:
            score += points

    return score


if __name__ == "__main__":
    sample = """
    China increased military drills near Taiwan amid rising regional tensions.
    """

    print(score_article(sample))