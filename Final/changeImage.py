#!/usr/bin/env python3

import os
from PIL import Image

size = (600, 400)
inoutdir = 'supplier-data/images'

# iterate images inside in folder
for infile in os.listdir(inoutdir):
    # skip sub-directories
    if not os.path.isfile(os.path.join(inoutdir, infile)):
        continue

    print("Processing {}".format(infile))
    try:
        with Image.open(os.path.join(inoutdir, infile)) as im:
            # resize image to 600x400 with Image.resize
            out = im.resize(size)

            # save image to out folder as JPEG with same name using Image.save
            outfile = infile.replace('.tiff', '.jpeg')
            out.convert('RGB').save(os.path.join(inoutdir, outfile), "JPEG")

    except OSError as err:
        print("{}: {}".format(infile, err))