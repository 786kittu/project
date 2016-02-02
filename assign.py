
amount=raw_input("Enter total amount for your online shopping ?")
Country="""
1. Canada
2. US """
print Country
choice=input("Enter the shipping country name:->")
if choice==2 and amount>=50:
    print("shipping cost is $6.00")
elif amount>=100:
    print("shipping cost is $9.00")
elif amount>=150:
    print("shipping cost is $12.00")
else:
    print("shipping is free")
if choice==1 and amount>=50:
    print("shipping cost is $8.00")