#! /usr/bin/env python 
# -*- coding: utf-8 -*

import os
import sys
from PIL import Image

def main():
    for infile in sys.argv[1:]:
        outfile = os.path.splitext(infile)[0] + ".thumbnail"
        if infile != outfile: 
            try: 
                im = Image.open(infile)
                x, y = im.size
                print im.format, im.size, im.mode
                im.show()
                im.thumbnail((x//2, y//2))
                im.save(outfile, "JPEG")
                im.show()
            except IOError:
                print "cannot create thumbnail for", infile


if __name__ == '__main__':
    main()
    