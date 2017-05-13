#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
if __name__ == '__main__':
    while True:
        commond = raw_input("""
									请输入你关心的数据	

						A	男女比例
						B	年级比例
						C	专业比例
						D	工作单位类型
						E	工作行业类别
						F	就业单位所属地区
						G	就业单位所属区域级别
						H	工作与专业的吻合度
						I	专业不对口的主要原因
						J	第一份薪资和目前薪资情况
						K	获得第一份工作的时间
						L	就业过程中面临的问题
						M	对专业的认知
						N	师资水平满意度
						O	专业学科对就业的帮助
						P	课程设置合理情况
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
        elif commond == 'exit':
            break
        else:
            print """
						您输入的有错，请重新输入！						
				 
				 """


























