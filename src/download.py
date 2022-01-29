import requests

FILES = [
    "UnicodeData.txt",
    "PropertyAliases.txt",
    "PropertyValueAliases.txt",
]

DATA_DIR = "data"

UCD_URL = "https://www.unicode.org/Public/14.0.0/ucd"

def all():
    for filename in FILES:
        path = "{}/{}".format(DATA_DIR, filename)
        with open(path, "w") as f:
            url = "{}/{}".format(UCD_URL, filename)
            response = requests.get(url)
            f.write(response.text)

if __name__ == "__main__":
    all()
