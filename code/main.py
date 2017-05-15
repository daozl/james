#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
if __name__ == '__main__':
    while True:
        commond = raw_input("""
		  Please input what data you about	

	A: male to female ratio			B: Grade ratio
	C: professional ratio			D: Work unit type
	E: job industry category		F: The area that work belongs 
	G: Working city level			H: work and professional consistency 
	I: the main reason for professional disagreement	
	J: the first salary and the current salary situation
	K: get the first working hours 
	L: the problems faced in the employment process 
	M: awareness of the profession		N: teacher level satisfaction 
	O: Professional disciplines help with employment 	
	P: Reasonable setting of course		Q: exit 

	: """)
        if commond == 'A':
	        os.system("python pie/SexScale.py")
        elif commond == 'B':
	        os.system("python bar/grade.py")
        elif commond == 'C':
	        os.system("python pie/Professional.py")
        elif commond == 'D':
	        os.system("python bar/company.py")
        elif commond == 'E':
	        os.system("python pie/JobCategory.py")
        elif commond == 'F':
	        os.system("python bar/area.py")
        elif commond == 'G':
	        os.system("python bar/AreaLevel.py")
        elif commond == 'H':
	        os.system("python bar/consistent.py")
        elif commond == 'I':
	        os.system("python bar/reason.py")
        elif commond == 'J':
	        os.system("python bar/salary.py")
        elif commond == 'K':
	        os.system("python pie/FirstJob.py")
        elif commond == 'L':
	        os.system("python bar/problem.py")
        elif commond == 'M': 
	        os.system("python pie/ProKnowldege.py")
        elif commond == 'N': 
	        os.system("python pie/teacher.py")
        elif commond == 'O': 
	        os.system("python pie/course.py")
        elif commond == 'P': 
	        os.system("python pie/curriculum.py")
        elif commond == 'Q':
            break
        else:
            print """
					Your input is error! Please input again!
				
				"""


























