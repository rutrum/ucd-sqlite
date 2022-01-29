data_dir := 'data'
out_dir := 'target'

default: construct

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

clean:
    rm {{data_dir}}/*
    rm {{out_dir}}/*
