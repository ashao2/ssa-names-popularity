import requests
from bs4 import BeautifulSoup
import csv
import argparse

url = 'https://www.ssa.gov/cgi-bin/popularnames.cgi'

def get_names(num, start_yr, end_yr):

    if end_yr <= start_yr:
        raise Exception("Year range entered is invalid")

    if num < 1 or num > 1000:
        raise Exception("Number entered is invalid")

    with open('babynames.csv', 'w') as bncsv:
        csvwriter = csv.writer(bncsv)
        #csvwriter.writerow(['year', 'rank', 'males', 'percent_males', 'females', 'percent_females'])
        csvwriter.writerow(['year', 'gender', 'rank', 'name', 'percent'])

        for yr in range (start_yr, end_yr + 1):
            post_params = {'year': yr, 'top': num, 'number': 'p'}
            response = requests.post(url, data=post_params)
            soup = BeautifulSoup(response.content, 'html.parser')

            table = soup.find("table", {"width":"72%"})
            for row in table.findAll("tr", {"align":"right"}):
                cells = row.findAll("td")

                if len(cells) != 5:
                    raise Exception("Something's wrong with the table on the webpage!")

                rank = cells[0].find(text = True)
                male = cells[1].find(text = True)
                percent_m = cells[2].find(text = True)
                female = cells[3].find(text = True)
                percent_f = cells[4].find(text = True)
                #csvwriter.writerow([yr, rank, male, percent_m, female, percent_f])
                csvwriter.writerow([yr, 'Male', rank, male, percent_m[:-1]])
                csvwriter.writerow([yr, 'Female', rank, female, percent_f[:-1]])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', default=100, help='Number of names (per gender), max is 1000')
    parser.add_argument('-s', '--start', default=1880, help='Start year, earliest available is 1880')
    parser.add_argument('-e', '--end', default=2020, help='End year, latest available is 2020')
    args = parser.parse_args()
    get_names(int(args.number), int(args.start), int(args.end))
