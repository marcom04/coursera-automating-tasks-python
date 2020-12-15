#!/usr/bin/env python3

import requests
import os

# {"name": "Test Fruit", "weight": 100, "description": "This is the description of my test fruit", "image_name": "icon.sheet.png"}

url = "http://localhost/fruits/"
indir = 'supplier-data/descriptions'

# iterate images inside in folder
for infile in os.listdir(indir):
    with open(os.path.join(indir, infile)) as f:
        data = {}
        lines = f.readlines()
        data["name"] = lines[0]
        data["weight"] = int(lines[1].strip(' lbs'))
        data["description"] = lines[2]
