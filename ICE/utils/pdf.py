import pdfkit
import json
from flask import Flask, send_file, request
def generate_pdf_from_html(html_string:str) -> bool:
    """Generates pdf from html string 

    Args:
        html_string (str): 

    Returns:
        bool: Status of conversion True | False
    """
    try:
        pdfkit.from_string(html_string,'report.pdf')
    except:
        return False
    return True