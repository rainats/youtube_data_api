# -*- coding: utf-8 -*-

from unicodedata import normalize

def search_list(service_obj,search_param):

    search_response = service_obj.search().list(
        part=search_param[0],
        pageToken=search_param[1],
        order=search_param[2],
        q=search_param[3],
        maxResults=search_param[4],
        type=search_param[5]
    ).execute()

    videosId = []

    for search_result in search_response.get("items", []):
        #normalize the unicode videoId data to string
        # from the search response
        vid_id = normalize('NFKD', search_result["id"]["videoId"]
        ).encode('ascii', 'ignore')
        videosId.append(vid_id)
    #convert list of video Ids to string
    vid_id_str = ','.join(videosId)

    #error handling for pagination
    try:
        next_token = search_response["nextPageToken"]
        return(next_token, vid_id_str)
    except Exception as e:
        nexttok = "last_page"
        return(next_token, vid_id_str)
