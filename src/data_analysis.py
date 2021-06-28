# -*- coding: utf-8 -*-

import os
import json
import csv
import re
from csv_tools import *
from json_to_csv import *

def myFunc1(e):
  return e["Video_Count"]

def myFunc2(e):
  return e["Time_Duration"]

def string_search(kw,str_dur):
    try:
        found = int(re.search(kw,str_dur).group(1))
    except AttributeError:
        found = 0
    except Exception:
        found = 0
    return found

def time_format(time_list):
    format_time_list = []

    for i in time_list:
        #converting hour to sec
        time_value = string_search('T(.+?)H',i)*3600
        #converting min to sec
        time_value+=string_search('T(.+?)M',i)*60
        time_value+=string_search('T(.+?)S',i)
        time_value+=string_search('H(.+?)M',i)*60
        time_value+=string_search('H(.+?)S',i)
        time_value+=string_search('M(.+?)S',i)

        format_time_list.append(time_value)

    return format_time_list

def analysis(data,tags_list,time_list):
    #arranging tags in order of video count for each tag
    #arranging tags in order of video duration
#data,tags_list,time_list = json_csv(" ")

    format_time_list = time_format(time_list)

    unique_tags,data_tags = ([] for i in range(2))

    for i,time in zip(tags_list,format_time_list):
        for j in i:
            k = j.strip()
            if k:
                if k not in unique_tags:
                    data_tags.append({"Tags":k,"Video_Count":1,"Time_Duration":time})
                    unique_tags.append(k)
                else:
                    dup_tag_index = unique_tags.index(k)
                    data_tags[dup_tag_index]["Video_Count"]+=1
                    data_tags[dup_tag_index]["Time_Duration"]+=time

    index = 0
    for i in data_tags:
        avg_time = float(i["Time_Duration"]/i["Video_Count"])
        data_tags[index]["Time_Duration"] = avg_time
        index+=1

    data_tags.sort(reverse=True,key=myFunc1)

    dest_dir = os.path.split(os.getcwd())[0] + '/results'

    fields_1 = ['Tags','Video_Count']
    dict_to_csv(dest_dir+'/'+"tag_vs_videocount.csv",fields_1,data_tags)

    data_tags.sort(reverse=True,key=myFunc2)

    fields_2 = ['Tags','Time_Duration']
    dict_to_csv(dest_dir+'/'+"tag_vs_duration.csv",fields_2,data_tags)
