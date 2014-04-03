#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    COPYRIGHT LUKE TURVEY (C) 2014
    
    This file is part of The Turvey Virus Scanner(TVS).

	TVS is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    TVS is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with TVS.  If not, see <http://www.gnu.org/licenses/>.
""" 

import json as simplejson #for VirusTotal API
import urllib #for VirusTotal API
import urllib2 #for VirusTotal API
import hashlib #for MD5

import easygui #used for GUI things
from Tkinter import Tk #used for GUI things
from tkFileDialog import *  #used for GUI things

import sys #To use sys. items
import os  #To use os. items
from operations import operations #Imports class to clear screen

    
class fileScan():
	def sha(self):
		Tk().withdraw() #removes the root window from TK gui
		chosenfile = askopenfilename() #stores user input directory
		
		BLOCKSIZE = 65536 #creates a chunk to work with
		hasher = hashlib.sha1() #creates an object for hashing with SHA1
		with open(chosenfile, 'rb') as afile: #open in binary mode
			buf = afile.read(BLOCKSIZE) #read file up to chunksize
			while len(buf) > 0: #while the chunk is bigger than 0
				hasher.update(buf) #update the hash
				buf = afile.read(BLOCKSIZE) #read next chunk
		checkSum = hasher.hexdigest() #update checkSum list with a hash
		self.Scanner(chosenfile, checkSum) #move onto next function
	
	def Scanner(self, chosenfile ,checkSum):
		#using TotalVirus API to do what I need
		url = "https://www.virustotal.com/vtapi/v2/file/report"
		parameters = {"resource": checkSum, "apikey": "241cb831ad128122acf2fdca69f02019998bf37c19201c86504229ef34600621"}
		data = urllib.urlencode(parameters)
		req = urllib2.Request(url, data)
		response = urllib2.urlopen(req)
		json = response.read()
		response_dict = simplejson.loads(json)
		decider = response_dict.get("response_code", {}) #Grabs reponse code from API
		if decider == 0: #if it is 0 do below
			print "This item isn't in the database"
			print "Be careful as this could have a virus"
			exiting = raw_input ("Press enter to exit the program")
			sys.exit() #exit the program
		else:
			if response_dict.get("response_code", {}) == 0: #checks for items in the database that aren't viruses
				print "This file is Virus Free and comes with no Warnings"
			else:
				numOf = response_dict.get("positives", {}) #stores number of positive viruses
				alert = "There are", numOf, "positives to this file" #sets up alert
				easygui.msgbox(alert, title="Alert, virus found") #Brings up a GUI alert if virus is found
				print 
				print 'Kaspersky Says:'
				print "Virus name:"
				#finds the scan result information for kaspersky
				print response_dict.get("scans", {}).get("kaspersky", {}).get("result")
				print '\nNod32 Says:'
				print "Virus name:"
				#finds the scan result information for NOD32
				print response_dict.get("scans", {}).get("NOD32", {}).get("result")
				print '\nClamAV Says:'
				print "Virus name:"
				#finds the scan result information for ClamAV
				print response_dict.get("scans", {}).get("ClamAV", {}).get("result")
				print '\nSophos Says:'
				print "Virus name:"
				#finds the scan result information for Sophos
				print response_dict.get("scans", {}).get("Sophos", {}).get("result")
				print '\nMcAfee Says:'
				print "Virus name:"
				#finds the scan result information for McAfee
				print response_dict.get("scans", {}).get("McAfee", {}).get("result")
				print "\nDon't see a result above but do get an alert with positives found?"
				print "It could be a false positive, be careful!"
				cont = raw_input ("\nPress enter to continue")
				self.delete(chosenfile) #Run delete class and bring file location
		
	def delete(self, chosenfile):
		clr=operations() #object for clear screen
		clr.clear() #clears screen
		print "\nFile location: ", chosenfile, "\n"
		print "Would you like to delete the file?"
		print "yes = File will be deleted"
		print "no = Program will close\n"
		keepDel = raw_input ("Please choose yes or no\n")
		if keepDel.lower() == 'yes':
			clr.clear() #clears screen
			os.remove(chosenfile) #deletes file in variable
			print "File has been deleted, threat eliminated"
		elif keepDel.lower() == 'no':
			sys.exit() #exits the program
		else:
			print "You need to type yes or no!"
			self.delete(chosenfile) #Go back untill an option is picked and remember the file location

		
	


