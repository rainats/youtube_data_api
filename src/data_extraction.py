# -*- coding: utf-8 -*-

from jsontool import *

def data_extraction():
    jsondata = jload("video_data.json")
    data_list = []
    for page in jsondata: #7 iterations
        for video in page["items"]:#50 iterations
            data_list.append({"title":video["snippet"]["title"],
            "duration":video["contentDetails"]["duration"],
            "tags":video["snippet"].get("tags",None)})
    jprint("main_data.json",data_list)
