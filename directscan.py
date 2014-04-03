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

    
class dirScan():
	def direc (self):
		Tk().withdraw() #removes the root window from TK gui
		directory = askdirectory() #stores user input directory
		finalfiles = [] #sets up for file list
		finalnames = [] #sets up for names list
		for folder, subs, files in os.walk(directory): #for everything in the directory
			for filename in files: #for all files
				finalfiles.append(os.path.join(folder,filename))#create list of file locations
				finalnames.append(filename)#create list of file names
		self.sha(finalnames, finalfiles)#move to next function with 2 arguments

		
	def sha(self, finalnames, finalfiles):
		BLOCKSIZE = 65536 #creates a chunk to work with
		checkSum = [] #creates list to work with
		for f in range(len(finalnames)): #for the num of files in filenames
			hasher = hashlib.sha1() #creates an object for hashing with SHA1
			with open(finalfiles[f], 'rb') as afile: #open in binary mode
				buf = afile.read(BLOCKSIZE) #read file up to chunksize
				while len(buf) > 0: #while the chunk is bigger than 0
					hasher.update(buf) #update the hash
					buf = afile.read(BLOCKSIZE) #read next chunk
			checkSum.append(hasher.hexdigest()) #update checkSum list with a hash
		self.direcScan(finalnames, checkSum) #move onto next function
		
			
	def direcScan(self, finalnames ,checkSum):
		clr=operations() #Creates object for clear screen
		print "We have found ",len(finalnames)," files in that directory"
		go = raw_input ("Press enter to carry on") #user input
		clr.clear()#clear screen
		print "These are your files \n"
		for allf in finalnames: #for all finalnames
			print allf #print them
		print "\nWould you like to scan them?\n"
		print "Yes = Scan files for viruses"
		print "No = Program will exit\n"
		yesno = raw_input ("Please enter Yes or No\n") #user input
		if yesno.lower() == 'yes': #if user enteres yes
			clr.clear() #clear screen
			for allcheck in range(len(checkSum)): #for all of the SHA1 hashes
				#TOTAL VIRUS API START, uses hashes and API key to work
				url = "https://www.virustotal.com/vtapi/v2/file/report"
				parameters = {"resource": checkSum[allcheck], "apikey": "241cb831ad128122acf2fdca69f02019998bf37c19201c86504229ef34600621"}
				data = urllib.urlencode(parameters)
				req = urllib2.Request(url, data)
				response = urllib2.urlopen(req)
				json = response.read()
				response_dict = simplejson.loads(json)
				decider = response_dict.get("response_code", {}) #Grabs reponse code from API
				if decider == 0: #if it is 0 do below
					print "This item isn't in the database"
					print "Be careful as this could have a virus"
					exiting = raw_input ("Press enter to continue")
				else: #if it is not 0 do below
					if response_dict.get("positives", {}) == 0: #checks for items in the database that aren't viruses
						print "This item is clean as a whistle"
						go = raw_input ("Press enter to continue")
					else: #must be a virus do below
						numOf = response_dict.get("positives", {}) #stores number of positive viruses
						alert = "There are", numOf, "positives to this file" #sets up alert
						easygui.msgbox(alert, title="Alert, virus found") #Brings up a GUI alert if virus is found
						print "Start of Details:\n"
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
						print "\nEnd of Details\n"
						cont = raw_input ("\nPress enter to continue")
			print "\nScanning has completed\n"
			print "Thank you for using the Turvey Virus Scanner\n"
			print "Don't forget to delete the malicious files!"
			exiting = raw_input ("\nPress enter to end the program")
			sys.exit() #exits the program
		elif yesno.lower() == 'no':
			exiting = raw_input ("\nPress enter to end the program")
			sys.exit() #exits the program
		else:
			clr.clear() #clear screen
			print "You need to enter Yes or No\n"
			#if not yes or no, go back to start
			self.direcScan(finalnames, checkSum)
