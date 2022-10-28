# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 23:16:03 2022

@author: AAkshayp
"""
import requests
import json
from accesstoken import getAccessToken
import pandas as pd


def readCtaskStatus(change_number):
    url = f"https://jnj-internal-development.apigee.net/apg-001-servicenow/v1/now/table/change_task?sysparm_query=parent.number={change_number}&sysparm_fields=parent.number,sys_id,number,order,u_state,short_description&sysparm_display_value=TRUE"
    
    headers = getAccessToken()
    
    response = requests.request(method = "GET", url = url, headers = headers)
    
    if response.status_code == requests.codes.ok:
        response_str = response.content.decode('utf-8')
        response_fields = json.loads(response_str)
        
    data = pd.DataFrame(response_fields['result'])
    data.sort_values('order', inplace=True)
    
    return data
    
data = readCtaskStatus("CHG000010835425")