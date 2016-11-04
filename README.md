# span-wall
A simple script to create a wallpaper that spans across 2 screens of different resolutions.

## Usage:

    span-wall.py [-h] [-l LEFT] [-r RIGHT] [--ileft ILEFT] [--iright IRIGHT] [-o OUTPUT]
    optional arguments:
    -h, --help                 show this help message and exit
    -l LEFT, --left LEFT       Resolution of left side screen, e.g. (1600x900)
    -r RIGHT, --right RIGHT    Resolution of right side screen, e.g. (1920x1080)
    --ileft ILEFT              Path of left side image
    --iright IRIGHT            Path of right side image
    -o OUTPUT, --output OUTPUT Name of output image.
    
## Example:
    
    python span-wall.py -l 1600x900 -r 1920x1080 --ileft r6left.jpg --iright r6right.jpg -o r6spanned
