import requests
from bs4 import BeautifulSoup


def fetch_published_google_doc(url):
    """
    Fetches the raw HTML content of a published Google Doc.
    """
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to download document. Status code: {response.status_code}")
        return None
    return response.text


def extract_text_from_html(html):
    """
    Parses HTML and extracts plain text from paragraphs, headers, and list items inside the main content div.
    """
    soup = BeautifulSoup(html, "html.parser")
    content_div = soup.find("div", id="contents")
    if not content_div:
        print("Content div not found in the published document.")
        return None

    elements = content_div.find_all(["p", "h1", "h2", "h3", "li"])
    return [el.get_text(strip=True) for el in elements]


def parse_character_data(lines):
    """
    Parses the extracted lines into a list of characters with coordinates.
    Assumes each character entry is 3 lines: x, char, y (starting after a 5-line header).
    Skips incomplete or malformed entries.
    """
    characters = []
    for i in range(5, len(lines), 3):  # Skip the first 5 lines (assumed header)
        try:
            x = int(lines[i])
            char = lines[i + 1]
            y = int(lines[i + 2])
            characters.append({'x': x, 'y': y, 'char': char})
        except (IndexError, ValueError) as e:
            # print(f"Skipping malformed entry at lines[{i}:{i + 3}]: {e}")
            continue
    return characters


def get_grid_size(characters):
    """
    Determines the size of the grid needed to hold all characters.
    """
    max_x = max(c['x'] for c in characters)
    max_y = max(c['y'] for c in characters)
    return max_x + 1, max_y + 1  # +1 to account for zero-based indexing


def build_character_grid(characters, width, height):
    """
    Builds a 2D grid of the given dimensions and places characters at the correct coordinates.
    """
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    for c in characters:
        grid[c['y']][c['x']] = c['char']
    return grid


def print_grid(grid):
    """
    Prints the grid upside-down so that y=0 appears at the bottom.
    """
    for row in reversed(grid):
        print(''.join(row))


def main(google_doc_url):
    html = fetch_published_google_doc(google_doc_url)
    if not html:
        return

    lines = extract_text_from_html(html)
    if not lines:
        return

    characters = parse_character_data(lines)
    width, height = get_grid_size(characters)
    grid = build_character_grid(characters, width, height)
    print_grid(grid)


if __name__ == "__main__":
    main(
        "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
    )
