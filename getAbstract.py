
import os
import xml.etree.ElementTree as ET
import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import glob

def get_abstract(url):
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        abstract_tag = soup.find('abstract')
        if abstract_tag:
            return abstract_tag.get_text()
    return ''
