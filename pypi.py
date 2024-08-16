from bs4 import BeautifulSoup
import requests
import os

def pypiurl(key: str, numb: int):
    try:
        res = requests.get(f'https://pypi.org/search/?q={key}')
        soup = BeautifulSoup(res.text, 'html.parser')
        link = soup.find_all('a', class_="package-snippet")[numb]
        return f"https://pypi.org{link["href"]}"
    except:
        return "Error."
        
def pypititle(key: str, numb: int):
    try:
        res = requests.get(f'https://pypi.org/search/?q={key}')
        soup = BeautifulSoup(res.text, 'html.parser')
        title = soup.find_all('span', class_="package-snippet__name")[numb]
        return f"{title.get_text()}"
    except:
        return "Error."