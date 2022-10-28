# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 23:30:43 2022

@author: AAkshayp
"""

import requests
import json
from accesstoken import getAccessToken
from updateCHNGUstate import updateChangeRequest

def createCtask(change_number):
    url = "https://jnj-internal-development.apigee.net/apg-001-servicenow/v1/now/table/change_task/"
    headers = getAccessToken()
    
    payload = json.dumps({"ctask_object":{"order" : "100",
                                          "planned_end_date" : "2022-10-29 08:45:00",
                                          "short_description": "Pre-implementation verification",
                                          "description": "Login to SAP DB Server, and verify select access is granted for the tables require supplemental logging",
                                          "planned_start_date" : "2022-10-28 08:50:00",
                                          "cmdb_ci" : "INFA_OPC_EDG_NA_DEV"},
                          "change_request":change_number
                          })
    response = requests.request(method = 'POST', url = url, headers = headers, data = payload)
    
    payload = json.dumps({"ctask_object":{"order" : "200",
                                          "planned_end_date" : "2022-10-29 08:45:00",
                                          "short_description": "Implementation",
                                          "description": "Enable Supplemental logging for tables",
                                          "planned_start_date" : "2022-10-28 08:50:00",
                                          "cmdb_ci" : "INFA_OPC_EDG_NA_DEV"},
                          "change_request":change_number
                          })
    response = requests.request(method = 'POST', url = url, headers = headers, data = payload)
    
    payload = json.dumps({"ctask_object":{"order" : "300",
                                          "planned_end_date" : "2022-10-29 08:45:00",
                                          "short_description": "Post-Implementation of Verification of Supplemental logging",
                                          "description": "Verify table supplemental logging granted successfully",
                                          "planned_start_date" : "2022-10-28 08:50:00",
                                          "cmdb_ci" : "INFA_OPC_EDG_NA_DEV"},
                          "change_request":change_number
                          })
    response = requests.request(method = 'POST', url = url, headers = headers, data = payload)
    
    payload = json.dumps({"ctask_object":{"order" : "400",
                                          "planned_end_date" : "2022-10-29 08:45:00",
                                          "short_description": "Implementation - Register the tables",
                                          "description": "Register the tables for which supplemental logging are granted",
                                          "planned_start_date" : "2022-10-28 08:50:00",
                                          "cmdb_ci" : "INFA_OPC_EDG_NA_DEV"},
                          "change_request":change_number
                          })
    response = requests.request(method = 'POST', url = url, headers = headers, data = payload)
    
    payload = json.dumps({"ctask_object":{"order" : "500",
                                          "planned_end_date" : "2022-10-29 08:45:00",
                                          "short_description": "Post-implemenation Register tables",
                                          "description": "Please check tables are registered successfully.",
                                          "planned_start_date" : "2022-10-28 08:50:00",
                                          "cmdb_ci" : "INFA_OPC_EDG_NA_DEV"},
                          "change_request":change_number
                          })
    response = requests.request(method = 'POST', url = url, headers = headers, data = payload)
    
    payload = json.dumps({"ctask_object":{"order" : "600",
                                          "planned_end_date" : "2022-10-29 08:45:00",
                                          "short_description": "Implementation - Stop & Start PWX Logger",
                                          "description": "In the database server , stop and start Informatica PWX logger",
                                          "planned_start_date" : "2022-10-28 08:50:00",
                                          "cmdb_ci" : "INFA_OPC_EDG_NA_DEV"},
                          "change_request":change_number
                          })
    response = requests.request(method = 'POST', url = url, headers = headers, data = payload)
    
    payload = json.dumps({"ctask_object":{"order" : "700",
                                          "planned_end_date" : "2022-10-29 08:45:00",
                                          "short_description": "Post-Implementation",
                                          "description": "Verify the informatica PWX logger in the DB server started successfully",
                                          "planned_start_date" : "2022-10-28 08:50:00",
                                          "cmdb_ci" : "INFA_OPC_EDG_NA_DEV"},
                          "change_request":change_number
                          })
    response = requests.request(method = 'POST', url = url, headers = headers, data = payload)
    

createCtask("CHG000010835425")
#createCtask("CHG000010835412")