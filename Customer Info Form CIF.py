# Customer Information Form (CIF) for Life Insurance Customer

from datetime import date

today = date.today()

print("Session Date: ", today.strftime("%d-%m-%Y"))

import time

print("""
||||~-----------------------------------------------------------------------------------------ab~||||
||||~********************SUN LIFE INSURANCE COMPANY PVT LTD*************************************~||||
||||~-------------------------------------------------------------------------------------------~||||
||||~-------------------------------------------------------------------------------------------~||||
||||~********We Insure Life to Protect People You Love After You********************************~||||
||||~-------------------------------------------------------------------------------------------~||||
        """)

# Design for APPLICATION FORM
print("""
||||~-------------------------------------------------------------------------------------------~||||
||||~**************************** APPLICATION FORM *********************************************~||||
||||~-------------------------------------------------------------------------------------------~||||
        """)


time.sleep(1)

# Design for PERSONAL DETAILS SECTIONS Section
print("""
||||~-----------------------------------~||||
||||~**PERSONAL DETAILS SECTION*********~||||
||||~-----------------------------------~||||
        """)


print("\n")

#Code for Input data -- Start

fname = input("First Name: ")
mname = input("Middle Name: ")
lname = input("Last Name: ")

print("\n")

date_birth = input("Date of Birth: (DD-MM-YYYY): ")

print("\n")

age = int(input("Age (N): ")) #This needs to be automated based on System date

print("\n")

perm_add_line1 = input("Permanent Address: \nLine1: ")
perm_add_line2 = input("Line2: ")
perm_add_line3 = input("Line3: ")
perm_town = input("Town / City: ")
perm_pin = input("Pin Code: ")
perm_state = input("State: ")
perm_country = input("Country: ")

time.sleep(1)

print("\n")

comm_add = input("Is communication address & permanent address different ?\n(Y- To Enter different Comm. Address / N - For same address ) : ")

if comm_add == "N" or comm_add == "n":
    comm_add_line1 = perm_add_line1
    comm_add_line2 = perm_add_line2
    comm_add_line3 = perm_add_line3
    comm_town = perm_town
    comm_pin = perm_pin
    comm_state = perm_state
    comm_country = perm_country

else:
    comm_add_line1 = input("Communication Address: \nLine1: ")
    comm_add_line2 = input("Line2: ")
    comm_add_line3 = input("Line3: ")
    comm_town = input("Town / City: ")
    comm_pin = input("Pin Code: ")
    comm_state = input("State: ")
    comm_country = input("Country: ")
    print("\n")

print("\n")

mobnum = int(input("Mobile Number (N): ")) #Mobile number

print("\n")

email = input("Email Address: ") #Email Address 

print("\n")

time.sleep(1)

#-----------------Modification Section--pd: Personal Details-----------------------------------------

print("""
-------------------------------------------------------------------------------------------------
********************************** Verification of Details **************************************
-------------------------------------------------------------------------------------------------
      """)

print("\n")

print("Please review & confirm all the below details are correct.",sep="",end="\n")

print("-----CONFIRM FOR ANY MODIFICATION IN PERSONAL DETAILS------")

modify_pd = input("Please confirm if any modification in data is required: Y / N: ")

mod_count=0


while modify_pd == "Y" or modify_pd == "y" : #if modify_pd == "Y" or modify_pd == "y" :
    
    ques_fname = input("Modification required in First Name ? Y / N: ")

    if ques_fname == "Y" or ques_fname == "y":
        fname = input("First Name: ")
        print("First Name:",fname)
        mod_count +=1
        print("\n")

    ques_mname = input("Modification required in Middle Name ? Y / N: ")

    if ques_mname == "Y" or ques_mname == "y":
        mname = input("Middle Name: ")
        print("Middle Name:",mname)
        mod_count +=1
        print("\n")

    ques_lname = input("Modification required in Last Name ? Y / N: ")

    if ques_lname == "Y" or ques_lname == "y":
        lname = input("Last Name: ")
        print("Last Name:",lname)
        mod_count +=1
        print("\n")

    ques_dob = input("Modification required in Date of Birth ? Y / N: ")

    if ques_dob == "Y" or ques_dob == "y":
        date_birth = input("Date of Birth: (DD-MM-YYYY)\n")
        mod_count +=1
        print("\n")

    print("\n")

    print("-----RECONFIRM FOR FURTHER MODIFICATION------")

    modify_pd = input("Please confirm if any modification in data is required: Y / N: ")

print("\n")

print("**********************", "Count of Modifications: ", mod_count, "**********************")

#Code for Output data -- Start
print("\n")
# Design for Personal Details Section
print(("|"+"+"*14+"-"*40+"+"*14+"|\n"),end="")
print(("|"+" "*20+"PERSONAL INFORMATION SECTION"+" "*20+"|\n"),end="")
print(("|"+"+"*14+"-"*40+"+"*14+"|\n"),end="")

print("\n")

print("Thank you ",fname, mname, lname,sep=" ",end=".\n")

print("\n")

time.sleep(1)

print("Date of Birth: ", date_birth,"\nAge: ", age,"years")

time.sleep(1)

print("\n")

# Design for Address & Comm Details Section
print(("|"+"+"*16+"-"*40+"+"*15+"|\n"),end="")
print(("|"+" "*20+"ADDRESS & COMMUNICATION SECTION"+" "*20+"|\n"),end="")
print(("|"+"+"*16+"-"*40+"+"*15+"|\n"),end="")

print("\n")

print("Permanent Address",perm_add_line1,perm_add_line2,perm_add_line3,perm_town,perm_pin,perm_state,perm_country,sep="\n",end="|\n")

print("\n")

if comm_add != "N":

    print("Communication Address",comm_add_line1,comm_add_line2,comm_add_line3,comm_town,comm_pin,comm_state,comm_country,sep="\n",end="\n")

    time.sleep(1)

else:
    print("Permanent and Communication Address is same.")

time.sleep(1)

print("Mobile Number: ",mobnum,end="\n")

print("\n")

print("Email Address: ",email,end="\n")

print("\n")


# Design for Health Details Section
print(("|"+"+"*16+"-"*40+"+"*15+"|\n"),end="")
print(("|"+" "*20+"FAMILY & HEALTH DETAILS SECTION"+" "*20+"|\n"),end="")
print(("|"+"+"*16+"-"*40+"+"*15+"|\n"),end="")

print("\n")

weight = int(input("Weight - in kgs: "))

height = int(input("Height - in cms: "))

height = height / 100 #Height to be divide by 100 got Body Mass Index (BMI).

bmi = (weight / height)/height

print("Body Mass Index: ",round(bmi))



# Design for Health Details Section
print(("""
|++++++++++++++++----------------------------------------+++++++++++++++|
|                    FAMILY & HEALTH DETAILS SECTION                    |
|++++++++++++++++----------------------------------------+++++++++++++++|
""")

print("\n")

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

    

