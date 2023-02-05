import camelot
# df = camelot.read_pdf('Vijaya.pdf', pages='1',table_regions=["53,653,540,151"])
# df.export('Vijaya/X.csv', f='csv')

# df = camelot.read_pdf('Vijaya.pdf', pages='2-4',table_regions=["53,706,547,159"])
# df.export('Vijaya/X.csv', f='csv')

# df = camelot.read_pdf('Vijaya.pdf', pages='5',table_regions=["51,710,547,663"])
# df.export('Vijaya/X.csv', f='csv')

df = camelot.read_pdf('Vijaya_removed.pdf', pages='2',table_regions=["53,706,547,159"])
df.export('acc/X.csv', f='csv')

df = camelot.read_pdf('Vijaya_removed.pdf', pages='2')
df.export('acc/Y.csv', f='csv')

# df = camelot.read_pdf('acc.pdf', pages='2-66',table_regions=["12,738,586,30"])
# df.export('acc/X.csv', f='csv')

# df = camelot.read_pdf('acc500.pdf', flavor = 'stream',edge_col=500)
# df.export('acc500/X.csv', f='csv')