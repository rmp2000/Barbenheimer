import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.boxofficemojo.com/title/tt15398776/' #To scrap the barbie table use "https://www.boxofficemojo.com/title/tt1517268/" as the url
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find_all('table',class_='a-bordered a-horizontal-stripes a-size-base-plus')
table1=soup.find_all('table',class_='a-bordered a-horizontal-stripes a-size-base-plus')[0]

headers = [] #create the headers for the Dataframe using the html tag <th>
for i in table1.find_all("th"):
 title = i.text.strip()
 headers.append(title)

dt = pd.DataFrame(columns = headers)

for tab in table: #The web contains multiple tables, we iterate every single one 
    scrap_tables(tab)

def scrap_tables(table1):  #Using the tags <tr> and <td> we locate the data and create the rows of our dataframe
    for i in table1.find_all("tr")[1:]:
     row_data = i.find_all("td")
     row = [j.text for j in row_data]
     length = len(dt)
     dt.loc[length] = row

dt.head()
dt.to_excel("Oppenheimer_box_ofice.xlsx") #Transform the data in an excel spreadsheet
