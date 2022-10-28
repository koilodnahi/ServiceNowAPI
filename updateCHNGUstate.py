# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:05:54 2022

@author: AAkshayp
"""

import requests
import json
from accesstoken import getAccessToken
from createCHNG import createChangeRequest

## "assigned_to":"702367400",
#                                           "assigned_to":"702310312",
#                                   "u_assignment_group":"EDG L1",

def updateChangeRequest(change_number):
    url = f"https://jnj-internal-development.apigee.net/apg-001-servicenow/v1/now/table/change/normal/{change_number}"
    print(url)
    headers = getAccessToken()
    
    payload = json.dumps({"change_object":{"cmdb_ci":"INFA_OPC_EDG_NA_DEV",
                                           "u_emergency_type":"3",
                                           "start_date":"2022-10-28 16:12:00",
                                           "end_date":"2022-10-29 17:30:00",
                                           "impact":"3",
                                           "urgency":"2",
                                           "justification":"This table data is needed for Common data layer (CDL) hosted in Azure data lake.",
                                           "u_business_impact":"No Impact",
                                           "implementation_plan":"implemention plan",
                                           "test_plan":"Test plan",
                                           "backout_plan":"Revert back to previous version",
                                           "risk_impact_analysis":"Low and no impact",
                                           "u_state":"200"
                                           }
                          })
    
    response = requests.request(method = 'PUT', url = url, headers = headers, data = payload)
    print(response.content)
    if response.status_code == requests.codes.ok:
        response_str = response.content.decode('utf-8')
        response_fields = json.loads(response_str)
        print(response_fields)
        
    print(change_number)
    return change_number
        
updateChangeRequest(createChangeRequest())
#updateChangeRequest("CHG000010835414")