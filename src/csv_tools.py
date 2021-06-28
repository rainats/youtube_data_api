# -*- coding: utf-8 -*-

import csv

#writing dictionary to csv
def dict_to_csv(filename,fields,data):

    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields, extrasaction="ignore")

        writer.writeheader()
        writer.writerows(data)


#writing a list of lists to csv
def write_csv(filename,fields,data):

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(fields)
        csvwriter.writerows(data)
