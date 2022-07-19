# VirtualSensor

O(n^2) for side length or O(n) for Pixel count
and O((1/n^root(faktor))^root(faktor))

Pixel Binning to create brighter Images with a lot of detail

Bugs:
-cant use subfolder
-too bright will get artifacts(so have the images 1/faktor as dark as maximum)

## How to install

1. Run: `pip install -r requirements.txt`


## How to use
0. convert picture(best lossless formats) to png(jpg is working, but has compressions)
1. put picture in same folder as _VirtualSensor.py
2. run _VirtualSensor.py
