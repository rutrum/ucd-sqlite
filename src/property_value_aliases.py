# Methods for constructing tables based of the contents of PropertyValueAliases.txt

import re
import io
import csv

def construct(db):

    txt = open("data/PropertyValueAliases.txt").read()

    # skip the header
    start = txt.find("\n\n")
    txt = txt[start:].strip()

    # split on titles, and not '# @missing...'
    header_re = re.compile(r"(^# [^@].*)", re.MULTILINE)
    sections = header_re.split(txt)
    sections = [ section for section in sections if section ]

    table_name = None

    for i, section in enumerate(sections):
        section = section.strip()
        if i % 2 == 0:
            table_name = section.strip(" #").replace(" ", "_").replace("(", "").replace(")", "")
        else:
            rows = []
            with io.StringIO(section) as f:
                reader = csv.reader(f, delimiter=';')
                for row in reader:
                    row = [
                        cell.strip() 
                        for cell in row 
                    ]
                    if not row[0].startswith("#"):
                        rows.append(row)

            if rows:
                db.execute("""
                    CREATE TABLE {}(
                        Short TEXT,
                        Long TEXT
                    )
                """.format(table_name))
