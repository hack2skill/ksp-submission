import requests
from typing import Dict
def get_url_to_enum_dict():
    return {
        "twitter.com": "TWITTER",
        "linkedin.com": "LINKEDIN",
        "instagram.com": "INSTAGRAM",
        "facebook.com": "FACEBOOK",
        "snapchat.com": "SNAPCHAT",
        "swiggy.com": "SWIGGY",
        "zomato.com": "ZOMATO",
        "phonepe.com": "PHONEPE",
        "pay.google.com": "GPAY",
        "paytm.com": "PAYTM",
        "amazon.in": "AMAZON",
        "amazon.com": "AMAZON",
        "flipkart.com": "FLIPKART",
        "myntra.com": "MYNTRA",
        "ajio.com": "AJIO",
        "uber.com": "UBER",
        "olacabs.com": "OLA"
    }


def check_if_whatsapp_exists(lnum:str)-> Dict:
    try:

        """Checks if the number has a whatsapp account

        Args:
            lnum (str): given number of the person ("8384852943")
        Returns:
            out (Dict): {'balance': 8, 'status': True, 'numberstatus': True, 'businessnumber': False}
        """
        out = requests.get(url="https://proweblook.com/api/v1/checkwanumber",params= {"number":lnum,"api_key":api_key})

        return out.json()['numberstatus']
    except Exception as e:
        return True