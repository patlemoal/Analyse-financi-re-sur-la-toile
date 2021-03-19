import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Nasdaq_Composite"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

table = soup.find('table')

cn = table.findAll('th')
column_names = [col.text.strip() for col in cn]

print(column_names)

table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    print([ele for ele in cols if ele])