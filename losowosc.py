#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bez nazwy.py
#  
#  Copyright 2014 pepcio03 <piotrk0303@gmail.com>
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

import random
import math as m
import scipy as sp

def main():

	liczbaosob = 100
	osobylista = range(0,liczbaosob)
	osoby = []
	for l in osobylista:
		osoby.append([])
	#~ print osoby
		
	symptomy = ["s1","s2","s3","s4","s5","s6"]
	procentsymp = [0.70,0.64,0.50,0.45,0.23,0.05]
	
	i = 0;
	
	for symptom in symptomy:
		alist = random.sample(osobylista,int(liczbaosob*procentsymp[i]));
		alist.sort();
		i = i + 1;
		#~ print symptom , alist;
		for osb in alist:
				osoby[osb].append(symptom)

	for iosoba in osobylista:	
		print "Osoba %d" % (iosoba+1), osoby[iosoba]
	
	return 0

if __name__ == '__main__':
	main()
