#Paid up value = ((Number of premiums paid / Total number of premiums payable) * Sum Insured) + Bonus (if any)

print("""
||||~*******************************************************************************************~||||
||||~*******************************************************************************************~||||
||||~*******************************************************************************************~||||
||||~********************SUN LIFE INSURANCE COMPANY PVT LTD*************************************~||||
||||~*******************************************************************************************~||||
||||~*******************************************************************************************~||||
||||~*******************************************************************************************~||||
||||~********We Insure Life to Protect People You Love After You********************************~||||
||||~*******************************************************************************************~||||
||||~*******************************************************************************************~||||
||||~*******************************************************************************************~||||
        """)

paidup_val = 0 #Paid up value

policy_no = int(input("Please provide Policy Number: ")) #Policy Number

policy_hldname = str(input("Please provide Policy Holders Name: ")) #Policy Holders Name

policy_type = input("Please provide Policy Plan Type\nType T-Tradition ; U-Unit LinkedInsurance Plan: ") #Policy Plan Type: T-Tradition ; U-Unit LinkedInsurance Plan

number_ann_prem_paid = int(input("Number of premiums paid (in years): ")) #Number of premiums paid-Annual

number_ann_prem_payable = int(input("Number of premiums payable or policy premium paying term (in years): ")) #Total number of premiums payable-Annual

sum_insured = int(input("Please provide Sum Insured: ")) #Sum Insured

bonus = int(input("Please provide Bonus, if applicable: ")) #Bonus (if any)

print("\n ***** Thank you for your Input ***** ",end="\n")

print("\n")

print("***************************", "Start Of Output", "***************************\n")

print("""
||||~*******************************************************************************************~||||
||||~********************SUN LIFE INSURANCE COMPANY PVT LTD*************************************~||||
||||~*******************************************************************************************~||||
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


print("***************************", "Error: ", error, "***************************\n")

print("""
||||~*******************************************************************************************~||||
||||~********************SUN LIFE INSURANCE COMPANY PVT LTD*************************************~||||
||||~*******************************************************************************************~||||
        """)


paidup_val = (((number_ann_prem_paid / number_ann_prem_payable) * sum_insured) + bonus)

print("Final Decision:\n")

print("The paid up value for Policy Number: ", policy_no, "of", policy_hldname, "is" , paidup_val)

print("\n")

print("***********************", "STATEMENT OF ESTIMATE FUTURE PAID UP VALUE", "***********************\n")

print("""
||||~*******************************************************************************************~||||
||||~********************SUN LIFE INSURANCE COMPANY PVT LTD*************************************~||||
||||~*******************************************************************************************~||||
        """)

print("**********************************", "Estimate as of Current Paid Up Value", paidup_val, "**********************************\n")

estimated = 1

estpaidup_val = paidup_val * 0.05

paidup_val += estpaidup_val

while estimated != 5:

    print("Your estimated increase in paid up value after",estimated,"years would be Rs.",round(estpaidup_val),"with Total Paid up value as Rs.",round(paidup_val))

    estimated += 1

    estpaidup_val = paidup_val * 0.05

    paidup_val += estpaidup_val

 
print("***************************************", "End Of Line", "***************************************\n")

print("\n")

print(" ***** Have a Nice Day ***** ",end="\n")

print("""
||||~*******************************************************************************************~||||
||||~********************SUN LIFE INSURANCE COMPANY PVT LTD*************************************~||||
||||~*******************************************************************************************~||||
||||~********We Insure Life to Protect People You Love After You********************************~||||
||||~*******************************************************************************************~||||
        """)
