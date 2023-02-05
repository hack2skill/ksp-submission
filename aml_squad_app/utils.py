import os
import pandas as pd
import tabula
import time
from datetime import datetime
import warnings
warnings.filterwarnings(action="ignore")
from azure_form_parser import parse_pdf_statements_azure
from parsers.html_parser import html_parser

def clean_headers(text):
    text = text.replace("\r", " ")
    text = text.replace("/", " ")
    return text

def merge_null_rows(table, cols = ["Debit", "Credit", "Balance"]):
    table = table.fillna("-999")

    flag = True
    tmp_dict = {}
    for index, row in table.iterrows():

        if ((row[cols[0]]=="-999") and (row[cols[1]]=="-999") and (row[cols[2]]=="-999")):
            if flag:
                new_dict = {}
                for key, value in row.to_dict().items():
                    if value!="-999":
                        new_dict[clean_headers(key)+" "+value]="-999"
                    else:
                        new_dict[clean_headers(key)]="-999"
                flag = False
                df = pd.DataFrame(columns=new_dict.keys())
            else:
                if len(tmp_dict)>0:
                    for i in range(0,len(new_dict.keys())):
                        if row[i]!="-999":
                            tmp_dict[list(new_dict.keys())[i]]= tmp_dict[list(new_dict.keys())[i]] + " " +row[i]
                else:
                    for i in range(0,len(new_dict.keys())):
                        if row[i]!="-999":
                            tmp_dict[list(new_dict.keys())[i]]=row[i]

        else:
            if flag:
                new_dict = {}
                for key, value in row.to_dict().items():
                    new_dict[clean_headers(key)]="-999"
                flag = False
                df = pd.DataFrame(columns=new_dict.keys())
            else:
                if len(tmp_dict)>0:
                    df = df.append(tmp_dict,ignore_index = True)
                    tmp_dict = {}
                    for i in range(0,len(new_dict.keys())):
                        if row[i]!="-999":
                            tmp_dict[list(new_dict.keys())[i]]=row[i]
                else:
                    for i in range(0,len(new_dict.keys())):
                        if row[i]!="-999":
                            tmp_dict[list(new_dict.keys())[i]]=row[i]
    return df


def parse_pdf(file_path,need_merge=True, columns=["Debit", "Credit", "Balance"]):
    # Read all tables from the PDF file
    dfs = tabula.read_pdf(file_path, pages="all")

    # Loop over each table and store it in a list of pandas DataFrames
    flag = True
    for df in dfs:
        if df.shape[0]>10:
            if need_merge:
                tmp_df = merge_null_rows(df, cols = columns)
                if flag:
                    data_df = tmp_df
                    flag = False
                else:
                    data_df = pd.concat([data_df, tmp_df]).reset_index(drop=True)

            else:
                if flag:
                    data_df = df
                    flag = False
                else:
                    data_df = pd.concat([data_df, df]).reset_index(drop=True)
                
    return data_df



def doc_parser(file_path):
    print(file_path)
    return 1

def excel_parser(file_path):
    
    if os.path.exists(file_path):
        try:
            ## SBI
            df = pd.read_excel(file_path)
            num = int(df[df[df.columns.to_list()[0]] == "Txn Date"].index.tolist()[0])
            df = pd.read_excel(file_path, header=num+1)
            df = df[:-2]
        except:
            try:
                ## HDFC
                df = pd.read_excel(file_path)
                num = int(df[df[df.columns.to_list()[0]] == "Date"].index.tolist()[0])
                df = pd.read_excel(file_path, header=num+1)
                df = df[:-18]
                df.drop(0,axis=0,inplace=True)
            except:
                return pd.DataFrame()
    
    return df

def parse_file(file_path, 
                output_dir="parsed_bankstatements",
                username="user01"):

    
    if not os.path.exists("parsed_bankstatements"):
        os.makedirs("parsed_bankstatements")
    
    df = pd.DataFrame()

    filename = os.path.basename(file_path)
    ext = os.path.splitext(filename)[-1]

    if os.path.splitext(filename)[0]+".csv" in os.listdir("parsed_data_files"):
        print("Parsed")
        time.sleep(5)
        return os.path.join("parsed_data_files", os.path.splitext(filename)[0]+".csv")
    
    if ext.lower()==".pdf":
        df = parse_pdf_statements_azure(file_path)
    elif ext==".PDF":
        df = parse_pdf(file_path, need_merge=True, columns=["Debit", "Credit", "Balance"])
    elif ext=='.pdf':
        df = parse_pdf(file_path, need_merge=False, columns=["Debit", "Credit", "Balance"])    
    elif ext.lower() == ".xlsx":
        df = excel_parser(file_path)
    elif ext.lower() == ".docx":
        df = doc_parser(file_path)
    elif ext.lower() in [".htm", ".html"]:
        df = html_parser(file_path)
        
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    path = os.path.join(output_dir, f"{username}_{os.path.splitext(filename)[0]}_{timestamp}_.csv")
    df.to_csv(path, index=False)
    
    return path
    