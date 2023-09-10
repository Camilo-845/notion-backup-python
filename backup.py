
import datetime
from src import *

timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
folder = '../backups/notionbackup_' + timestamp


headers = {
  'Authorization': 'Bearer secret_lpa4riCCDmZuURvr2GgsQVtkAIXRlVk8M77OpYO5KJm',
  'Notion-Version': '2022-06-28',
  'Content-Type': 'application/json',
}

makeBackup(folder, headers)