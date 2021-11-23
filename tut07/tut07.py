import os
import pandas as pd

dict_main={}
ltp_dict={}

def check(dict_registered,dict_submitted,roll):
	if roll in dict_registered:
		temp=dict_registered[roll].copy()
		s=[]
		if(len(temp)!=len(dict_submitted)):
			
			for i in temp:
				x=ltp_dict[i]
	
				if dict_submitted.count(i)!=x[0][1]:
					if temp.count(i)!=x[0][1]:
						diff=x[0][1]-temp.count(i)
						while diff>0:
							s.append(i)
							diff=diff-1
				s.append(i)
			
			for j in dict_submitted:
				x=ltp_dict[j]
				if j in s:
					s.remove(j)
			e=len(s)		
			if e!=0:		
				if roll not in dict_main:
					dict_main[roll]=[]
					dict_main[roll].append(s)
					
				else:
					dict_main[roll].append(s)
					
				return roll
	

def number_of_bits(s):
	    

		cnt=0
		zr=0
		k=len(s)
		
		for j in range(k):
			if((s[j])=='0'):
				zr=zr+1
			
		cnt=3-zr
		return cnt


def feedback_not_submitted():

	
	ltp_mapping_feedback_type = {1: 'lecture', 2: 'tutorial', 3:'practical'}
	output_file_name = "course_feedback_remaining.xlsx" 
	registered_file=pd.read_csv('course_registered_by_all_students.csv')
	registered_roll=registered_file['rollno'].values.tolist()
	registered_data=registered_file[['register_sem','schedule_sem','subno']].values.tolist()
	registered_sub=registered_file['subno'].values.tolist()
	
	unique_registered_roll=set(registered_roll)
	dict_registered={}
	
	x=0
	for k in registered_roll:
		if k not in dict_registered:
			dict_registered[k]=[]
			dict_registered[k].append(registered_sub[x])
			
		else:
			dict_registered[k].append(registered_sub[x])
			
		
		x=x+1
	
	c=0
	registered_data_dict={}
	for k in registered_sub:
		registered_data_dict[k]=[]
		registered_data_dict[k]=registered_data[c]
		c=c+1

	
	submitted_file=pd.read_csv("course_feedback_submitted_by_students.csv")
	submitted_sub=submitted_file['course_code'].values.tolist()
	submitted_roll=submitted_file['stud_roll'].values.tolist()
	unique_submitted_roll=set(submitted_file)
	dict_submitted={}

	d=0
	for k in submitted_roll:
		if k not in dict_submitted:
			dict_submitted[k]=[]
			dict_submitted[k].append(submitted_sub[d])
			
		else:
			dict_submitted[k].append(submitted_sub[d])
			
		d=d+1

	
	info_file=pd.read_csv('studentinfo.csv')
	ltp_file=pd.read_csv('course_master_dont_open_in_excel.csv')
	
	ltp_list=ltp_file['ltp'].values.tolist()
	ltp_sub=ltp_file['subno'].values.tolist()
	
	


	f=0
	for k in ltp_sub:
		bits=number_of_bits(ltp_list[f])
		if k not in ltp_dict:
			ltp_dict[k]=[]
			ltp_dict[k].append([ltp_list[f],bits])
			
		else:
			ltp_dict[k].append([ltp_list[f],bits])
			
		
		f=f+1
	
	info_list=info_file[['Name','email','aemail','contact']].values.tolist()
	info_roll=info_file['Roll No'].values.tolist()

	dict_info={}

	g=0
	for k in info_roll:
		if k not in dict_info:
			dict_info[k]=[]
			dict_info[k].append(info_list[g])
			
		else:
			dict_info[k].append(info_list[g])
		
		g=g+1


	
	for i in unique_registered_roll:
		if i in dict_submitted:
			temp=check(dict_registered,dict_submitted[i],i)


	
	
	output_list=[[]]
	for i in dict_main:
		for j in dict_main[i]:
			
			
			for k in j:
				x=[]
				x.append(i)
				
			
				x.extend(registered_data_dict[k])
				p=dict_info[i]
				
				for l in range(4):
					x.append(p[0][l])
				print(x)
				
				output_list.append(x)
	
	output_data=pd.DataFrame(output_list,columns=['rollno','register_sem','schedule_sem','subno','Name','email','aemail','contact'])
	output_data.to_excel(output_file_name)
	print(output_data.head())

feedback_not_submitted()