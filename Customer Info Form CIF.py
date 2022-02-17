# Customer Information Form (CIF) for Life Insurance Customer

from datetime import date

today = date.today()

print("Session Date: ", today.strftime("%d-%m-%Y"))

import time

print("""
||||~------------------------------------------------------------------------------------------------------------------------------------------------------------ab~||||
||||~**********************************************************USN LYFE INSURANCE COMPANY PVT LTD******************************************************************~||||
||||~--------------------------------------------------------------------------------------------------------------------------------------------------------------~||||
||||~--------------------------------------------------------------------------------------------------------------------------------------------------------------~||||
||||~**************************************************We Insure Life to Protect People You Love After You*********************************************************~||||
||||~--------------------------------------------------------------------------------------------------------------------------------------------------------------~||||
        """)

print("\n")
time.sleep(1)

# Design for APPLICATION FORM
print("""
||||~--------------------------------------------------------------------------------------------------------------------------------------------------------------~||||
||||~********************************************************* APPLICATION FORM ***********************************************************************************~||||
||||~--------------------------------------------------------------------------------------------------------------------------------------------------------------~||||
        """)

print("\n")
time.sleep(1)

# Design for PERSONAL DETAILS SECTIONS Section
print("""
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
************************************************************************************************************************************************************************
||                                                              PERSONAL DETAILS SECTION                                                                              ||
||                                                                                                                                                                    ||
||                                                                                                                                                                    ||
        """)

time.sleep(1)

#Code for Input data -- Start

# ============================================Name Section=========================================================================

print("""
------------------>
NAME OF APPLICANTS >
------------------>
        """)


fname = input("First Name: ")
mname = input("Middle Name: ")
lname = input("Last Name: ")

fname = fname.capitalize()
mname = mname.capitalize()
lname = lname.capitalize()

name = (fname+" "+mname+"."+lname)

print("\nHello ",name,sep=" ",end=".\n")

print("""
------------------------>
APPLICANTS DATE OF BIRTH >
------------------------>
        """)

time.sleep(1)

date_birth = input("Date of Birth: (DD-MM-YYYY): ")

print("""
------------------------>
APPLICANTS AGE           >
------------------------>
        """)


age = int(input("Age (N): ")) #This needs to be automated based on System date

age_stat = "Nill"

if age <= 17:
    age_stat = "Minor"

elif age > 17:
    age_stat = "Major"

print("""
------------------------>
APPLICANTS SEX           >
------------------------>
        """)
time.sleep(1)

#-------------------Code added on 10/02/2022----------------------Ashwinkumar D Basari--------

sex = input("Sex: \nM-Male / F-Female / T-Transgender: ")
sex = sex.upper()
print("\n")
time.sleep(1)

print("""
----------------------------}
APPLICANTS MARITAL STATUS    }
----------------------------}
        """)

mstat = str(input("Marital Status: \nS-Single / M-Married / O-Other: "))   ##Marital status
mstat = mstat.upper()


if mstat == "O" or mstat == "o":

    if mstat == "O" or mstat == "o":
        mstat = input("Please specify Marital Status: ")
        mstat = mstat.upper()

print("""
---------------------------------->
APPLICANTS SALUTATION PREFERENCE   >
---------------------------------->
        """)

salu = 0

risk1 = "No Risk" #risk1 - Legal criteria for Marriage is not met

if age <= 17 and mstat == "M" and sex == "F":
    salu = "Miss"
    risk1 = "risk1 - Female Life - Legal criteria for marriage is not met"

elif age <= 17 and mstat == "M" and sex == "M":
    salu = "Master"
    risk1 = "risk1 - Male Life - Legal criteria for marriage is not met"

elif age >= 18 and mstat == "M" and sex == "F":
    salu = "Mrs."

elif age >= 18 and mstat == "M" and sex == "M":
    salu = "Mr."

elif age >= 18 and mstat == "M" and sex == "T":
    salu = "Mx."


elif salu == 0:
    salu = input("System should consider salutation based on Sex.\nY-Mr for Male & Mrs for Female ELSE N-To provide input from your end: ")
    salu = salu.upper()

    if salu == "Y":
        if sex == "M":
            salu = "Mr."

        elif sex == "F":
            salu = "Mrs."

        elif sex == "T":
            salu = "Mx."


    elif salu == "N":
        salu = input("Please provide desired salutation: ")
        salu = salu.capitalize()

