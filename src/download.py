import requests

UNICODE_DATA_URL = "https://www.unicode.org/Public/14.0.0/ucd/UnicodeData.txt"
UNICODE_DATA_PATH = "data/UnicodeData.txt"

def from_urls():
    with open(UNICODE_DATA_PATH, "w") as f:
        response = requests.get(UNICODE_DATA_URL)
        f.write(response.text)

if __name__ == "__main__":
    from_urls()
