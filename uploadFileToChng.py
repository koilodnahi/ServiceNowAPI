# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 00:27:04 2022

@author: AAkshayp
"""

import requests
import json
from accesstoken import getAccessToken

def uploadFilesToChange(change_number, filename):
    url = f"https://jnj-internal-development.apigee.net/apg-001-servicenow/v1/now/table/change_request?sysparm_query=number={change_number}"
    headers = getAccessToken()
    
    response = requests.request(method = "GET", url = url, headers = headers)
    if response.status_code == requests.codes.ok:
        response_str = response.content.decode('utf-8')
        response_fields = json.loads(response_str)
        
        print(response_fields)
        
        sys_id = response_fields['result'][0]['sys_id']
        print(sys_id)
        
        url = f"https://jnj-internal-development.apigee.net/apg-001-servicenow/v1/now/attachment/change_request/{sys_id}"
        payload={}
        
        files=[
            ('',('SAP_REQUEST_ASPAC_APCONSUMER.xlsx',open('D:/Users/AAkshayp/Downloads/SAP_REQUEST_ASPAC_APCONSUMER.xlsx','rb'),
                 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
             )
            ]
        #headers['Content-Type'] = 'multipart/form-data'
        response = requests.request(method = "POST", url = url, headers=headers, files=files)
        
uploadFilesToChange("CHG000010835425", "")