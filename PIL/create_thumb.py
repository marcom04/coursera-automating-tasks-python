''' Crop image(s) to be squares (centered), then create 128x128 thumbnail.
    Just to play around with the PIL library.
'''

import os, sys
from PIL import Image

size = (128, 128)

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumb"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                # crop to square
                xsize, ysize = im.size
                if xsize != ysize:
                    center = (xsize/2, ysize/2)
                    if xsize > ysize:
                        box = ((xsize - ysize) / 2, 0, (xsize + ysize) / 2, ysize)
                        im = im.crop(box)
                    elif xsize < ysize:
                        box = (0, (ysize - xsize) / 2, xsize, (ysize + xsize) / 2)
                        im = im.crop(box)
                # create thumbnail
                im.thumbnail(size)
                im.save(outfile, "JPEG")
        except OSError:
            print("Cannot create thumbnail for {}".format(infile))