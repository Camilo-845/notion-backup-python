
import datetime
from src import *

timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H_%M_%S')
folder = '../backups/notionbackup_' + timestamp
dataBaseID = "731d20d7-7815-4dac-806e-bef4654f2467"

headers = {
  'Authorization': 'Bearer secret_lpa4riCCDmZuURvr2GgsQVtkAIXRlVk8M77OpYO5KJm',
  'Notion-Version': '2022-06-28',
  'Content-Type': 'application/json',
}

makeBackup(folder, headers,dataBaseID)