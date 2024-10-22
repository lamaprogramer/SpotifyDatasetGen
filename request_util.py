import requests
from urllib import parse

def get(url: str, access_token: str, params: str = ""):
    headers = {"Authorization": "Bearer " + access_token}
    return requests.get(url+"?"+params, headers=headers) if params != "" else requests.get(url, headers=headers)

# Dictionary Data
def delete(url: str, access_token: str, data: dict = {}, params: str = "", content_type: str = "application/json"):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": content_type}
    return requests.delete(url+"?"+params, headers=headers, data=data) if params != "" else requests.delete(url, headers=headers, data=data)

def put(url: str, access_token: str, data: dict = {}, params: str = "", content_type: str = "application/json"):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": content_type}
    return requests.put(url+"?"+params, headers=headers, data=data) if params != "" else requests.put(url, headers=headers, data=data)

def post(url: str, access_token: str, data: dict = {}, params: str = "", content_type: str = "application/json"):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": content_type}
    return requests.post(url+"?"+params, headers=headers, data=data) if params != "" else requests.post(url, headers=headers, data=data)

# String Data
def delete(url: str, access_token: str, data: str = "", params: str = "", content_type: str = "application/json"):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": content_type}
    return requests.delete(url+"?"+params, headers=headers, data=data) if params != "" else requests.delete(url, headers=headers, data=data)

def put(url: str, access_token: str, data: str = "", params: str = "", content_type: str = "application/json"):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": content_type}
    return requests.put(url+"?"+params, headers=headers, data=data) if params != "" else requests.put(url, headers=headers, data=data)

def post(url: str, access_token: str, data: str = "", params: str = "", content_type: str = "application/json"):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": content_type}
    return requests.post(url+"?"+params, headers=headers, data=data) if params != "" else requests.post(url, headers=headers, data=data)

def stringFromList(vals: list):
    output = ""
    for val in vals:
        output += str(val)+","
    return output[:-1]

def genParams(params: dict):
    paramString = ""
    for key, value in params.items():
        if value == None or value == "NaN" or value == "":
            continue
        
        if type(value) == list:
            paramString += key+"="+parse.quote(stringFromList(value))+"&"
            continue
        
        paramString += key+"="+parse.quote(str(value))+"&"
    return paramString[:-1]
