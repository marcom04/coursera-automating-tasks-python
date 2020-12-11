#!/usr/bin/env python3

import os
import requests

indir = "/data/feedback"
url = "http://34.70.234.76/feedback/"

files = os.listdir(indir)

for infile in files:
    # skip non-txt files
    if not infile.endswith('.txt'):
        continue
    
    # open file
    with open(os.path.join(indir, infile)) as f:
        data = {}
        lines = f.readlines()
        data["title"] = lines[0].strip()
        data["name"] = lines[1].strip()
        data["date"] = lines[2].strip()
        data["feedback"] = "".join(lines[3:]).replace("\n", " ")
        print("Posting feedback: {}".format(data))

        response = requests.post(url, data = data)
        response.raise_for_status()
        print("Response status code: {}".format(response.status_code))

        f.close()