print("\nTHANK YOU FOR DETAILS",salu,name,sep=" ",end=".\n")

time.sleep(1)

#===================Nationality & Residental===============================17022022-AB

print("""
---------------------------------->
                     NATIONALITY   >
---------------------------------->
        """)


n1 = int(input("Nationality: \n0-Indian \n1-Non-Indian\nPlease provide value as per above list : "))

citizen = ["Indian", "Non-Indian"]
print()
print("Nationality: ",citizen[n1])
print("\n")
time.sleep(1)


print("""
---------------------------------->
                RESIDENTAL STATUS  >
---------------------------------->
        """)


n2 = int(input("Residental Status: \n0-Resident \n1-NRI \n2-PIO\nPlease provide value as per above list : "))

res_stat = ["R-Resident","NRI-Non-Resident Indian", "PIO-Person of Indian Origin"]
print()
print("Residental Status: ",res_stat[n2])
print("\n")
time.sleep(1)

#===================Education Qualification & Occupational Details===============================17022022-AB

print("""
---------------------------------->
          EDUCATION QUALIFICATION  >
---------------------------------->
        """)


n3 = int(input("Education Qualification:\n0-Post Graduation\n1-Graduation\n2-Diploma\n3-12th pass\n4-10th Pass\n5-Below 10th\n6-Illiterate \nPlease provide value as per above list: "))

edu = ["Post Graduation","Graduation","Diploma","12th pass","10th Pass","Below 10th","Illiterate"]
print()
print("Education Qualification: ",edu[n3])
time.sleep(2)
print("\n")

print("""
---------------------------------->
                OCCUPATION DETAIL  >
---------------------------------->
        """)

n4 = int(input("Occupation Detail:\n0-Salaried\n1-Professional\n2-Self Employed\n3-Student\n4-Housewife\n5-Retired\n6-Agriculturist\n7-Others \nPlease provide value as per above list:"))

occ = ["Salaried","Professional","Self Employed","Student","Housewife","Retired","Agriculturist","Others"]

occ_oth = "N/A"

if occ[n4] == "Others":

    occ_oth = input("Please specify the details: ")
print()
print("Occupation Detail: ",occ[n4],"|| Occupation Detail for Other catagory: ",occ_oth)
time.sleep(2)
print("\n")

print("""
||                                                                                                                                                                    ||
||                                                                                                                                                                    ||
||                                                              END OF SECTION                                                                                        ||
************************************************************************************************************************************************************************
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        """)
time.sleep(5)


print("""
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
************************************************************************************************************************************************************************
||                                                             EMPLOYMENT DETAILS SECTION                                                                             ||
||                                                                                                                                                                    ||
||                                                                                                                                                                    ||
        """)


#===================Employement Details===============================17022022-AB

print("""
---------------------------------->
            NAME OF ORGANISATION   >
---------------------------------->
        """)

org_nam = input("Name of Organisation: ")
org_nam = org_nam.upper()
print()
print("Name of Organisation: ",org_nam)
time.sleep(1)
print("\n")


print("""
---------------------------------->
            TYPE OF ORGANISATION   >
---------------------------------->
        """)

n5 = int(input("Type of Organisation:\n0-Government\n1-Private Ltd\n2-Public Ltd\n3-Partner/Proprietor\n4-Trust\n5-HUF\n6-Society\n7-Others \nPlease provide value as per above list: "))

typ_org = ["Government","Private Ltd","Public Ltd","Partner / Proprietor","Trust","HUF","Society","Others"]
print()
print("Type of Organisation: ",typ_org[n5])
time.sleep(1)
print("\n")

print("""
---------------------------------->
                 NATURE OF WORK    >
---------------------------------->
        """)

n6 = int(input("Nature of Work:\n0-Director\n1-Manager\n2-Team Lead\n3-Team Member\n4-Back Office\n5-Labour \nPlease provide value as per above list: "))

natofwrk = ["Director","Manager","Team Leader","Team Member","Back Office","Labour"]
print()
print("Nature of Work: ",natofwrk[n6])
time.sleep(1)
print("\n")


print("""
---------------------------------->
               TYPE OF INDUSTRY    >
---------------------------------->
        """)


