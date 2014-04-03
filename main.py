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
from scanning import fileScan #Imports class to scan single file
from directscan import dirScan #Imports class to scan many files
from operations import operations #Imports class to clear screen
     
                           
def main():
	restart = True #setting up for while loop
	print 'Welcome to the Turvey Virus Scanner \n'
	print 'Your file/s will be scanned with 5 diffrent well known AntiViruses!'
	print 'Please choose what you would like to do \n'
	print '(1) Scan a File for Viruses \n'
	print '(2) Scan a directory for Viruses \n'
	while restart == True: #While restart says True do the below
		Program = raw_input ("Please enter a number 1-2\n") #user input
		if Program == '1': #user chooses 1 do below
			restart = False #change to false to stop a loop
			clr=operations() #setup object for clear screen
			clr.clear() #clear screen
			scan=fileScan() #setup object for single file scan
			scan.sha() #run filescan class
		elif Program == '2': #user chooses 2 do below
			restart = False #change to false to stop a loop
			clr=operations() #setup object for clear screen
			clr.clear() #clear screen
			scantwo=dirScan() #setup object for many file scan
			scantwo.direc() #run filescan class
		else:
			restart = True #change to True to loop, wrong item entered
	

if __name__ == '__main__': #if run from a console run function main
	main()

