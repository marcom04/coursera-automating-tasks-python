#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
indir = 'supplier-data/images'

# iterate images inside in folder
for infile in os.listdir(indir):
    if infile.endswith('.jpeg'):
        with open(os.path.join(indir, infile)) as opened:
            response = requests.post(url, files={'file': opened})