n7 = int(input("Industry Type:\n0-Jewellery\n1-Import/ Export\n2-Mining\n3-Shipping\n4-Scrap Dealing\n5-Real Estate\n6-Agriculture\n7-Stock Broking\n8-Others \nPlease provide value as per above list: "))

ind_typ = ["Jewellery","Import/ Export","Mining","Shipping","Scrap Dealing","Real Estate","Agriculture","Stock Broking","Others"]

ind_oth = "N/A"

if ind_typ[n7] == "Others":

    ind_oth = input("Please specify the details of Industry: ")

print()
print("Industry Type: ",ind_typ[n7]," || Details of Industry for Other catagory: ",ind_oth)
time.sleep(1)
print("\n")

print("""
---------------------------------->
            YEARS OF EXPERIENCE    >
---------------------------------->
        """)

texpyrs = input("Total Years in Service/ Business: ")
print()
print("Total Years in Service/ Business: ",texpyrs,"years")
time.sleep(1)
print("\n")

print("""
---------------------------------->
               SOURCE OF INCOME    >
---------------------------------->
        """)


sofinc = input("Source of Income: ")
print()
print("Source of Income: ",sofinc)
time.sleep(1)
print("\n")

print("""
---------------------------------->
                  ANNUAL INCOME    >
---------------------------------->
        """)


i1 = int(input("Please confirm income frequency\n0-Monthly\n1-Annual \nPlease provide value as per above list: "))
incomefre = ["Monthly","Annual"]

incomeamt = int(input("Please income Amount: Rs."))
if incomefre[i1] == "Monthly":
    incomeamt *= 12
    
print("Annual Income: Rs.",incomeamt)
time.sleep(1)
print("\n")


#==================================================================Code Changes 17022022==AB--

print("""
||                                                                                                                                                                    ||
||                                                                                                                                                                    ||
||                                                              END OF SECTION                                                                                        ||
************************************************************************************************************************************************************************
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        """)
time.sleep(5)


print("""
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
************************************************************************************************************************************************************************
||                                                             EMPLOYMENT DETAILS SECTION                                                                             ||
||                                                                                                                                                                    ||
||                                                                                                                                                                    ||
        """)


#-------------------Code added on 10/02/2022----------------------Ashwinkumar D Basari--------

print("\n")

perm_add_line1 = input("Permanent Address: \nLine1: ")
perm_add_line2 = input("Line2: ")
perm_add_line3 = input("Line3: ")
perm_town = input("Town / City: ")
perm_pin = input("Pin Code: ")
perm_state = input("State: ")
perm_country = input("Country: ")

#capitalize & Upper words of Perm Add

perm_add_line1 = perm_add_line1.capitalize()
perm_add_line2 = perm_add_line2.capitalize()
perm_add_line3 = perm_add_line3.capitalize()
perm_town = perm_town.capitalize()
perm_state = perm_state.capitalize()
perm_country = perm_country.upper()

print("\n")
time.sleep(1)

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

#capitalize & Upper words of Communication Address

comm_add_line1 = perm_add_line1.capitalize()
comm_add_line2 = perm_add_line2.capitalize()
comm_add_line3 = perm_add_line3.capitalize()
comm_town = perm_town.capitalize()
comm_state = perm_state.capitalize()
comm_country = perm_country.upper()
print("\n")
time.sleep(1)

mobnum = int(input("Mobile Number (N): ")) #Mobile number
print("\n")
time.sleep(1)

email = input("Email Address: ") #Email Address 
print("\n")
time.sleep(1)

print("""
||                                                                                                                                                                    ||
||                                                                                                                                                                    ||
||                                                              END OF SECTION                                                                                        ||
************************************************************************************************************************************************************************
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        """)
time.sleep(5)


#-----------------Modification Section--pd: Personal Details-----------------------------------------

print("""
-------------------------------------------------------------------------------------------------
********************************** Verification of Details **************************************
-------------------------------------------------------------------------------------------------
      """)

print("\n")
time.sleep(1)

print("Please review & confirm all the below details are correct.",sep="",end="\n")

print("-----CONFIRM FOR ANY MODIFICATION IN PERSONAL DETAILS------")
print("\n")
time.sleep(1)
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
time.sleep(1)

print("**********************", "Count of Modifications: ", mod_count, "**********************")

