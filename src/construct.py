# builds the sqlite3 database

DB_PATH = "target/unicode.db"

import sqlite3
import property_value_aliases

def construct():
    db = sqlite3.connect(":memory:")
    unicode_data_table(db)

    property_value_aliases.construct(db)

    write_db(db)
    db.close()

def write_db(db):
    write_db = sqlite3.connect(DB_PATH)
    db.backup(write_db)
    write_db.close()

def unicode_data_table(db):

    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE UnicodeData(
            Code_Point INTEGER PRIMARY KEY,
            Name TEXT,
            General_Category TEXT,
            Canonical_Combining_Class TEXT,
            Bidi_Class TEXT,
            Decomposition_Type TEXT,
            Decomposition_Mapping TEXT,
            Numeric_Type TEXT,
            Numeric_Value TEXT,
            Bidi_Mirrored TEXT,
            Unicode_1_Name TEXT,
            ISO_Comment TEXT,
            Simple_Uppercase_Mapping TEXT,
            Simple_Lowercase_Mapping TEXT,
            Simple_Titlecase_Mapping TEXT
        )
    ''')

    insert_query = '''
        INSERT INTO UnicodeData
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''

    with open("data/UnicodeData.txt") as f:
        records = [
            map_line(line)
            for line in f
        ]

    cursor.executemany(insert_query, records)
    db.commit()

def map_line(line):
    vals = line.strip().split(";")
    vals[0] = int(vals[0], 16)
    return tuple(vals)


if __name__ == "__main__":
    construct()
