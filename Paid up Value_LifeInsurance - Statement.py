#Paid up value = ((Number of premiums paid / Total number of premiums payable) * Sum Insured) + Bonus (if any)

from datetime import date

today= date.today()

print("Date: ", today)

import time

print("""
||||~-------------------------------------------------------------------------------------------~||||
||||~********************SUN LIFE INSURANCE COMPANY PVT LTD*************************************~||||
||||~-------------------------------------------------------------------------------------------~||||
||||~*******************************************************************************************~||||
||||~-------------------------------------------------------------------------------------------~||||
||||~********We Insure Life to Protect People You Love After You********************************~||||
||||~-------------------------------------------------------------------------------------------~||||
        """)

paidup_val = 0 #Paid up value

policy_no = int(input("Please provide Policy Number: ")) #Policy Number

policy_hldname = str(input("Please provide Policy Holders Name: ")) #Policy Holders Name

policy_type = input("Please provide Policy Plan Type\nType T-Tradition ; U-Unit LinkedInsurance Plan: ") #Policy Plan Type: T-Tradition ; U-Unit LinkedInsurance Plan

number_ann_prem_paid = int(input("Number of premiums paid (in years): ")) #Number of premiums paid-Annual

number_ann_prem_payable = int(input("Number of premiums payable or policy premium paying term (in years): ")) #Total number of premiums payable-Annual

sum_insured = int(input("Please provide Sum Insured: ")) #Sum Insured

bonus = int(input("Please provide Bonus, if applicable: ")) #Bonus (if any)

print("\n ************************************* Thank you for your Input ************************************* ",end="\n")

time.sleep(1)

print("""
||||~-------------------------------------------------------------------------------------------~||||
||||~********************SUN LIFE INSURANCE COMPANY PVT LTD*************************************~||||
||||~*****************************START OF OUTPUT***********************************************~||||
||||~-------------------------------------------------------------------------------------------~||||
        """)


error = 0

if number_ann_prem_paid <= 3:
    error += 1
    print("Error:", error, end=": ")
    print("\nThe Policy Number:", policy_no, "of", policy_hldname, "is Lapsed without any paid up value.",end="\n")
    sum_insured = 0
    bonus = 0

print("\n")

if policy_type == "U":
    error += 1
    print("Error:", error, end=": ")
    print("\nThe Policy Number:", policy_no, "of", policy_hldname, "is ULIP, paid up value is not applicable for ULIP.\n")
    sum_insured = 0
    bonus = 0
elif policy_type != "T":
    error += 1
    print("Error:", error, end=": ")
    print("\nINVALID INPUT, PLEASE CHECK.~~*****Acceptable Input U OR T*****~~\n")



print("***************************", "Error: ", error, "***************************")

time.sleep(2)

print("""
||||~-------------------------------------------------------------------------------------------~||||
||||~********************SUN LIFE INSURANCE COMPANY PVT LTD*************************************~||||
||||~-----------------------------FINAL DECISION------------------------------------------------~||||
        """)


paidup_val = (((number_ann_prem_paid / number_ann_prem_payable) * sum_insured) + bonus)

print("The paid up value for Policy Number: ", policy_no, "of", policy_hldname, "is" , round(paidup_val))

print("\n")



if paidup_val == 0:
    estimated = 6

elif paidup_val != 0:

    EstQ = input("DO YOU WISH STATEMENT OF ESTIMATE FUTURE PAID UP VALUE FOR 5 Years?\nY - Yes / N - No : ")
    

    if EstQ == "N":

        estimated = 6

    elif EstQ == "Y":

        estimated = 1

        print()

        print("""
||||~-------------------------------------------------------------------------------------------~||||
||||~********************SUN LIFE INSURANCE COMPANY PVT LTD*************************************~||||
||||~****************STATEMENT OF ESTIMATE FUTURE PAID UP VALUE*********************************~||||
||||~-------------------------------------------------------------------------------------------~||||
        """)

        print("**********************************", "Estimate as of Current Paid Up Value", paidup_val, "**********************************\n")

estpaidup_val = paidup_val * 0.05

paidup_val += estpaidup_val

while estimated != 6:

    print("Your estimated increase in paid up value after",estimated,"years would be Rs.",round(estpaidup_val),"with Total Paid up value as Rs.",round(paidup_val))

    estimated += 1

    estpaidup_val = paidup_val * 0.05

    paidup_val += estpaidup_val

    time.sleep(1)

 
print("""
||||~-------------------------------------------------------------------------------------------~||||
||||~********************SUN LIFE INSURANCE COMPANY PVT LTD*************************************~||||
||||~*******************************END OF OUTPUT***********************************************~||||
||||~-------------------------------------------------------------------------------------------~||||
        """)

time.sleep(2)

print("\n")

print(" ************************************* HAVE A NICE DAY !!! ********************************** ",end="\n")

print("""
||||~-------------------------------------------------------------------------------------------~||||
||||~********************SUN LIFE INSURANCE COMPANY PVT LTD*************************************~||||
||||~*******************************************************************************************~||||
||||~********We Insure Life to Protect People You Love After You******************************ab~||||
||||~-------------------------------------------------------------------------------------------~||||
        """)


#Added Date selction at top: AB 
