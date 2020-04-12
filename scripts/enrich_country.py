#!/usr/bin/python3
import os
import sys
import csv
import pickle

## Need this line so Atom can run it
os.chdir('/home/andres/Programs/python/covid/scripts')
#print(os.getcwdb())

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def get_coords(country):
    if country in country_dict:
        return country_dict[country]
    else: return False

country_dict = load_obj('country_coords')

def main():
    with open('../data/full_data.csv') as csvData:
        file = csv.reader(csvData, delimiter=',')
        headers = ['name','date','new_cases','new_deaths','total_cases','total_deaths']
        with open('../data/full_data_enrd.csv', 'w') as csvOut:
            writer = csv.DictWriter(csvOut, fieldnames=headers)
            writer.writeheader()
            next(file)
            sorted_file = sorted(file, key=lambda row: row[0], reverse=True)
            country = None
            date = '2020-04-01'
            for line in sorted_file:
                print (line)
                if line[1] != country and line[0] == date:
                    country = line[1]
                    date = line[0]
                    new_line = []
                    if get_coords(country):
                        new_line.append(country)
                        new_line.append(line[0])
                        new_line.append(line[2])
                        new_line.append(line[3])
                        new_line.append(line[4])
                        new_line.append(line[5])
                        line_dict = {k:v for k,v in zip(headers,new_line)}
                        writer.writerow(line_dict)
                        print(new_line)
if __name__ == '__main__':
    sys.exit(main())
