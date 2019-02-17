import requests
import json
import pandas as pd
import numpy as np
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

TOKEN = 'your token'
CHANNEL = 'target channel id'

###############
# post photo
###############
files = {'file': open("test.jpg", 'rb')}
param = {
    'token':TOKEN, 
    'channels':CHANNEL,
    'filename':"filename",
    'initial_comment': "initial_comment",
    'title': "title"
}
requests.post(url="https://slack.com/api/files.upload",params=param, files=files)
