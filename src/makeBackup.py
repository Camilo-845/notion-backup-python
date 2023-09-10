import os
import requests
import json
from .catchError import *

def makeBackup(folder,headers):
    try:
        os.mkdir(folder)
        # replace YOUR_INTEGRATION_TOKEN with your own secret token
        response =requests.post('https://api.notion.com/v1/search', headers=headers)
        
        if checkErrorCode(response.status_code) :
            os.rmdir(folder)
        else:
            has_more = True
            open(f'{folder}/result.json', 'w').write("[")
            while(has_more):
                with open(f'{folder}/result.json', 'a') as file:
                    file.write(json.dumps(response.json()["results"])[1:-1]+",")

                if(not response.json()['has_more']):
                    has_more=False
                    break
                
                params ={}
                params["start_cursor"] = response.json().get("next_cursor")
                response =requests.post(
                    f'https://api.notion.com/v1/search',
                    headers=headers,
                    json=params
                )
            open(f'{folder}/result.json', 'a').write("]")
        """  for block in response.json()['results']:
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
        print(response)