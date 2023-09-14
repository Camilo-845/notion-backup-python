import os
import requests
import json
import datetime
from .catchError import *

def getPage(pageId,headers,errorsLogsfolder):
    try:
        response =requests.post(f'https://api.notion.com/v1/pages/{pageId}', headers=headers)
        return response.json()
    except Exception as err:
        response = {"Type": type(err) ,"Error": err.args}
        saveError(errorsLogsfolder, response)

def mapByData(key,data):
    dataType = data["type"]
    if(dataType == "number"):
        return data["number"]
    elif (dataType=="formula"):
        return mapByData(key,data["formula"])
    elif (dataType=="status"):
        return data["status"]["name"]
    elif (dataType=="checkbox"):
        return data["checkbox"]
    elif (dataType=="text"):
        return data["text"]["content"]
    elif (dataType=="relation"):
        if(key=="Cliente"):
            for d in data["relation"]:
                return d["id"]
        else:
            for d in data["relation"]:
                return d["id"]
    elif (dataType=="rich_text"):
        if (len(data["rich_text"])==0):
            return ""
        else:
            return mapByData(key,data["rich_text"][0])
    elif (dataType=="date"):
        if(data["date"]):
            return data["date"]["start"]
        else:
            return data["date"]
    else:
        return "otro dato"

def mapResponse(data):
    mainData = []
    print(len(data))
    for element in data:
        mapData = {}
        for key,val in element["properties"].items():
            mapData[key] = mapByData(key,val)
        mainData.append(mapData)
    return mainData

def makeBackup(folder,headers, dataBaseID):
    try:
        os.mkdir(folder)
        # replace YOUR_INTEGRATION_TOKEN with your own secret token
        response =requests.post(f'https://api.notion.com/v1/databases/{dataBaseID}/query', headers=headers)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        errorsLogsfolder = './errorLogs/errorLog_' + timestamp
        
        if checkErrorCode(response.status_code) :
            os.rmdir(folder)
        else:
            has_more = True
            open(f'{folder}/result.json', 'w').write("[")
            while(has_more):
                with open(f'{folder}/result.json', 'a') as file:
                   # results = json.dumps(response.json())
                    print (type(response.json()["results"]))
                    
                    results = mapResponse(response.json()["results"])
                    file.write(json.dumps(results)[1:-1]+",")

                if(not response.json()['has_more']):
                    has_more=False
                    break
                
                params ={}
                params["start_cursor"] = response.json().get("next_cursor")
                response =requests.post(
                    f'https://api.notion.com/v1/databases/{dataBaseID}/query',
                    headers=headers,
                    json=params
                )
            open(f'{folder}/result.json', 'a').write("]")
        """ for block in response.json()['results']:
            with open(f'{folder}/{block["id"]}.json', 'w') as file:
                file.write(json.dumps(block))

            child_blocks = requests.get(
                f'https://api.notion.com/v1/blocks/{block["id"]}/children',
                headers=headers,
            )
            if child_blocks.json()['results']:
                os.mkdir(folder + f'/{block["id"]}')

                for child in child_blocks.json()['results']:
                with open(f'{folder}/{block["id"]}/{child["id"]}.json', 'w') as file:
                    file.write(json.dumps(child)) """
    except Exception as err:
        response = {"Type": type(err) ,"Error": err.args}
        saveError(errorsLogsfolder, response)

def mapData(data):
    print(data)
    return data