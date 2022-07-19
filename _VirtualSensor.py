#
from PIL import Image
import numpy as np

##
print("(test.jpg) File : ")
name = input()
if(name == ""):
    name = "test.jpg"
print("")
print("Image = "+str(name))

##
pictur = Image.open(str(name))
width, height = pictur.size
##

print("")
print("Binning Faktor (even subdivide from width and height): ")
faktor = int(input())

if(width % int(faktor) != 0):
    print("")
    print("Faktor is not an even divisor!!!")
    print("")
    print("Faktor is now [2]")
    faktor = 2

print("")
print("Faktor = "+str(faktor))

print("")
print("Converting ["+str(name)+"] with a faktor of ["+str(faktor)+"]...")


pixel_w = int(width / faktor)
pixel_h = int(height / faktor)

print("")
print(height)
print("")

print("")
print("Size: "+str(pixel_w)+" x "+str(pixel_h))


tmp_gesR = 0
tmp_gesG = 0
tmp_gesB = 0
tmp_ges = tmp_gesR, tmp_gesG, tmp_gesB
tmp_tmp_gesR = 0
tmp_tmp_gesG = 0
tmp_tmp_gesB = 0

newimgarray = np.zeros((pixel_h, pixel_w, 3))


#select main pixel
for y in range( pixel_h ):

	for x in range( pixel_w ):

		#get pixel value from 0.0, from 0.+1, from +1.0, from +1.+1
		tmp_tmp_gesR = 0
		tmp_tmp_gesG = 0
		tmp_tmp_gesB = 0

		xtmp,ytmp = x*faktor,y*faktor


		for i in range(faktor):
			for j in range(faktor):
				
				tmp_gesR, tmp_gesG, tmp_gesB = pictur.getpixel((xtmp+i,ytmp+j)) 
				tmp_tmp_gesR, tmp_tmp_gesG, tmp_tmp_gesB = tmp_tmp_gesR + tmp_gesR, tmp_tmp_gesG + tmp_gesG, tmp_tmp_gesB + tmp_gesB

		newimgarray[y][x][0] = tmp_tmp_gesR
		newimgarray[y][x][1] = tmp_tmp_gesG
		newimgarray[y][x][2] = tmp_tmp_gesB
##
Image.fromarray((newimgarray).astype('uint8'), mode='RGB').save(str(name)+'_x'+str(faktor)+'_Vsensor.png')

print("Done...")
input()