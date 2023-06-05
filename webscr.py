from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
import io

##  KOLEJE SLASKIE ----------------------------------------------------

opoznienia_ks = requests.get('https://www.kolejeslaskie.com/category/informacje/').text
soup = BeautifulSoup(opoznienia_ks, 'lxml')

ks_data = soup.findAll('div', class_ = 'row category-date')
ks_info = soup.findAll('div', class_ = 'col-sm-12 col-xl-12')
## print(ks_data)
## print(ks_info)

with open('kolejeslaskie.csv', 'a') as csv_file:
  writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
  writer.writerow(['Data','Szczegoly'])
  for col1,col2 in zip(ks_data, ks_info):
    writer.writerow([col1.get_text().strip(), col2.get_text().strip()])
    
## SKM WARSZAWA --------------------------------------------------------

opoznienia_skmw = requests.get('https://www.skm.warszawa.pl/aktualne-utrudnienia/', verify=False).text
soup = BeautifulSoup(opoznienia_skmw, 'lxml')

skmw_info = soup.find('div', class_ = 'col-xs-12 col-sm-12 col-md-8 content')

with open('skmwarszawa.csv', 'a') as csv_file:
  writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
  writer.writerow(['Szczegoly'])
  for col1 in tuple(skmw_info):
    writer.writerow([col1.get_text().strip()])
        
## PORTAL PASAZERA -------------------------------------------------------


## Warszawa Centralna
opoznienia_pp_wc = requests.get('https://portalpasazera.pl/Opoznienia?s=2&sid=19uLjuXEpMKSxJeSLtrGJmHyGWBdl8mSqzQDbVKD2S1ANVksYXqxAXcXDhV4EqaUm4zbDSSqU0SzydbcnffxIDJWA6gvERpbCSHRZ30FFz19OJnlscc2BVU46JLxQKm2nQt5').text
soup = BeautifulSoup(opoznienia_pp_wc, 'lxml')

data = soup.findAll('p', class_ = 'table-search-info__status')
pp_wc_info = soup.findAll('div', class_ = 'row delays-table__row abt-focusable')
pp_wc_szczegoly = soup.findAll('div', class_ = 'col-2 col-12--phone inline-left inline-center--phone')

with io.open('WarszawaCentralna.csv', 'a', encoding='utf-8') as csv_file:
  writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
  writer.writerow(data)
  writer.writerow(['1', '2'])
  for col1,col2 in zip(pp_wc_info, pp_wc_szczegoly):
    writer.writerow([col1.get_text().strip(),col2])