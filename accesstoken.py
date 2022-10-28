# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:37:27 2022

@author: AAkshayp
"""

import requests
import json
import datetime

def getAccessToken():
    url = "https://login.microsoftonline.com/its.jnj.com/oauth2/token?api-version=1.0"
    
    payload = {'grant_type': 'client_credentials',
               'client_id': 'ac905574-0edb-47b1-bd78-1f8ac067590f',
               'client_secret': '3Bz8Q~AYIGLVJTa4sMaT5Bx41AFcPw7DvGNrzc1E',
               'resource': 'https://ITS-APP-ISM-IRIS-Dev.jnj.com'}
    
    '''
    resource points for DEV/QA/PROD Env
    https://ITS-APP-ISM-IRIS-Dev.jnj.com --> Iris Development
    https://ITS-APP-ISM-IRIS-Test.jnj.com --> Iris Test
    https://ITS-APP-ISM-IRIS-QA.jnj.com --> Iris QA
    https://ITS-APP-ISM-IRIS-Prod.jnj.com --> Iris Production
    '''
    
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code==requests.codes.ok:           
        access_str = response.content.decode('utf-8')
        access_fields=json.loads(access_str)
        #print(access_fields)
        expires_on = datetime.datetime.fromtimestamp(int(access_fields['expires_on']))
        #print(expires_on)
        access_token = f'Bearer {access_fields["access_token"]}'
        print(access_token)
        
    headers = {'Authorization' : access_token,
               'Accept' : 'application/json',
               'Content-Type' : 'application/json'}
    
    return headers
