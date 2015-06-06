#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pdfsplitandpdf.py
#  
#  Copyright 2014 pepcio <piotrk0303@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from scipy import misc as spm
from scipy import ndimage
import scipy as sp
from wand.image import Image
from PIL import Image as pimage
from wand.display import display
from pyPdf import PdfFileWriter,PdfFileReader
#~ import matplotlib.pyplot as plt
#~ from skimage import data, filter
#~ from pytesseract import image_to_string

def proguj(ob, prog):
    ob_wyj = sp.zeros(ob.shape)
    ob_wyj[sp.where(ob>prog)]=1
    return ob_wyj

def main():
	
	output = PdfFileWriter()
	temp = PdfFileReader(file('org.pdf','rb'))
	#~ #numeracja
	for i in range(0,(temp.getNumPages()-1)):
		if i<10:
			w = '00'+str(i)
		elif i>=10 and i<100:
			w = '0'+str(i)
		elif i>=100 and i<1000:
			w = str(i)
		#wczytanie strony pdf 
	#~ i = 10
		img = Image(filename="org.pdf[" + str(i) + "]", resolution=300)
		img.type = 'bilevel';
		imga = img[:(int(img.width/2)),:]
		#~ print imga.make_blob()
		imgb = img[(int(img.width/2)):,:]
		#~ display(imga)
	#~ img1 = imga[500:750,500:750]
	#~ imga.save(filename="temp/temp1.png")
	
	#~ img1 = ndimage.imread('temp/temp1.png')
	#~ print image_to_string(pimage.open('temp/temp1.png'),lang='pol')
	
	#~ img3 = ndimage.binary_erosion(img1, structure = el).astype(img1.dtype)
	#~ img2 = ndimage.median_filter(img1, 20)
	#~ print dir(img2)
	#~ spm.imsave("temp/temp2.png",img2)
	#######Histogram
	#~ plt.figure('histogram szarosci')
	#~ plt.hist(img1.ravel(),255) # narysujmy histogram odcieni
	#~ plt.show()
	########
	#~ spm.imsave("temp/temp3.png",img3)
	
		#~ #tworzenie pdf z podzielonych stron
		for j in 'a','b':
			if j == 'a':
				imga.save(filename="temp/temp.pdf")
			if j == 'b':
				imgb.save(filename="temp/temp.pdf")
			temp = PdfFileReader(file('temp/temp.pdf','rb'))
			output.addPage(temp.getPage(0))
			outputStream = file("outputa.pdf", "wb")	
			output.write(outputStream)
			outputStream.close()
		print i
	return 0

if __name__ == '__main__':
	main()

