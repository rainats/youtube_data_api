# -*- coding: utf-8 -*-

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

def call_api():

    scopes = ["https://www.googleapis.com/auth/youtube.readonly",
            "https://www.googleapis.com/auth/youtube.force-ssl"]

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    service_obj = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    return service_obj