#Code for Output data -- Start
print("\n")
# Design for Personal Details Section
print(("|"+"+"*14+"-"*40+"+"*14+"|\n"),end="")
print(("|"+" "*20+"PERSONAL INFORMATION SECTION"+" "*20+"|\n"),end="")
print(("|"+"+"*14+"-"*40+"+"*14+"|\n"),end="")

print("\n")

print("Applicants Name: ",salu,".",name,sep=" ",end="\n")
print("\n")
time.sleep(1)

print("Date of Birth: ", date_birth,"\nAge: ", age,"years")
print("\n")
time.sleep(1)

print("Sex: ", sex,"\nMarital status: ", mstat)
print("\n")
time.sleep(1)

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
time.sleep(1)

#===================Nationality & Residental===============================17022022-AB

print("Nationality: ",citizen[n1])
time.sleep(1)
print("\n")

print("Residental Status: ",res_stat[n2])
time.sleep(1)
print("\n")

print("Education Qualification: ",edu[n3])
time.sleep(1)
print("\n")

print("Occupation Detail: ",occ[n4],"|| Occupation Detail for Other catagory: ",occ_oth)
time.sleep(1)
print("\n")

print("Name of Organisation: ",org_nam)
time.sleep(1)
print("\n")

print("Type of Organisation: ",typ_org[n5])
time.sleep(1)
print("\n")

print("Nature of Work: ",natofwrk[n6])
time.sleep(1)
print("\n")

print("Industry Type: ",ind_typ[n7]," || Details of Industry for Other catagory: ",ind_oth)
time.sleep(1)
print("\n")

print("Total Years in Service/ Business: ",texpyrs,"years")
time.sleep(1)
print("\n")

print("Source of Income: ",sofinc)
time.sleep(1)
print("\n")

print("Annaul Income: Rs.",incomeamt)
time.sleep(1)
print("\n")


#===================Code written===============================17022022-AB


time.sleep(1)

print("\n")

# Design for Health Details Section
print(("|"+"+"*16+"-"*40+"+"*15+"|\n"),end="")
print(("|"+" "*20+"FAMILY & HEALTH DETAILS SECTION"+" "*20+"|\n"),end="")
print(("|"+"+"*16+"-"*40+"+"*15+"|\n"),end="")

print("\n")

weight = float(input("Weight - in kgs: "))

height = float(input("Height - in cms: "))

height = height / 100 #Height to be divide by 100 got Body Mass Index (BMI).

bmi = (weight / height)/height

bmi = round(bmi,ndigits=2) #Modified on 14022022 - AB

print("Body Mass Index: ",bmi)

bmi_indi = "Nill"

if bmi < 18:
    bmi_indi = "Underweight"

if bmi > 18 and bmi < 25:
    bmi_indi = "Healthy"

if bmi > 25 and bmi < 29.90:
    bmi_indi = "Over-Weight"

if bmi > 30.00:
    bmi_indi = "Obese"


# Design for Undersriting Details Section

print("""
|++++++++++++++++----------------------------------------+++++++++++++++|
|                     UNDERWRITING DETAILS SECTION                      |
|++++++++++++++++----------------------------------------+++++++++++++++|
""")

#risksr = 0 -- Optimized 

#risksr += 1 -- Optimized 

risksr = 1

print(risksr,".Applicant is",age_stat) #Added on 14022022 - AB
risksr += 1

print(risksr,".Applicant Age is",age, "&","Marital status is", mstat, ".Hence Risk is",risk1) #Age_Marriage Risk
risksr += 1

print(risksr,".Body mass index is",bmi, ",applicant is",bmi_indi) #Added on 14022022 - AB
risksr += 1



print("\n")

print("+"+30*"-"+"+")
print(("|"+" "*30+"|\n")*1,end="")
print(("|"+" "*6+"-"*18+" "*6+"|\n"),end="")
print(("|"+" "*6+"USN LYFE INSURANCE"+" "*6+"|\n"),end="")
print(("|"+" "*6+"-"*18+" "*6+"|\n"),end="")
print(("|"+" "*6+"-"*7+"SEAL"+"-"*7+" "*6+"|\n"),end="")
print(("|"+" "*6+"-"*18+" "*6+"|\n"),end="")
print(("|"+" "*30+"|\n")*1,end="")
print("+"+30*"-"+"+")



#Coding date 08/02/2022 - Ashwinkumar D Basari

    

