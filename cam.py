import camelot

tables = camelot.read_pdf('foo.pdf')

tables

tables.export('foo.csv', f='csv', compress=True)

tables[0]

tables[0].parsing_report
{
    'accuracy': 99.02,
    'whitespace': 12.24,
    'order': 1,
    'page': 1
}

tables[0].to_csv('foo.csv') # to_json, to_excel, to_html, to_markdown, to_sqlite

tables[0].df
