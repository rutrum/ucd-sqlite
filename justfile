default: tree

construct:
    python3 src/construct.py

download:
    python3 src/download.py

tree:
    tree

schema:
    sqlite3 out/unicode.db ".schema"

head:
    sqlite3 out/unicode.db "select * from UnicodeData LIMIT 10"
