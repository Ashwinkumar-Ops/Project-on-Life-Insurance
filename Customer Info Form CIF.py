# Customer Information Form (CIF) for Life Insurance Customer

from datetime import date

today = date.today()

print("Session Date: ", today.strftime("%d-%m-%Y"))

import time

print("+"+30*"-"+"+")
print(("|"+" "*30+"|\n")*1,end="")
print(("|"+" "*6+"-"*18+" "*6+"|\n"),end="")
print(("|"+" "*6+"SUN LIFE INSURANCE"+" "*6+"|\n"),end="")
print(("|"+" "*6+"-"*18+" "*6+"|\n"),end="")
print(("|"+" "*30+"|\n")*1,end="")
print("+"+30*"-"+"+")

# Design for Health Details Details Section
print(("|"+"+"*16+"-"*40+"+"*15+"|\n"),end="")
print(("|"+" "*20+"FAMILY & HEALTH DETAILS SECTION"+" "*20+"|\n"),end="")
print(("|"+"+"*16+"-"*40+"+"*15+"|\n"),end="")


time.sleep(2)

print("\n")

#Code for Input data -- Start

fname = input("First Name: ")
mname = input("Middle Name: ")
lname = input("Last Name: ")

print("\n")

date_birth = input("Date of Birth: (DD-MM-YYYY)\n")

print("\n")

age = int(input("Age: ")) #This needs to be automated based on System date

print("\n")


perm_add_line1 = input("Permanent Address \nLine1: ")
perm_add_line2 = input("Line2: ")
perm_add_line3 = input("Line3: ")
perm_town = input("Town / City: ")
perm_state = input("State: ")
perm_country = input("Country: ")

time.sleep(2)

comm_add = input("Is communication address & permanent address different ? : (Y / N) : ")

if comm_add == "N":
    comm_add_line1 = perm_add_line1
    comm_add_line2 = perm_add_line2
    comm_add_line3 = perm_add_line3
    comm_town = perm_town
    comm_state = perm_state
    comm_country = perm_country

else:
    comm_add_line1 = input("Communication Address \nLine1: ")
    comm_add_line2 = input("Line2: ")
    comm_add_line3 = input("Line3: ")
    comm_town = input("Town / City: ")
    comm_state = input("State: ")
    comm_country = input("Country: ")

print("\n")

mobnum = int(input("Mobile Number: ")) #Mobile number 

print("\n")

email = input("Email Address: ") #Email Address 

print("\n")

time.sleep(5)


#-----------------Modification Section--pd: Personal Details-----------------------------------------

modify_pd = input("Please confirm if any modification in data is required: Y / N: ")

if modify_pd == "Y" or modify_pd == "y" :
    
    ques_fname = input("Modification required in First Name ? Y / N: ")
    if ques_fname == "Y" or ques_fname == "y":
        fname = input("First Name: ")

    ques_mname = input("Modification required in Middle Name ? Y / N: ")
    if ques_mname == "Y" or ques_mname == "y":
        mname = input("Middle Name: ")

    ques_lname = input("Modification required in Last Name? Y / N: ")
    if ques_lname == "Y" or ques_lname == "y":
        lname = input("Last Name: ")


    
    #x = input("Please provide a value for x: ")
    #y = input("Please provide a value for y: ")

    #print("Value of X is ",x ,"\nValue of Y is ",y)

#else:
    #print("Value of X is ",x ,"\nValue of Y is ",y)

#-----------------Modification Section-----------------------------------------------------------------

#Code for Output data -- Start

# Design for Personal Details Section
print(("|"+"+"*14+"-"*40+"+"*14+"|\n"),end="")
print(("|"+" "*20+"PERSONAL INFORMATION SECTION"+" "*20+"|\n"),end="")
print(("|"+"+"*14+"-"*40+"+"*14+"|\n"),end="")

print("Thank you ",fname, mname, lname,sep=".",end=".\n")

print("\n")

print("Please review & confirm all the below details are correct.",sep="",end="\n")

time.sleep(1)

print()

print("Date of Birth: ", date_birth,"\n", "Age: ", age)

time.sleep(1)

# Design for Address & Comm Details Section
print(("|"+"+"*16+"-"*40+"+"*15+"|\n"),end="")
print(("|"+" "*20+"ADDRESS & COMMUNICATION SECTION"+" "*20+"|\n"),end="")
print(("|"+"+"*16+"-"*40+"+"*15+"|\n"),end="")


print(perm_add_line1,perm_add_line2,perm_add_line3,perm_town,perm_state,perm_country,sep="\n",end="|")

print()

if comm_add != "N":

    print(comm_add_line1,comm_add_line2,comm_add_line3,comm_town,comm_state,comm_country,sep="\n",end="|")

    time.sleep(1)

else:
    print("Permanent and Communication Address is same.")

time.sleep(1)

print()

print("Mobile Number: ",mobnum)

print()

print("Email Address: ",email)

print()

print("+"+30*"-"+"+")
print(("|"+" "*30+"|\n")*1,end="")
print(("|"+" "*6+"-"*18+" "*6+"|\n"),end="")
print(("|"+" "*6+"SUN LIFE INSURANCE"+" "*6+"|\n"),end="")
print(("|"+" "*6+"-"*18+" "*6+"|\n"),end="")
print(("|"+" "*6+"-"*7+"SEAL"+"-"*7+" "*6+"|\n"),end="")
print(("|"+" "*6+"-"*18+" "*6+"|\n"),end="")
print(("|"+" "*30+"|\n")*1,end="")
print("+"+30*"-"+"+")



#Coding date 08/02/2022 - Ashwinkumar D Basari

    

