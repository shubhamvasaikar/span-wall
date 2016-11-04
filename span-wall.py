import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--left", help="Resolution of left side screen, e.g. (1600x900)")
parser.add_argument("-m", "--middle", help="Resolution of middle screen, e.g. (1280x720)", default="0x0")
parser.add_argument("-r", "--right", help="Resolution of right side screen, e.g. (1920x1080)")
parser.add_argument("--ileft", help="Path of left side image")
parser.add_argument("--imiddle", help="Path of middle image", default=None)
parser.add_argument("--iright", help="Path of right side image")
parser.add_argument("-o", "--output", help="Name of output image")

args = parser.parse_args()

x_left, y_left = args.left.split("x")
x_middle, y_middle = args.middle.split("x")
x_right, y_right = args.right.split("x")

x_left = int(x_left)
y_left = int(y_left)
x_middle = int(x_middle)
y_middle = int(y_middle)
x_right = int(x_right)
y_right = int(y_right)

x_new = x_left + x_middle + x_right
y_new = max(y_left, y_right)

left = Image.open(args.ileft)
left = left.resize((x_left, y_left), Image.ANTIALIAS)
if (x_middle > 0) and (y_middle > 0) and args.imiddle is not None:
    middle = Image.open(args.imiddle)
    middle = middle.resize((x_middle, y_middle), Image.ANTIALIAS)
right = Image.open(args.iright)
right = right.resize((x_right, y_right), Image.ANTIALIAS)

new_left = Image.new('RGB', (x_left, y_new))
if (x_middle > 0) and (y_middle > 0) and args.imiddle is not None:
    new_middle = Image.new('RGB', (x_middle, y_new))
new_right = Image.new('RGB', (x_right, y_new))

diff = y_new - y_left
for x in range(0, x_left):
    for y in range(0, y_new):
        if y < diff:
            new_left.putpixel((x, y), (0, 0, 0))
        else:
            new_left.putpixel((x, y), left.getpixel((x, y - diff)))

if (x_middle > 0) and (y_middle > 0) and args.imiddle is not None:
    diff = y_new - y_middle
    for x in range(0, x_middle):
        for y in range(0, y_new):
            if y < diff:
                new_middle.putpixel((x, y), (0, 0, 0))
            else:
                new_middle.putpixel((x, y), middle.getpixel((x, y - diff)))

diff = y_new - y_right
for x in range(0, x_right):
    for y in range(0, y_new):
        if y < diff:
            new_right.putpixel((x, y), (0, 0, 0))
        else:
            new_right.putpixel((x, y), right.getpixel((x, y - diff)))

final = Image.new('RGB', (x_new, y_new))

final.paste(new_left, (0, 0))
if (x_middle > 0) and (y_middle > 0) and args.imiddle is not None:
    final.paste(new_middle, (x_left, 0))
final.paste(new_right, ((x_left + x_middle), 0))

final.save(args.output+'.jpg')
