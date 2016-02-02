;
Student_data="""
    
    1. New Data
    2. Quit"""
print Student_data

aa={

	'Name':'kiran',
 	'Class': 'B.tech',
 	'Address': 'Una',
 	'Rollno': 1
}

print"@"*20
bb={
 	'Name':'Divya',
 	'Class':'B.tech',
 	'Address':'Mohali',
 	'Rollno': 2,
}

mydict={
	1: aa,
	2: bb,
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
    continue
    if choice==2:
        print 2
    break




