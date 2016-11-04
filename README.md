# span-wall
A simple script to create a wallpaper that spans across 2 screens of different resolutions.

## Usage:

    span-wall.py [-h] [-l LEFT] [-m MIDDLE] [-r RIGHT] [--ileft ILEFT] [--imiddle IMIDDLE] [--iright IRIGHT] [-o OUTPUT]

    optional arguments:
    -h, --help                 show this help message and exit
    -l LEFT, --left LEFT       Resolution of left side screen, e.g. (1600x900)
    -m MIDDLE, --middle MIDDLE Resolution of middle screen, e.g. (1280x720)
    -r RIGHT, --right RIGHT    Resolution of right side screen, e.g. (1920x1080)
    --ileft ILEFT              Path of left side image
    --imiddle IMIDDLE          Path of middle image
    --iright IRIGHT            Path of right side image
    -o OUTPUT, --output OUTPUT Name of output image.
    
## Example for 2 monitors:
    
    python span-wall.py -l 1600x900 -r 1920x1080 --ileft r6left.jpg --iright r6right.jpg -o r6spanned

### Left Image:

![alt text](http://i.imgur.com/rT3KlV0.jpg "Left Side Image")

### Right Image:

![alt text](http://i.imgur.com/yEFMuzb.jpg "Right Side Image")

### Final Image:

![alt text](http://i.imgur.com/D53spDm.jpg "Final Image")

## Example for 3 monitors:
    
    python span-wall.py -l 1600x900 -m 1280x720 -r 1920x1080 --ileft mleft.jpg --imiddle mmiddle.jpg --iright mright.jpg -o m3spanned

### Left Image:

![alt text](http://i.imgur.com/u42ZRTH.jpg "Left Side Image")

### Middle Image:

![alt text](http://i.imgur.com/LWYoePR.jpg "Middle Image")

### Right Image:

![alt text](http://i.imgur.com/jfsI4rJ.jpg "Final Image")

### Final Image:

![alt text](http://i.imgur.com/q9HzQuP.jpg "Final Image")