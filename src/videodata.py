# -*- coding: utf-8 -*-

def video_list(service_obj,video_param):

    video_response = service_obj.videos().list(
        part=video_param[0],
        id=video_param[1],
        maxResults=video_param[2]
        ).execute()

    return video_response
