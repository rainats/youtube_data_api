# -*- coding: utf-8 -*-

from api_call import *
from data_collect import *
from data_extraction import *
from json_to_csv import *
from data_analysis import *

def main():

    service_obj = call_api()
    collect_data(service_obj)
    data_extraction()
    data,tags_list,time_list = json_csv("True")
    analysis(data,tags_list,time_list)

if __name__ == "__main__":
    main()
