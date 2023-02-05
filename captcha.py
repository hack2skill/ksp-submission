from PIL import Image
import pytesseract
import cv2
import os


def get_captcha(imag_path):

    text = pytesseract.image_to_string(Image.open(imag_path))
    # os.remove(imag_path)
    return text.replace("\n\f","").strip()
