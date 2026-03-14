# Fix for lines on PNG files generated from tecplot:
from PIL import Image
for i in range(360):
    filename = ('assembly_%g.png' % i)
    try:
        img = Image.open(filename)
        size = img.size
        coords = [size[0]-2, size[1]-2,0,0]
        cropped = img.crop(coords)
        cropped.save(filename)
    except:
        print "clipping", filename
        pass
