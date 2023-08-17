import settings
import openai
import requests
from bs4 import BeautifulSoup
import fitz

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import json, re

import PyPDF2
from PIL import Image
import pytesseract
import magic

import settings

from datetime import datetime

openai.api_key = settings.APIKEY

def list_files(folder_path):
    files = os.listdir(folder_path)
    files.sort()
    pippa_log(f'Data files in the given folder: {folder_path}')

    for file in files:
        print(file)


def pippa_log(log_message, log_type='info'):

    if log_type == 'debug':
        print("️🪲DEBUG: ", log_message)
    elif log_type == 'error':
        print("‼️Error: ", log_message)
    else:
        print("✏️INFO: ", log_message)


def list_openai_models():

    # List OpenAI models accessible via API

    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    print("Current Date and Time:", formatted_datetime)

    print("OpenAI models accessible via API")

    models = dict(openai.Model.list())
    current_datetime = datetime.now()

    for i in models['data']:
        if i['id'].startswith('gpt'):
            print(i['id'])


def read_url_body_content(url, hide_browser=False):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920x1080") # Set window size
        if hide_browser:
            chrome_options.add_argument("--headless")

        # Initialize the web driver (replace the path with the path to your chromedriver)
        # executable_path='/path/to/chromedriver': it defaults to '/usr/local/bin/chromedriver
        driver = webdriver.Chrome()

        # Open the URL
        driver.get(url)

        # Wait for the body tag to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        # Find the body tag and extract its text content
        body_tag = driver.find_element(By.TAG_NAME, 'body')
        body_content = body_tag.text

        # Close the web driver
        driver.quit()

        return ' '.join(body_content.split()) # Removing extra whitespaces
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_file_type(file_path):
    mime = magic.Magic(mime=True)
    mime_type = mime.from_file(file_path)
    return mime_type


def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def read_image_file(file_path):
    image = Image.open(file_path)
    if settings.KOREAN_OCR_ENABLED:
        text = pytesseract.image_to_string(image, lang='kor')
    else:
        text = pytesseract.image_to_string(image)
    return text


def read_pdf_file(file_path):

    if settings.KOREAN_OCR_ENABLED:
        pdf_document = fitz.open(file_path)
        full_text = ""

        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)
            image = page.get_pixmap()
            image_data = image.samples
            pil_image = Image.frombytes("RGB", [image.width, image.height], image_data)

            text = pytesseract.image_to_string(pil_image, lang='kor')
            full_text += text

        return full_text
    else:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
        return text


def read_file_content(file_path):
    """
    Read the content of the file according to the type.

    :param file_path: path of the file to read
    :type prompt: str
    :return: The content of the file
    :rtype: str
    :raises ValueError: Unsupported file type
    """

    if os.path.exists(file_path):

        file_type = get_file_type(file_path)

        if 'text' in file_type:
            content = read_text_file(file_path)
        elif 'image' in file_type:
            content = read_image_file(file_path)
        elif 'pdf' in file_type:
            content = read_pdf_file(file_path)
        else:
            pippa_log("Unsupported file type.", 'error')
            raise ValueError("Unsupported file type.")

        return content

    else:
        pippa_log(f"No such file:{file_path}", 'error')
        return ""


if __name__ == "__main__":
    pippa_log("module debugging: cwk_modules")
    list_openai_models()
    list_files(settings.DATA_FOLDER)
    content = read_url_body_content(settings.TEST_URL, hide_browser=True)
    if content:
        print(content)
    else:
        print("Failed to fetch the content from the URL.")
    content = read_file_content(settings.TEST_FILE)
    if content:
        print(content)
    else:
        print("Failed to fetch the content from the file.")

    content = read_file_content(settings.TEST_PDF)
    if content:
        print(content)
    else:
        print("Failed to fetch the content from the file.")

    content = read_file_content(settings.TEST_IMAGE)
    if content:
        print(content)
    else:
        print("Failed to fetch the content from the file.")