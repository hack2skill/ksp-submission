import tabula

# Read pdf into a list of DataFrame
#dfs = tabula.read_pdf("HDFC.pdf", pages='all')
#print(dfs)

# Read remote pdf into a list of DataFrame
#dfs2 = tabula.read_pdf("https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf")

# convert PDF into CSV
#tabula.convert_into("HDFC.pdf", "HDFC.csv", output_format="csv", pages='all')

# convert all PDFs in a directory
tabula.convert_into_by_batch("pdfs", output_format='csv', pages='all')
