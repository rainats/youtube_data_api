# -*- coding: utf-8 -*-

from searchdata import *
from videodata import *
from jsontool import *

def collect_data(service_obj):

    next_token = None
    max_results = 50
    data_list = [] #array to dump in json file

    for i in range(7):
        #search parameters in the order part,pageToken
        #order,q,maxResults,type
        search_param = ["id",
        next_token,
        "viewCount",
        "python",
        max_results,
        "video"]
        search_data = search_list(service_obj,search_param)

        #video parameters in the order part,videoId,maxResults
        video_param = ["snippet,contentDetails",
        search_data[1],
        max_results]
        video_data = video_list(service_obj,video_param)

        data_list.append(video_data)

        next_token = search_data[0]

    jprint("video_data.json",data_list)
