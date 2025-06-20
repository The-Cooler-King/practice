import requests
from bs4 import BeautifulSoup

def extract_plain_text_from_google_doc(google_doc_url):
    # Download the document content
    response = requests.get(google_doc_url)
    if response.status_code != 200:
        print(f"Download failed. Status code: {response.status_code}")
        return
    return response.text


def parse_html(response_text):
    soup = BeautifulSoup(response_text, "html.parser")
    content_div = soup.find("div", id="contents")
    if content_div:
        paragraphs = content_div.find_all(["p", "h1", "h2", "h3", "li"])
        doc_text = "\n".join(p.get_text(strip=True) for p in paragraphs)
        return doc_text
    else:
        print("Couldn't find content div in the published document.")


def structure_output(parsed_text):
    rows = parsed_text.strip().splitlines()
    structured = []

    for i in range(5, len(rows), 3):  # skip headers
        x = int(rows[i])
        char = rows[i + 1]
        y = int(rows[i + 2])
        structured.append({'x': x, 'y': y, 'char': char})

    return structured


def determine_grid_dimensions(character_list):
    max_x = 0
    max_y = 0

    for character in character_list:
        max_x = max(character['x'], max_x)
        max_y = max(character['y'], max_y)

    return max_x, max_y


def construct_grid(character_list, max_x, max_y):
    # Initialize grid with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Place characters into the grid
    for character in character_list:
        y = character["y"]
        x = character["x"]
        char = character["char"]
        print("------------")
        print(f"x: {x}")
        print(f"y: {y}")
        print(f"char: {char}")
        grid[y][x] = char
        print(grid)

    # Print the grid
    for row in reversed(grid):
        print(''.join(row))


def main(google_doc_url):
    # google_doc_url = convert_google_doc_url_to_export_format(google_doc_url)
    response = extract_plain_text_from_google_doc(google_doc_url)
    parsed_response = parse_html(response_text=response)
    structured_output = structure_output(parsed_text=parsed_response)
    max_x, max_y = determine_grid_dimensions(structured_output)
    construct_grid(character_list=structured_output,
                   max_x=max_x,
                   max_y=max_y)


main(
    "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub")

