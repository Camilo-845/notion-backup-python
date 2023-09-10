import datetime
import os
import json

errorCodes = [400,401,403,404,409,429,500,503,504]


def checkErrorCode(code):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    errorsLogsfolder = './errorLogs/errorLog_' + timestamp

    if code in errorCodes:
        response = {"Type": "Error Code" ,"Error": code}
        open(f'{errorsLogsfolder}.json',"w").write(json.dumps(response))
        return True
    else:
        return False
        
