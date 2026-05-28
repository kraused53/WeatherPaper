import sys
import PyLog
from PIL import Image
#from inky import InkyWHAT

if __name__ == '__main__':
#    display = InkyWHAT("red")
#    display.set_border(display.WHITE)

    args = sys.argv

<<<<<<< HEAD:PushImage.py
    if len(args) != 2:
        PyLog.error( "Invalid number of arguments!" )
        exit(1)

    img_to_push = args[1]
    img = Image.open( img_to_push )
    pal_img = Image.new('P', (1,1))
    pal_img.putpalette((255,255,255,0,0,0,255,0,0)+(0,0,0)*252)
    img = img.convert('RGB').quantize(palette=pal_img)
    display.set_image(img)
    display.show()
=======
    img = generate_png( report )
    img.show()
#    pal_img = Image.new('P', (1,1))
#    pal_img.putpalette((255,255,255,0,0,0,255,0,0)+(0,0,0)*252)
#    img = img.convert('RGB').quantize(palette=pal_img)
#    display.set_image(img)
#    display.show()
>>>>>>> 0354d405fade6ed35332b14c167fd62de4956acb:main.py
