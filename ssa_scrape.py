import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.ssa.gov/cgi-bin/popularnames.cgi'

start_yr = 2019
end_yr = 2020

with open('babynames.csv', 'w') as bncsv:
    csvwriter = csv.writer(bncsv)
    #csvwriter.writerow(['year', 'rank', 'males', 'percent_males', 'females', 'percent_females'])
    csvwriter.writerow(['year', 'gender', 'rank', 'name', 'percent'])

    for yr in range (start_yr, end_yr + 1):
        post_params = {'year': yr, 'top': 50, 'number': 'p'}
        response = requests.post(url, data=post_params)
        #print(response.content)
        soup = BeautifulSoup(response.content, 'html.parser')
        print("YEAR:", yr)
        table = soup.find("table", {"width":"72%"})
        for row in table.findAll("tr", {"align":"right"}):
            cells = row.findAll("td")
            if len(cells) == 5:
                rank = cells[0].find(text = True)
                male = cells[1].find(text = True)
                percent_m = cells[2].find(text = True)
                female = cells[3].find(text = True)
                percent_f = cells[4].find(text = True)
                #csvwriter.writerow([yr, rank, male, percent_m, female, percent_f])
                csvwriter.writerow([yr, 'Male', rank, male, percent_m])
                csvwriter.writerow([yr, 'Female', rank, female, percent_f])

            elif len(cells) == 3:
                ank = cells[0].find(text = True)
                male = cells[1].find(text = True)
                female = cells[2].find(text = True)
                print(rank, male, female)
