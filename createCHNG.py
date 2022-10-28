# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 23:04:44 2022

@author: AAkshayp
"""
from accesstoken import getAccessToken
import requests
import json


def createChangeRequest():
    url = "https://jnj-internal-development.apigee.net/apg-001-servicenow/v1/now/table/change/normal/"
    
    headers = getAccessToken()
    #"correlation_id":"ExternalTicket-12345",
    payload = json.dumps({"category":"Application",
                          "short_description":"Sample Change - Add table supplemental logs for Informatica CDC",
                          "description":"Sample Change - 1) Add table supplimental logs 2) Register tables 3) Stop and Start Informatica Logger",
                          "u_state":"100"})
    
    
    response = requests.post(url, headers = headers, data = payload)
    print(response)
    if response.status_code == requests.codes.ok:
        response_str = response.content.decode('utf-8')
        response_fields = json.loads(response_str)
        print(response_fields)
        
    print(response_fields['result']['number']['display_value'])
    return response_fields['result']['number']['display_value']
        
