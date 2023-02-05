# import libraries
import os
import PyPDF2
import pandas as pd
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from datetime import datetime

# set `<your-endpoint>` and `<your-key>` variables with the values from the Azure portal
# endpoint = "https://parser-statements-prod.cognitiveservices.azure.com/"
# key = "aead8ba83eca4dfc9c59c5e9c32fc159"

key = "a175f08fddf345f59b3f00370d5d11e6"
endpoint = "https://parser-statements.cognitiveservices.azure.com/"

def get_page_count(file):
    readpdf = PyPDF2.PdfReader(file)
    count = len(readpdf.pages)
    return count

def parse_pdf_statements_azure(file_path):

    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    with open(file_path, "rb") as f:
        poller = document_analysis_client.begin_analyze_document(
            "prebuilt-layout", document=f, pages="1-"+str(get_page_count(file_path))
        )
    result = poller.result()

    df = format_output_to_dataframe(result)

    return df


def format_output_to_dataframe(result):
    dict_tmp = {}
    flag = True
    header_flag = True

    for table_idx, table in enumerate(result.tables):
        
        if table.row_count>5:
            print(
                "Table # {} has {} rows and {} columns".format(
                table_idx, table.row_count, table.column_count
                )
            )
            for cell in table.cells:
                #print(cell.kind)
                dict_tmp[cell.column_index] = cell.content
                #dict_tmp[cell.column_index+1] = cell.kind 
                if cell.column_index+1==table.column_count:
                    if cell.kind=="columnHeader" and header_flag:
                        if flag:
                            df = pd.DataFrame([dict_tmp])
                            dict_tmp = {}
                            flag = False
                        else:
                            df = pd.concat([df, pd.DataFrame([dict_tmp])]).reset_index(drop=True)
                            dict_tmp = {}
                        header_flag = False
                    elif not cell.kind=="columnHeader":
                        if flag:
                            df = pd.DataFrame([dict_tmp])
                            dict_tmp = {}
                            flag = False
                        else:
                            df = pd.concat([df, pd.DataFrame([dict_tmp])]).reset_index(drop=True)
                            dict_tmp = {}
                        
    #df = df.dropna(axis=0,inplace=False).reset_index(drop=True)
    return df