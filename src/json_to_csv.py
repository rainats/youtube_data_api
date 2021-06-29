# -*- coding: utf-8 -*-

import json
import csv
from jsontool import *
from unicodedata import normalize
from csv_tools import *

#converting unicode to byte string
def norm_uni(elem):
    return normalize('NFKD',elem).encode('ascii', 'ignore')


def json_csv():
    jsondata = jload("main_data.json")

    #creating a list of list of tags from all videos
    #replacing the unicode tag values in jsondata with byte string value
    index = 0
    tags_list,time_list,norm_tag = ([] for i in range(3))
    #returns tag and duration list of all videos
    # IMP : Any videos without tags will be permanently removed from
    #here onwards except in the main_data.csv file
    for videos in jsondata:

        if videos.get("tags") is not None:

            norm_tag = [norm_uni(elem) for elem in videos.get("tags")]
            tags_list.append(norm_tag)
            time_list.append(norm_uni(videos.get("duration")))
            jsondata[index]["tags"]= norm_tag

            index +=1

    #writing to a csv file
    fields = ['duration','tags']
    filename = "main_data.csv"
    dict_to_csv(filename,fields,jsondata)

    return jsondata,tags_list,time_list
