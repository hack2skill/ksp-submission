import os
from bs4 import BeautifulSoup
import pandas as pd

def html_parser(file_path):
    
    with open(file_path, encoding="utf-8") as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    # find the table
    table = soup.find('pre')

    # extract the data from the table
    rows = table.text.strip().split('\n')
    flag = True
    tmp_dict = {}
    df = pd.DataFrame(columns=["TXD Date", "Description", "TO", "Value Date", "Debit/Credit", "Balance"])
    for row in rows:
        cells = row.strip().split()

        if len(cells)>8:
            continue
        elif len(cells)>=6:
            if len(tmp_dict)>0:
                df = df.append(tmp_dict, ignore_index=True)
                tmp_dict = {}
            else:
                tmp_dict["TXD Date"] = cells[0]
                tmp_dict["Description"] = " ".join(cells[1:-4])
                tmp_dict["TO"] = cells[-4]
                tmp_dict["Value Date"] = cells[-3]
                tmp_dict['Debit/Credit'] = cells[-2]
                tmp_dict['Balance'] = cells[-1]
        elif len(cells)<6:
            if len(tmp_dict)>0:
                tmp_dict["Description"] = tmp_dict["Description"]+ " ".join(cells)
    
    return df
