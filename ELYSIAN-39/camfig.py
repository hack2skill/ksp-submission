import camelot
tables = camelot.read_pdf('Vijaya.pdf')
camelot.plot(tables[0], kind='text').show()