import re
import glob
import Image
from PIL.ExifTags import TAGS

def resize_file(name,append_name,ext,percentage,folder):
	# open an image file (.bmp,.jpg,.png,.gif) you have in the working folder
	im1 = Image.open(name + ext)
        im1 = rotate_upright(im1)
        ret = {}
        info =  im1._getexif()
        for tag, value in info.items():
           decoded = TAGS.get(tag, tag)
           if decoded == "Orientation": 
              print value
           
	#(width,height) = im1.size
	#print im1.size
	#height = int(height * percentage)
	#width = int(width * percentage)
	#im2 = im1.resize((width,height), Image.NEAREST)
	#print im2.size
	#im2 = im2.rotate(90) #dunno why.
	#im2.save("./" + folder + "/" + name + append_name + ext)
def rotate_upright(img):
   ret = {}
   info =  img._getexif()
   for tag, value in info.items():
      decoded = TAGS.get(tag, tag)
      if decoded == "Orientation": 
         orientation = value
         #print "before:" + str(value)
   if orientation is 6: img = img.rotate(-90)
   elif orientation is 8:
      img = img.rotate(90)
      print type(img)
      print orientation
   elif orientation is 3: img = img.rotate(180)
   elif orientation is 2: img = img.transpose(Image.FLIP_LEFT_RIGHT)
   elif orientation is 5: img = img.rotate(-90).transpose(Image.FLIP_LEFT_RIGHT)
   elif orientation is 7: img = img.rotate(90).transpose(Image.FLIP_LEFT_RIGHT)
   elif orientation is 4: img = img.rotate(180).transpose(Image.FLIP_LEFT_RIGHT)
   print type(img)
   ret = {}
   info =  img._getexif()
   for tag, value in info.items():
      decoded = TAGS.get(tag, tag)
      if decoded == "Orientation": 
         orientation = value
         print "before:" + str(value)
   return img
# loop through all files
files = glob.glob("*.[jJ][pP][gG]")
print files
for file_ in files:
   print file_
   m = re.search("(.*)(.jpg|.JPG)",file_)
   if m:
     resize_file(m.group(1),"_resized",m.group(2), .4, "Resized")
