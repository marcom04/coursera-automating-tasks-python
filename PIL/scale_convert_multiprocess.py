#!/usr/bin/env python3

import os, sys
import multiprocessing
from PIL import Image
import time

angle = 90
size = (128, 128)
indir = 'images'
outdir = 'icons'


def transform(infile):
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


if __name__ == "__main__":
    files = os.listdir(indir)

    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(transform, files)
    duration = time.time() - start_time
    print("Duration: {} seconds".format(duration))