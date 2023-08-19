data_dir := "data"
out_dir := "target"
db_path := "target/unicode.db"

default: construct

construct:
    python3 src/construct.py

download:
    python3 src/download.py

tree:
    tree -I __pycache__

schema:
    sqlite3 {{db_path}} ".schema"

head:
    sqlite3 {{db_path}} "select * from UnicodeData LIMIT 10"

clean:
    rm {{data_dir}}/*
    rm {{out_dir}}/*
