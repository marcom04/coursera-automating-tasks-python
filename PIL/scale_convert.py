#!/usr/bin/env python3

import os, sys
from PIL import Image

angle = 90
size = (128, 128)
indir = 'images'
outdir = '/opt/icons'

# iterate images inside in folder
for infile in os.listdir(indir):
    # skip sub-directories
    if not os.path.isfile(os.path.join(indir, infile)):
        continue

    print("Processing {}".format(infile))
    try:
        with Image.open(os.path.join(indir, infile)) as im:
            # rotate image 90° clockwise with Image.rotate and resize image to 128x128 with Image.resize
            # print("Rotating and resizing {}".format(im.filename))
            out = im.rotate(angle).resize(size)

            # save image to out folder as JPEG with same name using Image.save
            # print("Saving {} to {}".format(im.filename, outdir))
            out.convert('RGB').save(os.path.join(outdir, infile), "JPEG")

    except OSError as err:
        print("{}: {}".format(infile, err))
