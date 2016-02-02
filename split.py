def main_function():
    main()
    header()
    
def main():
    print""" 
    1.simple
    2.Reverse"""
   
    
def header():
    a=raw_input("Enter your first string:->")
    b=raw_input("Enter your Second string:->")
    choice(a,b)
def choice (a,b):
    choice=input("enter choice:->")
    
    
    if  choice==1:
        print a+b
    else:
        print b+a
    
main_function() 
