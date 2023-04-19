#!/usr/bin/env python

import sys
from PIL import Image

# Get the width and height from the command line arguments
try:
    width = int(sys.argv[1])
    height = int(sys.argv[2])
except:
    print("Usage: python program.py <width> <height> <filename>")
    sys.exit(1)

# Create a new grayscale image with the specified width and height
image = Image.new("L", (width, height), color=128)

# Get the filename from the command line arguments
filename = sys.argv[3]

# Save the image to a file with the specified filename
image.save(filename)

print("Success...")