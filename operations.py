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

import os #for use of os. item

class operations():
	def clear(self):
		#if the os is nt use cls else use clear
		#cross compatibility
		os.system('cls' if os.name == 'nt' else 'clear')
	
