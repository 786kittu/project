Student_data="""
    
    1. Search
    2. Edit
    3. Quit"""
print Student_data
print"*"*20
aa={

	'Name':'kiran',
 	'Class': 'B.tech',
 	'Address': 'Una',
 	'Roll no': 1
}
bb={
 	'Name':'Divya',
 	'Class':'B.tech',
 	'Address': 'Mohali',
 	'Roll no': 2
}
choice=input("Enter your choice:")

while choice==1:
    
    a=input("enter your roll no.:")
    try:
        tmp = mydict[a]
	
	print "Name:",tmp['Name']
	print "Class:",tmp['Class']
	print "Address:",tmp['Address']
	
    except:
        print "Non-available"
        
    if choice==2:
        b=raw_input("What You want to edit ?")
    elif b==Name:
	 	
    
