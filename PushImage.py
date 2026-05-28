import sys
import PyLog
from PIL import Image
from inky import InkyWHAT

if __name__ == '__main__':
    display = InkyWHAT("red")
    display.set_border(display.WHITE)

    args = sys.argv

    if len(args) != 2:
        PyLog.error( "Invalid number of arguments!" )
        exit(1)

    PyLog.log( f"Pusing {args[1]} to screen" )

    img_to_push = args[1]
    img = Image.open( img_to_push )
    pal_img = Image.new('P', (1,1))
    pal_img.putpalette((255,255,255,0,0,0,255,0,0)+(0,0,0)*252)
    img = img.convert('RGB').quantize(palette=pal_img)
    display.set_image(img)
    display.show()
