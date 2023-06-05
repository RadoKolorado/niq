import requests
from bs4 import BeautifulSoup
import csv

try:

   ## Andrychów

    url = "https://infopasazer.intercity.pl/?p=station&id=76273"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')

    data = []

    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)

    with open('Andrychów.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Numer pociagu', 'Przewoznik', 'Data', 'Relacja', 'Przyjazd planowo', 'Opoznienie'])
        for row in data:
            writer.writerow(row)

except (AttributeError, requests.exceptions.Timeout):
    pass

try:

   ## Anieliny

    url = "http://infopasazer.intercity.pl/?p=station&id=18242"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')

    data = []

    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)

    with open('Anieliny.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Numer pociagu', 'Przewoznik', 'Data', 'Relacja', 'Przyjazd planowo', 'Opoznienie'])
        for row in data:
            writer.writerow(row)

except (AttributeError, requests.exceptions.Timeout):
    pass
            
try:

   ## Babimost

    url = "http://infopasazer.intercity.pl/?p=station&id=26161"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')

    data = []

    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)

    with open('Babimost.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Numer pociagu', 'Przewoznik', 'Data', 'Relacja', 'Przyjazd planowo', 'Opoznienie'])
        for row in data:
            writer.writerow(row)

except (AttributeError, requests.exceptions.Timeout):
    pass