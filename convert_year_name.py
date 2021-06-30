import pandas as pd
import numpy as np
import csv
import argparse

def convert_years_to_names(path):
    df = pd.read_csv(path)
    dims = df.shape
    start_yr = df['year'].min()
    end_yr = df['year'].max()

    names_dict = dict()
    for i in range(0, dims[0]):
        name = str(df['name'][i])
        rank = int(df['rank'][i])
        yr = int(df['year'][i])
        if name not in names_dict:
            names_dict[name] = np.empty((end_yr - start_yr + 2), dtype=object)
            names_dict[name][0] = name
            names_dict[name][yr - start_yr + 1] = rank
        else:
            names_dict[name][yr - start_yr + 1] = rank

    with open('post_conversion.csv', 'w') as bncsv:
        csvwriter = csv.writer(bncsv)
        col_names = list(range(start_yr, end_yr + 1))
        col_names.insert(0, 'name')
        csvwriter.writerow(col_names)

        for k, v in names_dict.items():
            csvwriter.writerow(v)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filepath', help='Enter path to CSV file')
    args = parser.parse_args()
    convert_years_to_names(args.filepath)
