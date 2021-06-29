import urllib.request
import urllib.parse
import requests
from bs4 import BeautifulSoup

url = 'http://www.ssa.gov/cgi-bin/popularnames.cgi'

start_yr = 1880
end_yr = 2020

for year in range (end_yr, end_yr + 1):
    params = {
        'top'  : '100',
        'year' : str(year)
        }

    # Not working
    post_args = urllib.parse.urlencode(params)
    post_args = post_args.encode('UTF-8')
    page = urllib.request.urlopen(url, post_args)

    # Also not working
    # encoded = urllib.parse.urlencode(params)
    # encoded = encoded.encode('UTF-8')
    #
    # pg_request = urllib.request.Request(url, encoded)
    # page = urllib.request.urlopen(pg_request).read().decode('UTF-8', 'ignore')

    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find("table", {"width":"72%"})
    for row in table.findAll("tr", {"align":"right"}):
        cells = row.findAll("td")
        if len(cells) == 5:
            rank = cells[0].find(text = True)
            male = cells[1].find(text = True)
            female = cells[3].find(text = True)
            print(rank, male, female)
        elif len(cells) == 3:
            ank = cells[0].find(text = True)
            male = cells[1].find(text = True)
            female = cells[2].find(text = True)
            print(rank, male, female)

#
#     soup = BeautifulSoup(page)
#     table = soup.find("table", {"width":"48%"})
#
#     for row in table.findAll("tr", {"align":"right"}):
#         cells = row.findAll("td")
#         if len(cells) == 3:
#             rank = cells[0].find(text = True)
#             male = cells[1].find(text = True)
#             female = cells[2].find(text = True)
#             print(rank, male, female)

# page = requests.get(url)
#
# soup = BeautifulSoup(page.content, 'html.parser')
# table = soup.find("table", {"width":"72%"})
# for row in table.findAll("tr", {"align":"right"}):
#     cells = row.findAll("td")
#     if len(cells) == 5:
#         rank = cells[0].find(text = True)
#         male = cells[1].find(text = True)
#         female = cells[3].find(text = True)
#         print(rank, male, female)
#     elif len(cells) == 3:
#         ank = cells[0].find(text = True)
#         male = cells[1].find(text = True)
#         female = cells[2].find(text = True)
#         print(rank, male, female)
