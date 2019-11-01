import sys
from pathlib import Path

CWF = Path(__file__)
PROJECT_PATH = str(CWF.parent) + '/'

print (CWF.parent)
URL_PATH = 'url.txt'
PARSED_URL_PATH = PROJECT_PATH + 'data/parsed_url.txt'
AUDIO_PATH = PROJECT_PATH + 'data/audio/'
SCRIPT_PATH = PROJECT_PATH + 'data/script/'