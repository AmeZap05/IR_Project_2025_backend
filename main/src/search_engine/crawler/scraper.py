"""
    Websites to be scraped:
    1. Open Library (BEST CHOICE for scraping or API)
    2. BookBrainz (Open Data, Easy to Scrape)
    3. One among:
        i.  Goodreads (Scrapable but tricky)
        ii. Fantastic Fiction
"""
import requests

BASE_URL = "https://openlibrary.org"


def search_books(query: str, limit: int = 5):
    """
    Uses the official Open Library search API (stable, JSON).
    """
    response = requests.get(f"{BASE_URL}/search.json", params={"q": query})
    response.raise_for_status()

    data = response.json()

    results = []
    for doc in data.get("docs", [])[:limit]:
        results.append({
            "title": doc.get("title"),
            "olid": doc.get("key").replace("/works/", "") if doc.get("key") else None,
            "author_name": doc.get("author_name", []),
            "first_publish_year": doc.get("first_publish_year"),
        })

    return results


def get_book_data(olid: str):
    """
    Get book/work details from the stable JSON API.
    """
    response = requests.get(f"{BASE_URL}/works/{olid}.json")
    response.raise_for_status()

    data = response.json()

    return {
        "olid": olid,
        "title": data.get("title"),
        "description": (
            data.get("description", {}).get("value")
            if isinstance(data.get("description"), dict)
            else data.get("description")
        ),
        "subjects": data.get("subjects", []),
        "covers": data.get("covers", []),
    }


if __name__ == "__main__":
    results = search_books("The Hobbit")
    print("Search results:", results)

    if results:
        book = get_book_data(results[0]["olid"])
        print("\nBook data:", book)

