#
import time
from PIL import Image
import numpy as np

prot = False
tmp_gesR = 0
tmp_gesG = 0
tmp_gesB = 0
tmp_ges = tmp_gesR, tmp_gesG, tmp_gesB
tmp_tmp_gesR = 0
tmp_tmp_gesG = 0
tmp_tmp_gesB = 0

##
print("(test.jpg) File : ")
name = input()
if(name == ""):
    name = "test.jpg"

##
pictur = Image.open(str(name))
width, height = pictur.size
##

print("")
print("Binning Faktor (even subdivide from width and height): ")
faktor = int(input())

if(width % int(faktor) != 0):
    print("Faktor is not an even divisor!!!")
    print("")
    print("Faktor is now [2]")
    faktor = 2

print("")
print("(y)Artifact protection? y/n:")

tobright = input()
if(tobright == ""):
	prot = True
elif(tobright == "n"):
	prot = False

####
start_time = time.time()
####

print("")
print("Converting ["+str(name)+"] with a faktor of ["+str(faktor)+"]...")


pixel_w = int(width / faktor)
pixel_h = int(height / faktor)


print("")
print("Size: "+str(pixel_w)+" x "+str(pixel_h))


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
		
		#too bright protect
		if((tmp_tmp_gesR or tmp_tmp_gesG or tmp_tmp_gesB) > 255 and prot):
			newimgarray[y][x][0] = tmp_tmp_gesR / (faktor**2)
			newimgarray[y][x][1] = tmp_tmp_gesG / (faktor**2)
			newimgarray[y][x][2] = tmp_tmp_gesB / (faktor**2)
			protected = True
		else:
			newimgarray[y][x][0] = tmp_tmp_gesR
			newimgarray[y][x][1] = tmp_tmp_gesG
			newimgarray[y][x][2] = tmp_tmp_gesB

##
Image.fromarray((newimgarray).astype('uint8'), mode='RGB').save(str(name)+'_x'+str(faktor)+'_Vsensor.png')

####
end_time = time.time()
####
print("Time Elapsed: "+str(end_time-start_time)+"s")
print("Protected: "+str(protected))

print("Done...")
input()