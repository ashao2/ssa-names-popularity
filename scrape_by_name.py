import requests
from bs4 import BeautifulSoup
import csv
import argparse
import numpy as np

url = 'https://www.ssa.gov/cgi-bin/popularnames.cgi'

def get_names(num, start_yr, end_yr):

    if end_yr <= start_yr:
        raise Exception("Year range entered is invalid")

    if num < 1 or num > 1000:
        raise Exception("Number entered is invalid")

    yr_range = end_yr - start_yr + 1

    names_dict = dict()

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
            female = cells[3].find(text = True)

            if male not in names_dict:
                names_dict[male] = np.empty((end_yr - start_yr + 3), dtype=object)
                names_dict[male][0] = male
                names_dict[male][1] = 'Male'
                names_dict[male][yr - start_yr + 2] = rank
            else:
                names_dict[male][yr - start_yr + 2] = rank

            if female not in names_dict:
                names_dict[female] = np.empty((end_yr - start_yr + 3), dtype=object)
                names_dict[female][0] = female
                names_dict[female][1] = 'Female'
                names_dict[female][yr - start_yr + 2] = rank
            else:
                names_dict[female][yr - start_yr + 2] = rank


    with open('checkgender.csv', 'w') as bncsv:
        csvwriter = csv.writer(bncsv)
        col_names = list(range(start_yr, end_yr + 1))
        col_names.insert(0, 'gender')
        col_names.insert(0, 'name')
        csvwriter.writerow(col_names)

        for k, v in names_dict.items():
            csvwriter.writerow(v)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', default=100, help='Number of names (per gender), max is 1000')
    parser.add_argument('-s', '--start', default=1880, help='Start year, earliest available is 1880')
    parser.add_argument('-e', '--end', default=2020, help='End year, latest available is 2020')
    args = parser.parse_args()
    get_names(int(args.number), int(args.start), int(args.end))
