import requests
from bs4 import BeautifulSoup
import csv
import re

# Website URL
url = "https://books.toscrape.com/"

try:
    # Send request to the website
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all book items
    books = soup.find_all("article", class_="product_pod")

    # Create CSV file
    with open(
        "output.csv",
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        writer = csv.writer(file)

        # CSV header
        writer.writerow(["Title", "Price"])

        # Extract book information
        for book in books:
            title = book.h3.a.get("title", "").strip()

            # Get price text
            price_text = book.find(
                "p",
                class_="price_color"
            ).get_text(strip=True)

            # Extract only the numeric price
            match = re.search(r"\d+\.\d+", price_text)

            if match:
                price = f"£{match.group()}"
            else:
                price = price_text

            # Write data to CSV
            writer.writerow([title, price])

    print("Data scraping completed successfully.")
    print(f"Total books scraped: {len(books)}")
    print("Data saved to output.csv")

except requests.exceptions.RequestException as error:
    print("Error while accessing the website:", error)

except Exception as error:
    print("An unexpected error occurred:", error)