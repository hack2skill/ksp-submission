import pandas as pd

workbook_url = 'HDFC.xlsx'

single_df =  pd.read_excel(workbook_url, sheet_name='HDFC')

single_df.head()

all_dfs = pd.read_excel(workbook_url, sheet_name=None)

type(all_dfs)

all_dfs.keys()


#all_dfs['Sheet1'].head()

#all_dfs['Sheet2'].head()

for sheet in all_dfs:
    print(f"{sheet} - {all_dfs[sheet].shape}")
    
df = pd.concat(all_dfs)
df.to_csv("alldata.csv")

df.shape



df.head()



print(pd.concat(pd.read_excel(workbook_url, sheet_name=None), ignore_index=True))


